import time
import os
from PyQt5 import QtWidgets 
from pydub import AudioSegment
import azure.cognitiveservices.speech as speechsdk


def STT_from_file(filePath):
    speech_key, service_region = "a6db1d8286b84a1489c92a88184f57a6", "eastus"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_recognition_language="zh-TW"
    audio_config = speechsdk.audio.AudioConfig(filename=filePath)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    all_results = []

    def handle_final_result(evt):
        all_results.append(evt.result.text) 

    done = False #檢查stt是否完成了

    def stop_cb(evt):
        print('CLOSING on {}'.format(evt))
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True
    
    #Appends the recognized text to the all_results variable. 
    speech_recognizer.recognized.connect(handle_final_result) 

    # speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))
    # speech_recognizer.recognized.connect(lambda evt: print('RECOGNIZED: {}'.format(evt)))
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))

    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.5)

    
    return all_results #List

def tranfer(filePath):
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
def importAudio(self): 
    outputText = [] 
    filePath, _ = QtWidgets.QFileDialog.getOpenFileName(None,
                                        "開啟音訊",
                                        "",
                                        "Audio Files(*.mp3 *.m4a *.wav)")
    if filePath and os.path.exists(filePath):
        newPath = tranfer(filePath)
        outputText = STT_from_file(newPath)
    
    # 這個看你要存在哪
    return outputText