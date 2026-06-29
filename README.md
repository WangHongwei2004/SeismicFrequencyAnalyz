# 宽频带地震动卓越频率分析

一个用于宽频带地震动 TXT/DAT 数据批量处理、频谱绘图和卓越频率判读的 PyQt5 桌面工具。
v1.1.0 新增 EVT 原始数据智能裁剪功能，可自动筛选最优线性数据段并导出为 DAT 格式。

软件版本：`v1.1.0`  
作者：`WHW`  
完成时间：`2026.6.27`（v1.0.0），`2026.6.29`（v1.1.0 EVT 裁剪）  
GitHub：<https://github.com/WangHongwei2004>

## 功能特性

### 频谱分析（v1.0.0）
- 支持批量读取 `SeismicFrequencyAnalyzer/data` 中的三分量地震动 TXT 数据。
- 原始数据文件不随仓库发布，请在本地自行放入 TXT 数据。
- 同时计算直接法频谱和间接法功率谱密度。
- 自动生成原始计数时程图、校正加速度时程图、直接法频谱图、间接法频谱图。
- 在频谱图中标注 P1-P4 候选峰，辅助选择合理的卓越频率。
- 将各分量和平均谱的卓越频率、周期、峰值和 P1-P4 候选峰写入 CSV。
- 提供 PyQt5 图形界面，可设置选峰范围、显示频率上限和实际处理点数。

### EVT 原始数据智能裁剪（v1.1.0 新增）
- 支持直接读取 EDAS-24 系列数字地震仪生成的 `.evt` 原始二进制文件。
- **自动筛选最优数据段**：滑动窗口 + 四维评分算法，自动选出最平稳、干扰最小的数据段。
  - 平稳性评分：子窗口统计量（均值/标准差）一致性
  - 弯曲度惩罚：二次拟合显著优于线性拟合 → 有弯曲漂移
  - 尖峰检测：基于 MAD 鲁棒统计的异常值检测
  - 死数据惩罚：全零/常量段
- 用户可自定义截取长度（1024/2048/4096/8192 点，或自定义任意点数）。
- 支持手动选择目标采样率：保持原始 / 50 Hz / 100 Hz / 200 Hz。
- 支持按分量选择（EW/NS/UD 多选）。
- 裁剪结果导出为 DAT 格式，文件头完整记录元信息。

## 项目结构

```text
.
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
├── SeismicFrequencyAnalyzer.spec
├── SeismicFrequencyAnalyzer/
│   ├── analysis_ui.py                         # PyQt5 图形界面入口
│   ├── analysis_worker.py                     # 后台频谱分析线程
│   ├── evt_preprocess_worker.py               # 后台 EVT 预处理线程（v1.1.0）
│   ├── evt_reader.py                          # EDAS EVT 二进制格式解析器（v1.1.0）
│   ├── segment_selector.py                    # 最优数据段自动筛选算法（v1.1.0）
│   ├── dat_exporter.py                        # DAT 格式导出模块（v1.1.0）
│   ├── app_info.py                            # 软件版本、作者和默认配置
│   ├── dominant_frequency_two_methods.py      # 直接法/间接法主分析流程
│   ├── ui_style.py                            # 界面样式表
│   ├── data/                                  # 本地 TXT 数据目录，原始数据不提交
│   ├── evt_dat_output/                        # EVT 裁剪 DAT 输出目录（v1.1.0）
│   └── two_method_spectrum_output/            # 直接法/间接法频谱分析结果
├── tools/
│   └── generate_copyright_docs.py             # 软著文档生成工具
├── build/                                     # PyInstaller 构建缓存，建议不提交
└── dist/                                      # 打包后的 exe，建议发布时单独上传
```

## 环境安装

建议使用 Python 3.10 或更高版本。

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

如果使用 Anaconda，也可以在当前环境中直接执行：

```powershell
python -m pip install -r requirements.txt
```

### 依赖

| 包 | 用途 |
|----|------|
| `numpy` | 数值计算、FFT、多项式拟合 |
| `matplotlib` | 频谱图、时程图绘制 |
| `PyQt5` | 图形界面 |

## 图形界面运行

```powershell
python SeismicFrequencyAnalyzer\analysis_ui.py
```

### EVT 预处理面板

界面顶部为 **"EVT 数据预处理 — 自动筛选最优线性段"** 面板：

1. **选择 EVT 文件**：点击"浏览..."选择 `.evt` 原始数据文件。
2. **设置截取长度**：从下拉框选择预设值（1024/2048/4096/8192 点），或勾选"自定义"手动输入任意点数。
3. **目标采样率**：选择"保持原始采样率"或指定 50/100/200 Hz（通过 FFT 重采样）。
4. **处理分量**：勾选需要处理的 EW/NS/UD 分量。
5. **点击"裁剪并导出 DAT"**：后台自动解析 EVT → 搜索最优窗口 → 导出 DAT 文件。
6. 处理完成后点击"打开 DAT 输出目录"查看结果。

### 频谱分析面板

界面默认设置：

- 数据目录：`SeismicFrequencyAnalyzer/data`
- 输出目录：`SeismicFrequencyAnalyzer/two_method_spectrum_output`
- 选峰上限为 `0` 时表示不设上限，搜索到 Nyquist 频率。
- 频谱图显示上限为 `0` 时表示显示到 Nyquist 频率。
- 实际处理点数为 `0` 时表示使用全部样本。

## 命令行运行

### 频谱分析

```powershell
python SeismicFrequencyAnalyzer\dominant_frequency_two_methods.py
```

常用参数示例：

```powershell
python SeismicFrequencyAnalyzer\dominant_frequency_two_methods.py `
  --data-dir SeismicFrequencyAnalyzer\data `
  --output-dir SeismicFrequencyAnalyzer\two_method_spectrum_output `
  --min-peak-frequency 1 `
  --max-peak-frequency 25 `
  --plot-max-frequency 25
```

说明：如果低频漂移影响卓越频率判断，建议将 `--min-peak-frequency` 或界面中的"选峰下限 Hz"设置为 `1` 或 `2`，再重新运行。

### EVT 裁剪（Python 脚本调用）

```python
from evt_reader import read_evt, find_first_valid_frame, get_component_array
from segment_selector import find_best_segment
from dat_exporter import export_dat

# 读取 EVT
evt = read_evt("path/to/file.evt")
first = find_first_valid_frame(evt)
ew = get_component_array(evt, "EW")[first:]

# 搜索最优窗口
result = find_best_segment(ew, window_size=2048,
                           sample_rate_hz=evt.header.sample_rate_hz)
bw = result.best_window

# 导出 DAT
export_dat(
    data=result.data,
    output_path="output_EW.dat",
    component="EW",
    sample_rate_hz=evt.header.sample_rate_hz,
    start_sample_index=first + bw.start_index,
    end_sample_index=first + bw.end_index,
    original_file="file.evt",
)
```

## 输出文件

### 频谱分析输出

每个输入文件会生成一个同名子目录，包含：

- `*_01_raw_counts_time_history.png`
- `*_02_corrected_acceleration_time_history_um_s2.png`
- `*_03_direct_spectrum.png`
- `*_04_indirect_spectrum.png`

汇总表：

- `component_direct_indirect_results.csv`

CSV 中包含直接法和间接法的卓越频率、卓越周期、峰值，以及 P1-P4 候选峰频率、周期和峰值。

### EVT 裁剪 DAT 输出

输出目录：`SeismicFrequencyAnalyzer/evt_dat_output/`

每个分量生成一个 `.dat` 文件，命名格式：`{原始文件名}_{分量}.dat`

DAT 文件格式（文本文件，UTF-8 编码）：

```
; DAT Export - SeismicFrequencyAnalyzer
; Export time: 2026-06-29 15:03:48
;
; Original file: 202606071041.evt
; Record time: 2026-06-07 10:41:00
; Original sample rate: 131.6400 Hz
; Component: EW
; Data type: raw counts (int16)
;
; --- Extraction info ---
; Start sample index: 71919
; End sample index:   72943
; Extracted samples:  1024
; Start time: 546.330905 s
; End time:   554.109696 s
; Duration:   7.778791 s
; Sample rate: 131.6400 Hz
; samp: 131.6400
;
; Data length: 1024
; --- Begin data ---
6.000000
9348.000000
...
```

头信息说明：

| 字段 | 含义 |
|------|------|
| `Original file` | 原始 EVT 文件名 |
| `Record time` | 原始数据记录时间 |
| `Original sample rate` | 原始采样率 |
| `Component` | 分量名（EW/NS/UD） |
| `Start sample index` | 截取起始点号（相对于原始文件全帧） |
| `End sample index` | 截取结束点号（不含） |
| `Extracted samples` | 截取数据点数 |
| `Start/End time` | 截取起止时间（秒） |
| `samp` | 采样率（兼容现有 TXT 格式解析）|

## 打包

确认功能稳定后，可以使用 PyInstaller 打包：

```powershell
python -m PyInstaller SeismicFrequencyAnalyzer.spec --noconfirm
```

生成文件位于 `dist/SeismicFrequencyAnalyzer.exe`。

## 许可协议

本项目使用自定义非商业科研教学许可协议，允许个人自用、教学、科研、课程实验、非商业评估和非商业二次开发。

未经作者书面授权，不允许将本软件或其衍生版本用于商业产品、商业服务、付费咨询、付费培训、商业数据处理、商业工作流集成、转售、租赁、再许可或其他以商业利益为主要目的的场景。

如需商业授权，请通过作者 GitHub 主页联系：<https://github.com/WangHongwei2004>。

提交到 GitHub 时，建议提交源码、README、requirements、LICENSE 和必要占位文件；`build/`、`dist/`、`__pycache__/`、原始数据、分析输出图和 CSV 属于本地文件或生成物，默认通过 `.gitignore` 排除。