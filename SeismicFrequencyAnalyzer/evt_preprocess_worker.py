# -*- coding: utf-8 -*-
"""EVT 预处理后台工作线程。

read_evt() 已完成：50-block 解码 + 前导切除。
此 Worker：读取 → 联合搜索 → 导出 TXT（兼容现有频谱分析）。
支持单文件或目录批量处理。
"""

from __future__ import annotations

import traceback
from pathlib import Path

from PyQt5.QtCore import QObject, pyqtSignal

from evt_reader import read_evt
from segment_selector import find_best_segment_three_component
from dat_exporter import export_three_component_dat


class EvtPreprocessWorker(QObject):
    """后台处理 EVT 文件：三分量联合筛选 → 导出 TXT。

    支持批量：传入一组 EVT 文件路径，逐个处理。
    单个文件失败不会中断整体流程，错误会记录到日志。
    """

    log = pyqtSignal(str)
    # output_dir, [txt_path, ...], [results, ...]
    finished = pyqtSignal(str, list, list)
    failed = pyqtSignal(str)

    def __init__(
        self,
        evt_paths: list[Path],
        output_dir: Path,
        window_size: int,
        instrument_sample_rate_hz: float,
        step: int | None = None,
    ) -> None:
        super().__init__()
        self.evt_paths = list(evt_paths)
        self.output_dir = output_dir
        self.window_size = window_size
        self.instrument_sample_rate_hz = instrument_sample_rate_hz
        self.step = step

    def run(self) -> None:
        try:
            total = len(self.evt_paths)
            self.log.emit(f"=== EVT 批量预处理：共 {total} 个文件 ===")
            self.output_dir.mkdir(parents=True, exist_ok=True)

            txt_paths: list[str] = []
            results_list: list[dict] = []
            ok_count = 0
            fail_count = 0

            for i, evt_path in enumerate(self.evt_paths, start=1):
                self.log.emit("")
                self.log.emit(f"[{i}/{total}] 处理: {evt_path.name}")
                try:
                    results = self._process_one(evt_path)
                    if results is not None:
                        txt_paths.append(results["txt_path"])
                        results_list.append(results)
                        ok_count += 1
                except Exception as exc:
                    fail_count += 1
                    self.log.emit(f"  ✗ 处理失败: {exc}")
                    self.log.emit(traceback.format_exc())

            self.log.emit("")
            self.log.emit(
                f"=== 批量完成：成功 {ok_count} 个，失败 {fail_count} 个 ==="
            )
            self.finished.emit(
                str(self.output_dir), txt_paths, results_list
            )

        except Exception as exc:
            details = traceback.format_exc()
            self.failed.emit(f"{exc}\n\n{details}")

    def _process_one(self, evt_path: Path) -> dict | None:
        """处理单个 EVT 文件，返回结果字典。"""
        self.log.emit(f"  读取 EVT 文件: {evt_path.name}")
        evt = read_evt(evt_path)
        h = evt.header

        self.log.emit(
            f"  台站: {h.station_name or '(未知)'} | "
            f"仪器: {h.instrument or '(未知)'} | "
            f"坐标: ({h.latitude:.4f}, {h.longitude:.4f})"
        )
        self.log.emit(
            f"  前导 int32: {h.preamble_int32} | "
            f"有效数据: {evt.sample_count} 点/分量 | "
            f"采样率: {self.instrument_sample_rate_hz:.0f} Hz | "
            f"窗口: {self.window_size} 点"
        )
        self.log.emit(
            f"  时长: {evt.sample_count / self.instrument_sample_rate_hz:.1f} s "
            f"@ {self.instrument_sample_rate_hz:.0f} Hz"
        )

        ew = evt.ew
        ns = evt.ns
        ud = evt.ud

        if evt.sample_count < self.window_size:
            self.log.emit(
                f"  ⚠ 有效数据 {evt.sample_count} 点 < 窗口 {self.window_size} 点，跳过"
            )
            return None

        # 三分量联合搜索最优窗口
        step_label = f"步长={self.step}" if self.step else "步长=auto"
        self.log.emit(
            f"  三分量联合搜索最优数据段 (窗口={self.window_size}, {step_label})..."
        )
        result = find_best_segment_three_component(
            ew=ew, ns=ns, ud=ud,
            window_size=self.window_size,
            sample_rate_hz=self.instrument_sample_rate_hz,
            step=self.step,
            progress_callback=None,
        )
        bw = result.best_window

        # 计算截取起始时间（秒）
        start_time_s = bw.start_index / self.instrument_sample_rate_hz

        self.log.emit(
            f"  最优窗口: [{bw.start_index}, {bw.end_index}) "
            f"({start_time_s:.1f}s 起) "
            f"综合={bw.total_score:.4f} "
            f"EW={bw.ew_score:.4f} NS={bw.ns_score:.4f} "
            f"UD={bw.ud_score:.4f}"
        )

        # 导出为 txt — 文件名: {原数据名}_{开始时间}s.txt
        base_name = evt_path.stem
        txt_name = f"{base_name}_{start_time_s:.1f}s.txt"
        txt_path = self.output_dir / txt_name

        export_three_component_dat(
            ew_data=result.ew_data,
            ns_data=result.ns_data,
            ud_data=result.ud_data,
            output_path=txt_path,
            sample_rate_hz=self.instrument_sample_rate_hz,
            start_sample_index=bw.start_index,
            end_sample_index=bw.end_index,
            original_file=evt_path.name,
            record_time=str(h.record_time) if h.record_time else "",
            extra_metadata={
                "window_score": f"{bw.total_score:.4f}",
                "ew_score": f"{bw.ew_score:.4f}",
                "ns_score": f"{bw.ns_score:.4f}",
                "ud_score": f"{bw.ud_score:.4f}",
            },
        )

        self.log.emit(f"  已导出: {txt_path.name}")

        return {
            "txt_path": str(txt_path),
            "evt_name": evt_path.name,
            "start_index": bw.start_index,
            "end_index": bw.end_index,
            "score": bw.total_score,
            "ew_score": bw.ew_score,
            "ns_score": bw.ns_score,
            "ud_score": bw.ud_score,
            "sample_count": len(result.ew_data),
            "sample_rate": self.instrument_sample_rate_hz,
        }