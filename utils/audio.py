import time
import os
import re
import requests
import configparser
from PyQt5 import QtCore
from azure.cognitiveservices.speech import languageconfig
from pydub import AudioSegment
import azure.cognitiveservices.speech as speechsdk


class STT(QtCore.QObject):
    procMain = QtCore.pyqtSignal(int, float)

    def STT_from_file(self, filePath):
        cf = configparser.ConfigParser()
        cf.read("config.ini") 
        key = cf.get("STT", "key")

        # 先檢查Key是否有效
        url = "https://eastus.api.cognitive.microsoft.com/sts/v1.0/issueToken"
        headers = {'Ocp-Apim-Subscription-Key': key, 'Content-type': 'application/x-www-form-urlencoded', 'Content-Length': '0'}
        r = requests.post(url, headers=headers)
        if r.status_code != 200:
            return False

        speech_key, service_region, language = key, "eastus", "zh-TW"
        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region, speech_recognition_language=language)
        speech_config.set_profanity(speechsdk.ProfanityOption.Raw)
        
        audio_config = speechsdk.audio.AudioConfig(filename=filePath)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        all_results = []
        def handle_final_result(evt):
            remove_punct = re.split('[，。、？！]+', evt.result.text)
            print(remove_punct)
            all_results.extend(remove_punct[:-1])

        def handle_start_process(evt):
            self.procMain.emit(7, 0)

        done = False #檢查stt是否完成了

        def stop_cb(evt):
            print('CLOSING on {}'.format(evt))
            speech_recognizer.stop_continuous_recognition()
            nonlocal done
            done = True
        
        #Appends the recognized text to the all_results variable. 
        speech_recognizer.recognized.connect(handle_final_result) 

        # speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))
        speech_recognizer.session_started.connect(handle_start_process)
        speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
        speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))

        speech_recognizer.session_stopped.connect(stop_cb)
        speech_recognizer.canceled.connect(stop_cb)

        # 開始轉錄
        speech_recognizer.start_continuous_recognition() 

        #讓程式等待轉錄，直到收到訊號
        while not done:
            time.sleep(.5)
        
        
        return all_results #List

    def tranfer(self, filePath):
        #取Path和副檔名
        filename, file_extension = os.path.splitext(filePath)

        #轉檔
        if(file_extension == '.wav'): #wav不用轉檔
            return filePath
        
        elif(file_extension == '.mp3' or file_extension == '.m4a'):
            if(file_extension == '.mp3'):
                song = AudioSegment.from_mp3(filePath)
            elif(file_extension == '.m4a'):
                song = AudioSegment.from_file(filePath)
            
            newfilePath = filename + '.wav'
            song.export(newfilePath, format='wav')
            
            return newfilePath

    # button呼叫這個function
    def importAudio(self, filePath): 
        outputText = [] 
        
        if filePath and os.path.exists(filePath):
            newPath = self.tranfer(filePath)
            outputText = self.STT_from_file(newPath)
        
        # 這個看你要存在哪
        return outputText

    def getAudioLength(self, filePath):
        song = AudioSegment.from_file(filePath)
        return song.duration_seconds
