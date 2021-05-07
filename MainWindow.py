import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainTabWidget import MainTabWidget
import database.DBapi

class LoadingScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        self.setStyleSheet("background-color: white;")
        #self.setFixedSize(200,200)
        self.label1 = QtWidgets.QLabel('<p style="font-size:10pt; color: black; font-weight: bold;">彙整中...</p>')
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.CustomizeWindowHint)
        self.label = QtWidgets.QLabel(self)
        self.movie = QtGui.QMovie('sss.gif')
        self.label.setMovie(self.movie)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        #timer = QTimer(self)
        layout.addWidget(self.label1)
        layout.addWidget(self.label)
        
        #timer.singleShot(3000,self.stopAnimation)

    def startAnimation(self):
        self.show()
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(1393, 870)
        self.setWindowTitle("CLSA")
        self.mainTab = MainTabWidget()
        self.setCentralWidget(self.mainTab)

        #模糊特效
        self.blur_effect = QtWidgets.QGraphicsBlurEffect()
        #self.setGraphicsEffect(self.blur_effect)

        #signal
        self.mainTab.tab0.procMain.connect(self.getAction)
        self.mainTab.tab2.procMain.connect(self.getAction)
        self.mainTab.tab3.procMain.connect(self.getAction)

        self.load = LoadingScreen()

        if database.DBapi.connectDB():
            print("t")
            # 資料庫連接成功
        else:
            print("f")
            # 資料庫連接失敗



    @QtCore.pyqtSlot(int)
    def getAction(self, key):
        if key == 1:
            self.mainTab.setCurrentIndex(1)
        elif key == 2:
            pass
        elif key == 3:
            #self.load.stopAnimation()
            informBox = QtWidgets.QMessageBox.information(self, '通知','資料彙整並儲存成功', QtWidgets.QMessageBox.Ok)
    
    def showProgress(self):
        pass
            

    def closeEvent(self, event):
        if self.mainTab.tab1.saveExamination() or self.mainTab.tab2.isEdit():
            warnText = '<p style="font-size:13pt; color: #3778bf;">要儲存對下列頁面的變更嗎?</p>\n'
            if self.mainTab.tab1.saveExamination():
                warnText += '收錄表\n'
            if self.mainTab.tab2.isEdit():
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

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()