# 瀹介甯﹀湴闇囧姩鍗撹秺棰戠巼鍒嗘瀽

![鐗堟湰](https://img.shields.io/badge/version-v1.1.0-blue)
![璁稿彲](https://img.shields.io/badge/license-闈炲晢涓氱鐮旀暀瀛﹁鍙?green)
![骞冲彴](https://img.shields.io/badge/platform-Windows-lightgrey)
![Python](https://img.shields.io/badge/python-3.10+-yellow)

> **馃摜 [涓嬭浇 Windows 鍙墽琛岀▼搴忥紙.exe锛塢(https://github.com/WangHongwei2004/SeismicFrequencyAnalyzer/releases/latest)** 鈥斺€?鏃犻渶瀹夎 Python锛岃В鍘嬪嵆鐢ㄣ€?
[![涓嬭浇 exe](https://img.shields.io/badge/猬?20涓嬭浇-SeismicFrequencyAnalyzer.exe-blue?style=for-the-badge&logo=windows)](https://github.com/WangHongwei2004/SeismicFrequencyAnalyzer/releases/latest)

涓€涓敤浜庡棰戝甫鍦伴渿鍔ㄦ暟鎹壒閲忓鐞嗐€侀璋辩粯鍥惧拰鍗撹秺棰戠巼鍒よ鐨?PyQt5 妗岄潰宸ュ叿銆傛敮鎸佺洿鎺ヨ鍙?EDAS-24 绯诲垪鏁板瓧鍦伴渿浠敓鎴愮殑 EVT 鍘熷浜岃繘鍒舵枃浠讹紝鑷姩绛涢€夋渶浼樼嚎鎬ф暟鎹锛屽啀杩涜鐩存帴娉?闂存帴娉曢璋卞垎鏋愩€?
杞欢鐗堟湰锛歚v1.1.0`
浣滆€咃細`WHW`
瀹屾垚鏃堕棿锛歚2026.6.27`锛坴1.0.0锛夛紝`2026.6.30`锛坴1.1.0 EVT 鏅鸿兘瑁佸壀锛?
椤圭洰鍦板潃锛?https://github.com/WangHongwei2004/SeismicFrequencyAnalyzer>

---

## 鐩綍

- [鍔熻兘鐗规€(#鍔熻兘鐗规€?
- [杞欢鎴浘](#杞欢鎴浘)
- [椤圭洰缁撴瀯](#椤圭洰缁撴瀯)
- [蹇€熷紑濮媇(#蹇€熷紑濮?
- [鍥惧舰鐣岄潰浣跨敤](#鍥惧舰鐣岄潰浣跨敤)
- [鍛戒护琛屼娇鐢╙(#鍛戒护琛屼娇鐢?
- [杈撳嚭鏂囦欢](#杈撳嚭鏂囦欢)
- [绠楁硶鍘熺悊](#绠楁硶鍘熺悊)
- [鎵撳寘](#鎵撳寘)
- [璁稿彲鍗忚](#璁稿彲鍗忚)

---

## 鍔熻兘鐗规€?
### EVT 鍘熷鏁版嵁鏅鸿兘瑁佸壀锛坴1.1.0 鏍稿績锛?
瑙ｅ喅瀹介甯﹀湴闇囦华鍘熷鏁版嵁闈炵嚎鎬ф紓绉汇€佸惈澶ч噺骞叉壈銆佹棤娉曠洿鎺ュ幓绾挎紓鐨勯棶棰樸€?
- **鐩存帴璇诲彇 EVT 浜岃繘鍒?*锛氳В鏋?EDAS-24 绯诲垪鏁板瓧鍦伴渿浠敓鎴愮殑 `.evt` 鏂囦欢锛屾纭В鐮?int32 椤哄簭涓夊潡锛圲D/NS/EW锛夋暟鎹牸寮忋€?- **鎵归噺澶勭悊**锛氭敮鎸侀€夋嫨鍗曚釜鏂囦欢鎴栨暣涓洰褰曪紝涓€娆℃€ф壒閲忚鍓墍鏈?`.evt` 鏂囦欢銆傚崟涓枃浠跺け璐ヤ笉褰卞搷鏁翠綋娴佺▼銆?- **涓夊垎閲忚仈鍚堣嚜鍔ㄧ瓫閫夋渶浼樻暟鎹**锛氭粦鍔ㄧ獥鍙?+ 鍥涚淮璇勫垎绠楁硶锛屽鍚屼竴绐楀彛浣嶇疆鐨勪笁鍒嗛噺鍒嗗埆璇勫垎鍚庡彇骞冲潎锛?*纭繚涓夊垎閲忔椂闂村榻?*锛堜笉浼氬悇鍙栧悇鐨勬渶浼樻锛夈€?  - **骞崇ǔ鎬ц瘎鍒?*锛堟潈閲?0.50锛夛細瀛愮獥鍙ｇ粺璁￠噺锛堝潎鍊?鏍囧噯宸級涓€鑷存€?  - **寮洸搴︽儵缃?*锛堟潈閲?0.25锛夛細浜屾鎷熷悎鏄捐憲浼樹簬绾挎€ф嫙鍚?鈫?鏈夊集鏇叉紓绉伙紝閲嶇綒
  - **灏栧嘲妫€娴?*锛堟潈閲?0.10锛夛細鍩轰簬 MAD锛堜腑浣嶆暟缁濆鍋忓樊锛夐瞾妫掔粺璁＄殑寮傚父鍊兼娴?  - **姝绘暟鎹儵缃?*锛堟潈閲?0.15锛夛細鍏ㄩ浂/甯搁噺娈?- **閲囨牱鐜囧畬鍏ㄧ敱鐢ㄦ埛璁剧疆**锛?0 Hz / 100 Hz / 200 Hz锛堥粯璁?50 Hz锛夈€備笉璇诲彇 EVT 鍐呴儴閲囨牱鐜囧弬鏁帮紝鍥犱负閭ｆ槸浠櫒鍐呴儴鍊间笉鍙潬锛涚敤鎴疯缃殑鎵嶆槸鍦伴渿浠疄闄呭伐浣滈噰鏍风巼锛屾墍鏈夋埅鍙栭暱搴﹀拰鏃堕棿璁＄畻閮藉熀浜庢銆?- **鎴彇闀垮害鍙嚜瀹氫箟**锛氶璁?1024/2048/4096/8192 鐐癸紝鎴栧嬀閫?鑷畾涔?杈撳叆浠绘剰鐐规暟銆?- **婊戝姩姝ラ暱鍙嚜瀹氫箟**锛氳嚜鍔紙绐楀彛/4锛? 128 鐐?/ 256 鐐?/ 512 鐐癸紝姝ラ暱瓒婂皬閫夊彇瓒婄簿缁嗐€?- **杈撳嚭鏂囦欢鍚嶇洿瑙?*锛歚{鍘熷鏂囦欢鍚峿_{鎴彇璧峰鏃堕棿}s.txt`锛屼緥濡?`202606071041_568.4s.txt`銆?- **瀵煎嚭鏍煎紡鍏煎**锛氳鍓粨鏋滃鍑轰负鍗曚釜 TXT 鏂囦欢锛堟斁鍏?`data/` 鐩綍锛夛紝鏍煎紡鍏煎鐜版湁 `load_traces()` 瑙ｆ瀽閫昏緫锛屽彲鐩存帴杩涘叆棰戣氨鍒嗘瀽娴佺▼銆傛枃浠跺ご璁板綍瑁佸壀鍏冧俊鎭紙璧峰/缁撴潫鐐瑰彿銆佹椂闂淬€佸緱鍒嗭級銆?
### 棰戣氨鍒嗘瀽锛坴1.0.0 + v1.1.0 澧炲己锛?
- 鎵归噺璇诲彇 `data/` 鐩綍涓殑涓夊垎閲忓湴闇囧姩 TXT/DAT 鏁版嵁锛堟敮鎸?`.txt` 鍜?`.dat` 涓ょ鎵╁睍鍚嶏級銆?- 鍘熷鏁版嵁鏂囦欢涓嶉殢浠撳簱鍙戝竷锛岃鍦ㄦ湰鍦拌嚜琛屾斁鍏ャ€?- 鍚屾椂璁＄畻**鐩存帴娉曢璋?*锛團FT 鈫?骞呭€艰氨 鈫?骞虫柟 鈫?鍔熺巼璋憋級鍜?*闂存帴娉曞姛鐜囪氨瀵嗗害**锛堣嚜鐩稿叧 鈫?FFT 鈫?闄や互棰戠巼鍒嗚鲸鐜囷級銆?- 鑷姩鐢熸垚鍥涘紶鍥撅細鍘熷璁℃暟鏃剁▼銆佹牎姝ｅ姞閫熷害鏃剁▼锛堝幓浠櫒鍝嶅簲/闆舵紓/绾挎紓锛夈€佺洿鎺ユ硶棰戣氨銆侀棿鎺ユ硶棰戣氨銆?- 棰戣氨鍥句腑鏍囨敞 P1-P4 鍊欓€夊嘲锛岃緟鍔╅€夋嫨鍚堢悊鐨勫崜瓒婇鐜囥€?- **CSV 鏂板鏃跺煙宄板€煎姞閫熷害锛埼糾/s虏锛?*锛氬垪鍑烘瘡涓垎閲忔牎姝ｅ悗鍔犻€熷害鐨勬椂鍩熷嘲鍊笺€?- 榛樿鍙傛暟宸蹭紭鍖栵細閫夊嘲鑼冨洿 1-8 Hz銆侀璋辨樉绀轰笂闄?15 Hz锛堝父鐢ㄨ寖鍥达級锛屽潎鍙墜鍔ㄤ慨鏀广€?- 鎻愪緵 PyQt5 鍥惧舰鐣岄潰锛岀獥鍙ｅ鏁烇紙1460脳1180锛夛紝鍙缃€夊嘲鑼冨洿銆佹樉绀洪鐜囦笂闄愬拰瀹為檯澶勭悊鐐规暟銆?
---

## 杞欢鎴浘

杞欢涓荤晫闈紙v1.1.0锛夊寘鍚?EVT 棰勫鐞嗛潰鏉裤€侀璋卞垎鏋愯矾寰勪笌鍙傛暟銆佽繍琛屾棩蹇楋細

> 涓荤晫闈㈡埅鍥捐椤圭洰 `docs/` 鐩綍鎴?GitHub Release 椤甸潰闄勫浘銆?
---

## 椤圭洰缁撴瀯

```text
.
鈹溾攢鈹€ README.md
鈹溾攢鈹€ requirements.txt                            # numpy, matplotlib, PyQt5
鈹溾攢鈹€ LICENSE
鈹溾攢鈹€ .gitignore
鈹溾攢鈹€ SeismicFrequencyAnalyzer.spec               # PyInstaller 鎵撳寘閰嶇疆
鈹溾攢鈹€ SeismicFrequencyAnalyzer/
鈹?  鈹溾攢鈹€ analysis_ui.py                          # PyQt5 鍥惧舰鐣岄潰鍏ュ彛
鈹?  鈹溾攢鈹€ analysis_worker.py                      # 鍚庡彴棰戣氨鍒嗘瀽绾跨▼
鈹?  鈹溾攢鈹€ evt_preprocess_worker.py                # 鍚庡彴 EVT 鎵归噺棰勫鐞嗙嚎绋嬶紙v1.1.0锛?鈹?  鈹溾攢鈹€ evt_reader.py                           # EDAS EVT 浜岃繘鍒舵牸寮忚В鏋愬櫒锛坴1.1.0锛?鈹?  鈹溾攢鈹€ segment_selector.py                     # 鏈€浼樻暟鎹鑷姩绛涢€夌畻娉曪紙v1.1.0锛?鈹?  鈹溾攢鈹€ dat_exporter.py                         # DAT/TXT 鏍煎紡瀵煎嚭妯″潡锛坴1.1.0锛?鈹?  鈹溾攢鈹€ app_info.py                             # 杞欢鐗堟湰銆佷綔鑰呭拰榛樿閰嶇疆
鈹?  鈹溾攢鈹€ dominant_frequency_two_methods.py       # 鐩存帴娉?闂存帴娉曚富鍒嗘瀽娴佺▼
鈹?  鈹溾攢鈹€ ui_style.py                             # 鐣岄潰鏍峰紡琛?鈹?  鈹溾攢鈹€ data/                                   # 鏈湴鏁版嵁鐩綍锛圱XT + EVT 瑁佸壀杈撳嚭锛?鈹?  鈹斺攢鈹€ two_method_spectrum_output/             # 棰戣氨鍒嗘瀽缁撴灉锛堝浘 + CSV锛?鈹溾攢鈹€ tools/
鈹?  鈹斺攢鈹€ generate_copyright_docs.py              # 杞憲鏂囨。鐢熸垚宸ュ叿
鈹溾攢鈹€ docs/                                       # 杞憲鏂囨。涓庢埅鍥?鈹溾攢鈹€ build/                                      # PyInstaller 鏋勫缓缂撳瓨锛堜笉鎻愪氦锛?鈹斺攢鈹€ dist/                                       # 鎵撳寘鍚庣殑 exe锛堝彂甯冩椂鍗曠嫭涓婁紶锛?```

---

## 蹇€熷紑濮?
### 鏂瑰紡涓€锛氫笅杞?exe锛堟帹鑽愭櫘閫氱敤鎴凤級

鍓嶅線 [Releases 椤甸潰](https://github.com/WangHongwei2004/SeismicFrequencyAnalyzer/releases/latest) 涓嬭浇 `SeismicFrequencyAnalyzer.exe`锛屽弻鍑昏繍琛屽嵆鍙紝鏃犻渶瀹夎 Python 鐜銆?
[![涓嬭浇 exe](https://img.shields.io/badge/猬?20涓嬭浇-SeismicFrequencyAnalyzer.exe-blue?style=for-the-badge&logo=windows)](https://github.com/WangHongwei2004/SeismicFrequencyAnalyzer/releases/latest)

### 鏂瑰紡浜岋細浠庢簮鐮佽繍琛?
寤鸿浣跨敤 Python 3.10 鎴栨洿楂樼増鏈€?
```powershell
git clone https://github.com/WangHongwei2004/SeismicFrequencyAnalyzer.git
cd SeismicFrequencyAnalyzer
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python SeismicFrequencyAnalyzer\analysis_ui.py
```

#### 渚濊禆

| 鍖?| 鐢ㄩ€?|
|----|------|
| `numpy` | 鏁板€艰绠椼€丗FT銆佸椤瑰紡鎷熷悎 |
| `matplotlib` | 棰戣氨鍥俱€佹椂绋嬪浘缁樺埗 |
| `PyQt5` | 鍥惧舰鐣岄潰 |

---

## 鍥惧舰鐣岄潰浣跨敤

鍚姩鍚庣晫闈㈠垎涓轰笂涓嬩袱閮ㄥ垎锛?*EVT 棰勫鐞?*锛堜笂锛夊拰 **棰戣氨鍒嗘瀽**锛堜笅锛夈€?
### EVT 棰勫鐞嗛潰鏉?
1. **閫夋嫨 EVT 鏂囦欢/鐩綍**锛氱偣鍑?娴忚鏂囦欢..."閫夋嫨鍗曚釜 `.evt`锛屾垨鐐瑰嚮"娴忚鐩綍..."閫夋嫨鍖呭惈澶氫釜 `.evt` 鐨勭洰褰曡繘琛屾壒閲忓鐞嗐€?2. **鎴彇闀垮害**锛氫笅鎷夐€夋嫨 1024/2048锛堥粯璁わ級/4096/8192 鐐癸紝鎴栧嬀閫?鑷畾涔?鎵嬪姩杈撳叆浠绘剰鐐规暟銆?3. **鍦伴渿浠噰鏍风巼**锛氶€夋嫨鍦伴渿浠疄闄呭伐浣滈噰鏍风巼锛岄粯璁?**50 Hz**锛堝彲閫?100/200 Hz锛夈€?4. **婊戝姩姝ラ暱**锛氶粯璁?鑷姩"锛堢獥鍙ｅぇ灏?4锛夛紝鍙€?128/256/512 鐐癸紝姝ラ暱瓒婂皬閫夊彇瓒婄簿缁嗕絾鑰楁椂瓒婇暱銆?5. **鐐瑰嚮"瑁佸壀骞跺鍑?TXT"**锛氬悗鍙版壒閲忚В鏋?鈫?涓夊垎閲忚仈鍚堟悳绱㈡渶浼樼獥鍙?鈫?瀵煎嚭 `{鍘熷悕}_{璧峰鏃堕棿}s.txt` 鍒?`data/` 鐩綍銆?6. 澶勭悊瀹屾垚鍚庣偣鍑?鎵撳紑鏁版嵁鐩綍"鏌ョ湅缁撴灉锛屽彲鐩存帴鐢ㄤ簬棰戣氨鍒嗘瀽銆?
### 棰戣氨鍒嗘瀽闈㈡澘

榛樿璁剧疆锛?
| 鍙傛暟 | 榛樿鍊?| 璇存槑 |
|------|--------|------|
| 鏁版嵁鐩綍 | `SeismicFrequencyAnalyzer/data` | 鍚?TXT/DAT 涓夊垎閲忔暟鎹?|
| 杈撳嚭鐩綍 | `SeismicFrequencyAnalyzer/two_method_spectrum_output` | 鍥句笌 CSV 杈撳嚭 |
| 閫夊嘲涓嬮檺 | **1 Hz** | 閬垮紑浣庨婕傜Щ |
| 閫夊嘲涓婇檺 | **8 Hz**锛?=涓嶈涓婇檺锛屾悳鍒?Nyquist锛?| 甯哥敤鑼冨洿 |
| 棰戣氨鍥炬樉绀轰笂闄?| **15 Hz**锛?=鏄剧ず鍒?Nyquist锛?| 甯哥敤鑼冨洿 |
| 瀹為檯澶勭悊鐐规暟 | 0锛堝叏閮級 | 0 琛ㄧず浣跨敤鍏ㄩ儴鏍锋湰 |

鐐瑰嚮"寮€濮嬪垎鏋?鍗冲彲鎵归噺澶勭悊 `data/` 鐩綍涓嬫墍鏈?TXT/DAT 鏂囦欢銆?
---

## 鍛戒护琛屼娇鐢?
### 棰戣氨鍒嗘瀽

```powershell
python SeismicFrequencyAnalyzer\dominant_frequency_two_methods.py `
  --data-dir SeismicFrequencyAnalyzer\data `
  --output-dir SeismicFrequencyAnalyzer\two_method_spectrum_output `
  --min-peak-frequency 1 `
  --max-peak-frequency 8 `
  --plot-max-frequency 15
```

### EVT 瑁佸壀锛圥ython 鑴氭湰璋冪敤锛?
```python
from pathlib import Path
from evt_reader import read_evt
from segment_selector import find_best_segment_three_component
from dat_exporter import export_three_component_dat

evt = read_evt("path/to/file.evt")
h = evt.header

# 涓夊垎閲忚仈鍚堟悳绱㈡渶浼樼獥鍙ｏ紙閲囨牱鐜囩敱鐢ㄦ埛鎸囧畾锛屽 50 Hz锛?INSTRUMENT_SR = 50.0
result = find_best_segment_three_component(
    evt.ew, evt.ns, evt.ud,
    window_size=2048,
    sample_rate_hz=INSTRUMENT_SR,
    step=512,  # 鑷畾涔夋闀匡紝None=鑷姩
)
bw = result.best_window

# 瀵煎嚭鍗曚釜 TXT 鏂囦欢锛堝吋瀹?load_traces()锛?start_time_s = bw.start_index / INSTRUMENT_SR
export_three_component_dat(
    ew_data=result.ew_data,
    ns_data=result.ns_data,
    ud_data=result.ud_data,
    output_path=f"output_{start_time_s:.1f}s.txt",
    sample_rate_hz=INSTRUMENT_SR,
    start_sample_index=bw.start_index,
    end_sample_index=bw.end_index,
    original_file="file.evt",
)
```

---

## 杈撳嚭鏂囦欢

### EVT 瑁佸壀 TXT 杈撳嚭

杈撳嚭鐩綍锛歚SeismicFrequencyAnalyzer/data/`锛堜笌棰戣氨鍒嗘瀽杈撳叆鐩綍涓€鑷达紝鍙棤缂濊鎺ワ級

鏂囦欢鍚嶏細`{鍘熷鏂囦欢鍚峿_{鎴彇璧峰鏃堕棿}s.txt`锛屼緥濡?`202606071041_568.4s.txt`

鏍煎紡鍏煎鐜版湁 TXT 瑙ｆ瀽閫昏緫锛坄load_traces()`锛夛紝鍏冧俊鎭紪鐮佸湪绗竴涓垎閲忓ご琛岋細

```
; samp: 50.0000; comp: 0; Data length:40.960000; Original: 202606071041.evt; RecordTime: 2026-06-07 10:41:00; StartIdx: 28420; EndIdx: 30468; StartTime: 568.400000s; EndTime: 609.360000s; window_score: 0.4292; ew_score: 0.4866; ns_score: 0.4140; ud_score: 0.3871
<UD 鏁版嵁鍊硷紝姣忚涓€涓?
; samp: 50.0000; comp: 1; Data length:40.960000
<NS 鏁版嵁鍊硷紝姣忚涓€涓?
; samp: 50.0000; comp: 2; Data length:40.960000
<EW 鏁版嵁鍊硷紝姣忚涓€涓?
```

| 瀛楁 | 鍚箟 |
|------|------|
| `samp` | 閲囨牱鐜囷紙Hz锛岀敤鎴疯缃級 |
| `comp` | 鍒嗛噺鍙凤紙0=UD, 1=NS, 2=EW锛?|
| `Data length` | 鏁版嵁鏃堕暱锛堢锛?|
| `Original` | 鍘熷 EVT 鏂囦欢鍚?|
| `RecordTime` | 鍘熷鏁版嵁璁板綍鏃堕棿 |
| `StartIdx / EndIdx` | 鎴彇璧峰/缁撴潫鐐瑰彿 |
| `StartTime / EndTime` | 鎴彇璧锋鏃堕棿锛堢锛?|
| `*_score` | 缁煎悎寰楀垎鍙婁笁鍒嗛噺鍚勮嚜寰楀垎 |

### 棰戣氨鍒嗘瀽杈撳嚭

姣忎釜杈撳叆鏂囦欢鐢熸垚涓€涓悓鍚嶅瓙鐩綍锛屽寘鍚細

- `*_01_raw_counts_time_history.png` 鈥?鍘熷璁℃暟鏃剁▼锛堜笁鍒嗛噺锛?- `*_02_corrected_acceleration_time_history_um_s2.png` 鈥?鏍℃鍔犻€熷害鏃剁▼
- `*_03_direct_spectrum.png` 鈥?鐩存帴娉曢璋?+ P1-P4 鍊欓€夊嘲
- `*_04_indirect_spectrum.png` 鈥?闂存帴娉曞姛鐜囪氨瀵嗗害 + P1-P4 鍊欓€夊嘲

姹囨€昏〃 `component_direct_indirect_results.csv`锛屽寘鍚細

- 鐩存帴娉?闂存帴娉曞崜瓒婇鐜囥€佸崜瓒婂懆鏈熴€佸嘲鍊?- P1-P4 鍊欓€夊嘲棰戠巼銆佸懆鏈熴€佸嘲鍊?- **鏃跺煙宄板€煎姞閫熷害锛埼糾/s虏锛?* 鈥斺€?姣忎釜鍒嗛噺鏍℃鍚庡姞閫熷害鐨勬椂鍩熷嘲鍊?
---

## 绠楁硶鍘熺悊

### 绾挎€у幓婕傜Щ锛坮emove_linear_drift锛?
閲囩敤**鏈€灏忎簩涔樼嚎鎬ф嫙鍚?*锛氬绐楀彛鍐呮暟鎹嫙鍚?`y = a路x + b`锛岃绠楁枩鐜?`a` 鍚庡噺鍘荤嚎鎬ц秼鍔?`a路x`銆傚墠鎻愭槸鏁版嵁鏈韩鏄嚎鎬х殑锛堝彧鏈夊潎鍖€婕傜Щ锛屾病鏈夊集鏇诧級锛岃繖姝ｆ槸闇€瑕佸厛瑁佸壀鍑虹嚎鎬ф鐨勫師鍥犮€?
### 鏈€浼樻暟鎹绛涢€夛紙鍥涚淮璇勫垎锛?
瀵规瘡涓粦鍔ㄧ獥鍙ｄ綅缃紝涓夊垎閲忓垎鍒瘎鍒嗗悗鍙栧钩鍧囷細

| 缁村害 | 鏉冮噸 | 璁＄畻 |
|------|------|------|
| 骞崇ǔ鎬?| 0.50 | 瀛愮獥鍙ｅ潎鍊?鏍囧噯宸彉寮傜郴鏁?鈫?`exp(-cv脳k)` |
| 寮洸搴?| 0.25 | `(RMS_linear - RMS_quad) / RMS_linear`锛屼簩娆℃樉钁椾紭浜庣嚎鎬у垯鎯╃綒 |
| 灏栧嘲 | 0.10 | MAD 椴佹缁熻锛岃秴 5脳robust_std 鐨勭偣鍗犳瘮 |
| 姝绘暟鎹?| 0.15 | 鍏ㄩ浂/甯搁噺娈垫垨澶ч噺鎺ヨ繎闆跺€?|

鎬诲垎 = `0.50脳骞崇ǔ鎬?- 0.25脳寮洸 - 0.10脳灏栧嘲 - 0.15脳姝诲尯`锛屽彇鏈€楂樺垎绐楀彛銆?
### 鐩存帴娉?vs 闂存帴娉?
- **鐩存帴娉?*锛氭椂鍩熶俊鍙?鈫?FFT 鈫?骞呭€艰氨 鈫?骞虫柟 鈫?鍔熺巼璋?- **闂存帴娉?*锛氭椂鍩熶俊鍙?鈫?鑷浉鍏冲嚱鏁?鈫?FFT 鈫?鍔熺巼璋?鈫?闄や互棰戠巼鍒嗚鲸鐜?鈫?鍔熺巼璋卞瘑搴?
---

## 鎵撳寘

浣跨敤 PyInstaller 鎵撳寘涓?Windows 鐙珛鍙墽琛岀▼搴忥細

```powershell
python -m PyInstaller SeismicFrequencyAnalyzer.spec --noconfirm
```

鐢熸垚鏂囦欢浣嶄簬 `dist/SeismicFrequencyAnalyzer.exe`锛屽彂甯冩椂涓婁紶鍒?[GitHub Releases](https://github.com/WangHongwei2004/SeismicFrequencyAnalyzer/releases)銆?
---

## 璁稿彲鍗忚

鏈」鐩娇鐢?*鑷畾涔夐潪鍟嗕笟绉戠爺鏁欏璁稿彲鍗忚**锛屽厑璁镐釜浜鸿嚜鐢ㄣ€佹暀瀛︺€佺鐮斻€佽绋嬪疄楠屻€侀潪鍟嗕笟璇勪及鍜岄潪鍟嗕笟浜屾寮€鍙戙€?
鏈粡浣滆€呬功闈㈡巿鏉冿紝涓嶅厑璁稿皢鏈蒋浠舵垨鍏惰鐢熺増鏈敤浜庡晢涓氫骇鍝併€佸晢涓氭湇鍔°€佷粯璐瑰挩璇€佷粯璐瑰煿璁€佸晢涓氭暟鎹鐞嗐€佸晢涓氬伐浣滄祦闆嗘垚銆佽浆鍞€佺璧併€佸啀璁稿彲鎴栧叾浠栦互鍟嗕笟鍒╃泭涓轰富瑕佺洰鐨勭殑鍦烘櫙銆?
濡傞渶鍟嗕笟鎺堟潈锛岃閫氳繃椤圭洰鍦板潃鑱旂郴锛?https://github.com/WangHongwei2004/SeismicFrequencyAnalyzer>銆?
鎻愪氦鍒?GitHub 鏃讹紝寤鸿鎻愪氦婧愮爜銆丷EADME銆乺equirements銆丩ICENSE 鍜屽繀瑕佸崰浣嶆枃浠讹紱`build/`銆乣dist/`銆乣__pycache__/`銆佸師濮嬫暟鎹€佸垎鏋愯緭鍑哄浘鍜?CSV 灞炰簬鏈湴鏂囦欢鎴栫敓鎴愮墿锛岄粯璁ら€氳繃 `.gitignore` 鎺掗櫎銆?
