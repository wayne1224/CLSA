import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainTabWidget import MainTabWidget
from components.loading import LoadingScreen, LoadingBar
import database.DatabaseApi
import DistilTag


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(1393, 870)
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
        self.thread = QtCore.QThread()
        self.worker = Worker(database.DatabaseApi.connectDB)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        #讀取資料並產生圖表
        self.thread.finished.connect(self.mainTab.tab4.tab1.lineChart)

        #讀取NORM
        self.thread.finished.connect(self.mainTab.tab4.tab2.getNorms)
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
            QtWidgets.QMessageBox.information(self, '通知','資料彙整並儲存成功', QtWidgets.QMessageBox.Ok)
        elif key == 4:
            self.load.stopAnimation()
            QtWidgets.QMessageBox.warning(self, '警告','資料不足無法彙整', QtWidgets.QMessageBox.Ok)
        
        #key(5~7) Tab2 使用
        elif key == 5:
            self.load2.wait(time)   
        elif key == 6:
            self.load2.stop()
            QtWidgets.QMessageBox.information(self, '通知','轉錄成功', QtWidgets.QMessageBox.Ok)
        elif key == 7:
            self.load2.start()
        

    def closeEvent(self, event):
        checkTab1 = self.mainTab.tab1.saveExamination()
        checkTab2 = self.mainTab.tab2.isEdit()
        if checkTab2 == "NoAdultID":
            event.ignore()
        else:
            if checkTab1 or checkTab2:
                warnText = '<p style="font-size:13pt; color: #3778bf;">要儲存對下列頁面的變更嗎?</p>\n'
                if checkTab1:
                    warnText += '收錄表\n'
                if checkTab2:
                    warnText += '轉錄表'

                close = QtWidgets.QMessageBox.warning(self,
                                "CLSA",
                                warnText,
                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
                if close == QtWidgets.QMessageBox.Yes and self.mainTab.tab1.save():
                    event.accept()
                elif close == QtWidgets.QMessageBox.No:
                    event.accept()
                else:
                    event.ignore()

class Worker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(int)

    def __init__(self, fn):
        super(Worker, self).__init__()
        self.func = fn

    def run(self):
        if not self.func():
            print("Database Failed")
            sys.quit()  
        self.finished.emit()


if __name__ == '__main__':
    try:
        DistilTag.download()
    except:
        print('模型下載失敗')
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()