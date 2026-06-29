from __future__ import annotations

import struct
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import numpy as np


# ── 数据类 ──────────────────────────────────────────────────────

@dataclass(frozen=True)
class EvtHeader:
    """EVT 文件全局头段信息。"""
    station_id: int
    station_name: str
    instrument: str
    latitude: float
    longitude: float
    elevation_m: float
    component_count: int
    data_format: int
    record_time: datetime | None
    preamble_count: int   # 数据区前导 int32 个数
    total_samples: int    # 每分量样本数


@dataclass(frozen=True)
class EvtData:
    """EVT 三分量数据（已去前导、分块）。"""
    header: EvtHeader
    ew: np.ndarray   # float64
    ns: np.ndarray   # float64
    ud: np.ndarray   # float64

    @property
    def sample_count(self) -> int:
        return int(self.ew.size)


# ── 公共 API ────────────────────────────────────────────────────

def read_evt(file_path: str | Path) -> EvtData:
    """读取 EVT 文件，返回三分量数据。

    EVT 数据区格式（int32 顺序三块）：
      [preamble int32] [UD block int32] [NS block int32] [EW block int32]

    Parameters
    ----------
    file_path : str or Path

    Returns
    -------
    EvtData
    """
    file_path = Path(file_path)
    data = np.fromfile(file_path, dtype=np.uint8)

    if b"digital event" not in data[:16].tobytes():
        raise ValueError(f"不是有效的 EVT 文件: {file_path}")

    # ── 全局头段 ──
    station_id = int(struct.unpack_from("<I", data, 0x100)[0])
    fmt_flag   = int(struct.unpack_from("<H", data, 0x10A)[0])

    record_time = _parse_evt_time(
        int(struct.unpack_from("<H", data, 0x10C)[0]),
        int(struct.unpack_from("<H", data, 0x10E)[0]),
        int(struct.unpack_from("<H", data, 0x110)[0]),
        int(struct.unpack_from("<H", data, 0x112)[0]),
        int(struct.unpack_from("<H", data, 0x114)[0]),
        int(struct.unpack_from("<H", data, 0x116)[0]),
        file_path,
    )

    station_name = _clean_str(data[0x11C:0x11C + 16].tobytes())
    instrument   = _clean_str(data[0x12C:0x12C + 16].tobytes())
    latitude     = float(struct.unpack_from("<f", data, 0x7C)[0])
    longitude    = float(struct.unpack_from("<f", data, 0x80)[0])
    elevation_m  = float(struct.unpack_from("<f", data, 0x84)[0])

    # ── 数据区 ──
    data_start = _find_data_start(data)
    raw = data[data_start:]                  # uint8
    n_int32 = len(raw) // 4
    arr = raw[:n_int32 * 4].view(np.int32)   # 所有 int32

    preamble = _find_preamble_int32(arr)
    body = arr[preamble:]                    # 去掉前导
    n_per = len(body) // 3                   # 每分量样本数
    body = body[:n_per * 3]                  # 截齐

    # 三块顺序：UD / NS / EW（与现有 COMPONENT_NAMES 一致: 0=UD, 1=NS, 2=EW）
    ud = body[0 * n_per:1 * n_per].astype(np.float64)
    ns = body[1 * n_per:2 * n_per].astype(np.float64)
    ew = body[2 * n_per:3 * n_per].astype(np.float64)

    header = EvtHeader(
        station_id=station_id,
        station_name=station_name,
        instrument=instrument,
        latitude=latitude,
        longitude=longitude,
        elevation_m=elevation_m,
        component_count=3,
        data_format=fmt_flag,
        record_time=record_time,
        preamble_count=preamble,
        total_samples=n_per,
    )

    return EvtData(header=header, ew=ew, ns=ns, ud=ud)


# ── 内部函数 ────────────────────────────────────────────────────

def _clean_str(raw: bytes) -> str:
    text = raw.rstrip(b"\x00").decode("latin-1", errors="replace")
    return "".join(ch if ch.isprintable() or ch in "\n\r\t" else " "
                   for ch in text).strip()


def _parse_evt_time(year: int, doy: int, h: int, m: int, s: int, ms: int,
                    file_path: Path) -> datetime | None:
    import re
    m = re.search(r"(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})", file_path.stem)
    if m:
        try:
            return datetime(int(m[1]), int(m[2]), int(m[3]), int(m[4]), int(m[5]))
        except ValueError:
            pass
    try:
        y = 2000 + year if year < 100 else year
        if 1 <= doy <= 366:
            from datetime import timedelta
            return (datetime(y, 1, 1) + timedelta(days=doy - 1)).replace(
                hour=h % 24, minute=m % 60, second=s % 60,
                microsecond=(ms % 1000) * 1000)
    except (ValueError, OverflowError):
        pass
    return None


def _find_data_start(data: np.ndarray) -> int:
    """查找数据区起始位置。"""
    raw_bytes = data.tobytes()
    for marker in (b"E-W", b"N-S"):
        pos = raw_bytes.find(marker)
        if pos >= 4:
            seg_start = pos - 4
            n_calib = struct.unpack_from("<I", raw_bytes, seg_start + 32)[0]
            if 0 < n_calib < 50:
                return seg_start + 36 + n_calib * 8
    return 0x322C


def _find_preamble_int32(arr: np.ndarray) -> int:
    """找到连续合理 int32 数据段的起始位置。

    前导部分通常包含大量零值及孤立异常值，
    这里寻找第一个前后 50 个值都在合理范围 (abs < 1000万) 的索引。
    """
    ok = (arr > 100) & (arr < 10_000_000)
    # 滑动窗口：连续 50 个 ok 即视为数据开始
    window = np.convolve(ok.astype(np.int32), np.ones(50, dtype=np.int32), mode='valid')
    hits = np.where(window >= 50)[0]
    return int(hits[0]) if len(hits) > 0 else 0


def find_first_valid_frame(evt_data: EvtData) -> int:
    """返回前导 int32 个数（对应原始文件中的偏移，用于溯源）。"""
    return evt_data.header.preamble_count


def get_component_array(evt_data: EvtData, component: str) -> np.ndarray:
    mapping = {"EW": evt_data.ew, "NS": evt_data.ns, "UD": evt_data.ud}
    if component not in mapping:
        raise ValueError(f"未知分量名: {component}，可选: EW, NS, UD")
    return mapping[component]