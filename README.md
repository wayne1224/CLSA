# CLSA (華語兒童語言樣本分析系統)

## Description
本系統是根據《華語兒童語言樣本分析》一書中的內容進行開發，旨在提供語言治療師一個系統化方式來分析兒童語料樣本，以用於評估兒童在自然情境下的表達性語言能力<br/><br/>
設計上與教學醫院的臨床語言治療師進行多次會談, 針對臨床人員著重的向度進行設計, 包含 [平均語句長度](https://st-box.blogspot.com/2017/07/mean-length-of-utterances-mlu.html) 和 [詞彙多樣性](https://www.researchgate.net/profile/Brian-Richards-8/publication/283149921_Measuring_Vocabulary_Diversity_Using_Dedicated_Software/links/569ca93808ae6169e563955e/Measuring-Vocabulary-Diversity-Using-Dedicated-Software.pdf?origin=publication_detail) 的計算，且結合[微軟語言轉文字 SDK](https://github.com/Azure-Samples/cognitive-services-speech-sdk/blob/master/samples/python/console/speech_sample.py)，大幅縮短聽打時間，並使用 [MongoDB](https://pymongo.readthedocs.io/en/stable/) 幫助治療師進行資料管理

### 系統架構
<img src="https://user-images.githubusercontent.com/58461709/159930055-df6a3388-32fa-4fec-a4a3-bcc71db59438.png" width="500">


## Setup

### Requirements
* Python 3.7+

### Installation
1. Clone repository 
2. 安裝 dependencies
```
$ cd <github_repo>
$ pip install -r requirements.txt
```
3. 安裝 [MongoDB Community Server](https://www.mongodb.com/try/download/community?tck=docs_server) - Windows <br/>
4. 安裝 FFmpeg
   (1) 下載 [libav]()
