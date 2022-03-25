# CLSA (華語兒童語言樣本分析系統)

## Description
本系統是根據《華語兒童語言樣本分析》一書中的內容進行開發，旨在提供語言治療師一個系統化方式來分析兒童語料樣本，以用於評估兒童在自然情境下的表達性語言能力<br/><br/>
設計上與教學醫院的臨床語言治療師進行多次會談, 針對臨床人員著重的向度進行設計, 包含 [平均語句長度](https://st-box.blogspot.com/2017/07/mean-length-of-utterances-mlu.html) 和 [詞彙多樣性](https://www.researchgate.net/profile/Brian-Richards-8/publication/283149921_Measuring_Vocabulary_Diversity_Using_Dedicated_Software/links/569ca93808ae6169e563955e/Measuring-Vocabulary-Diversity-Using-Dedicated-Software.pdf?origin=publication_detail) 的計算，且結合[微軟語言轉文字 SDK](https://github.com/Azure-Samples/cognitive-services-speech-sdk/blob/master/samples/python/console/speech_sample.py)，大幅縮短聽打時間，並使用 [MongoDB](https://pymongo.readthedocs.io/en/stable/) 幫助治療師進行資料管理

### 系統架構
<img src="https://user-images.githubusercontent.com/58461709/159930055-df6a3388-32fa-4fec-a4a3-bcc71db59438.png" width="500">

### Branch 差異
**main_ver3:** 開發時所使用，透過 MongoDB URI 讀取線上資料庫，以便開發時同步資料庫的內容 <br/>
**release:** 醫院使用版本，透過本機 MongoDB server 讀取本機資料庫

## Setup

### Requirements

* Windows
* Python 3.7+

### Installation
1. Clone repository 
2. 安裝 dependencies
```
cd <github_repo>
pip install -r requirements.txt
```
3. 安裝 [MongoDB Community Server](https://www.mongodb.com/try/download/community?tck=docs_server) - Windows <br/>
4. 安裝 FFmpeg 
   1. 下載 [libav](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z) & 解壓縮
   2. 放在 C 槽 (C:\ffmpeg\bin)
   3. 開啟 **Windows 設定** > **進階系統設定** > **環境變數**
   4. 開啟 **變數：Path** > 點選 **新增** > 輸入 **C:\ffmpeg\bin** > 確定
   5. 開啟 **cmd** 輸入 set Path=C:
   6. 安裝 PyAudio
   
   ```
   pip install pyAudio
   ```

### Usage
```
cd <github_repo>
python MainWindow.py
```

### Package
1. 建立虛擬環境
```
cd <Desktop>
virtualenv env_win
```
2. activate 虛擬環境
```
cd env_win\Scripts
activate
```
3. 安裝 dependencies
```
cd <github_repo>
pip install -r requirements.txt
```
4. 執行 PyInstaller
```
pyinstaller  MainWindow.spec
```
生成的 EXE 和相關檔案會存放在 dist 資料夾裡 <br/>
可以刪除 build 資料夾

### Directory Layout
```
├─components              # 可重複使用之元件
|  ├─ Mytable.py          # 轉錄表中的表格
|  ├─ loading.py          # 讀取視窗
|  ├─ messageBox.py       # 顯示比對資訊的通知視窗
│  ├─ norm.py             # 常模設定頁面
|  ├─ setting.py          # 其他設定頁面
│  └─ statChart.py        # 圖表生成
├─database
│  └─ DatabaseApi.py      # PyMongo APIs
├─QSS                     # PyQT StyleSheets
├─utils
│  ├─ audio.py            # Microsoft STT SDK
│  └─ worker.py           # PyQT QThread Implementation
├─ MainWindow.py          # 主程式
├─ Tab0.py                # 查詢頁面
├─ Tab1.py                # 收錄表
├─ Tab2.py                # 轉錄表
├─ Tab3.py                # 彙整表
├─ Tab4.py                # 圖表頁
├─ Tab5.py                # 設定頁面
├─ MainWindow.spec        # 紀錄 pyinstaller 打包此系統的指令
└─ mongodb_dir.bat        # 建立 MongoDB 預設 data directory
```
