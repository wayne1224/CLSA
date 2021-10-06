import sys
import os
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from MainTabWidget import MainTabWidget
from components.loading import LoadingScreen, LoadingBar, DownloadScreen
from utils.worker import Worker_DB, Worker
import database.DatabaseApi


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(1400, 700)
        self.setWindowTitle("CLSA")
        self.mainTab = MainTabWidget()
        self.mainTab.tabBar().setDocumentMode(True)
        self.mainTab.tabBar().setExpanding(True)
        self.setCentralWidget(self.mainTab)

        #模糊特效
        #self.blur_effect = QtWidgets.QGraphicsBlurEffect()
        #self.setGraphicsEffect(self.blur_effect)

        #設定tab的css
        # self.setStyleSheet(open("C:/Users/HAO/Desktop/Code/Python/CLSA/QSS/MainWindow.qss", "r").read())
        self.setStyleSheet(open("QSS/MainWindow.qss", "r").read())

        #signal
        self.mainTab.tab0.procMain.connect(self.getAction)
        self.mainTab.tab2.procMain.connect(self.getAction)
        self.mainTab.tab3.procMain.connect(self.getAction)
        self.mainTab.tab2.audio.procMain.connect(self.getAction)

        #Loading Screen
        self.load = LoadingScreen()
        self.load.setObjectName("loadScreen") 
        self.load2 = LoadingBar()

        # 資料庫連接失敗 直接關閉程式
        self.thread_DB = QtCore.QThread()
        self.worker_DB = Worker_DB(database.DatabaseApi.connectDB)
        self.worker_DB.moveToThread(self.thread_DB)
        self.thread_DB.started.connect(self.worker_DB.run)
        self.worker_DB.finished.connect(self.thread_DB.quit)
        self.worker_DB.finished.connect(self.worker_DB.deleteLater)
        self.thread_DB.finished.connect(self.thread_DB.deleteLater)
        self.thread_DB.finished.connect(self.mainTab.tab4.tab1.createBarCharts) #讀取資料並產生圖表
        self.thread_DB.finished.connect(self.mainTab.tab4.tab2.getNorms)  #讀取NORM
        self.thread_DB.start() #開始跑Thread
        
        #讀取CKIP transformers
        self.window = DownloadScreen()
        if os.path.exists(self.get_model_path()) == False:
            self.window.show()
        
        #讀取 Model Thread
        self.thread = QtCore.QThread()
        self.worker = Worker(self.load_model)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

    @QtCore.pyqtSlot(int, float)
    def getAction(self, key, time):
        if key == 1:
            self.mainTab.setCurrentIndex(1)

        #key(2~4) Tab3 使用
        elif key == 2:
            self.load.startAnimation('彙整中...')
        elif key == 3:
            self.load.stopAnimation()
            self.mainTab.setCurrentIndex(3)
            QtWidgets.QMessageBox.information(self, '通知',"<p style='font-size:12pt;'>資料彙整並儲存成功</p>", QtWidgets.QMessageBox.Ok)
        elif key == 4:
            self.load.stopAnimation()
            QtWidgets.QMessageBox.warning(self, '警告',"<p style='font-size:12pt;'>資料不足無法彙整</p>", QtWidgets.QMessageBox.Ok)
        
        #key(5~7) Tab2 使用
        elif key == 5:
            self.load2.wait(time)   
        elif key == 6:
            self.load2.stop()
            QtWidgets.QMessageBox.information(self, '通知',"<p style='font-size:12pt;'>轉錄成功</p>", QtWidgets.QMessageBox.Ok)
        elif key == 7:
            self.load2.start()
        

    def closeEvent(self, event):
        checkTab1 = self.mainTab.tab1.isEdit()
        checkTab2 = self.mainTab.tab2.isEdit()
        if checkTab2 == "NoAdultID":
            event.ignore()
        else:
            if checkTab1 or checkTab2:
                warnText = '<p style="font-size:12pt; color: #3778bf;">要儲存對下列頁面的變更嗎?</p>\n'
                if checkTab1:
                    warnText += '收錄表\n'
                if checkTab2:
                    warnText += '轉錄表'

                close = QtWidgets.QMessageBox.question(self,
                                "CLSA",
                                warnText,
                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
                if close == QtWidgets.QMessageBox.Yes :
                    if self.mainTab.tab1.currentDoc_id:
                        if (self.mainTab.tab1.updateRecord()):
                            event.accept()
                    else :
                        if (self.mainTab.tab1.insertRecord()):
                            event.accept()
                elif close == QtWidgets.QMessageBox.No:
                    event.accept()
                else:
                    event.ignore()

    def get_model_path(self):
        home_dir = os.path.expanduser("~")
        cache_dir = os.path.join(home_dir, ".cache")
        model_path = os.path.join(cache_dir, "huggingface/transformers")
        return model_path

    def load_model(self):
        import time
        time.sleep(2)
        
        #Download Tab3 ws_driver, pos_driver
        self.mainTab.tab3.init_transformers()

        #關閉loading視窗
        self.window.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    
    
if __name__ == '__main__':
    main()