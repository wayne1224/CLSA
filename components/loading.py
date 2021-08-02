from PyQt5 import QtCore, QtGui, QtWidgets

class LoadingScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        self.setStyleSheet("background-color:#c7daed")
        #self.setFixedSize(200,200)
        self.label1 = QtWidgets.QLabel('<p style="font-size:10pt; color: black; font-weight: bold;">彙整中...</p>')
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.CustomizeWindowHint)
        self.label = QtWidgets.QLabel(self)
        self.movie = QtGui.QMovie('./image/loading.gif')
        self.label.setMovie(self.movie)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        layout.addWidget(self.label1)
        layout.addWidget(self.label)

        radius = 40.0
        path = QtGui.QPainterPath()
        self.resize(220,250)
        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)
        #self.move(QtGui.QCursor.pos())
    
    def startAnimation(self, info):
        self.label1.setText('<p style="font-size:10pt; color: black; font-weight: bold;">'+ info +'</p>')
        self.show()
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()



class LoadingBar(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.CustomizeWindowHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setStyleSheet(open("./QSS/loading.qss", "r").read())
        
        #Qlabel
        self.label = QtWidgets.QLabel()
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.label)

        #Qbar
        self.pbar = QtWidgets.QProgressBar()
        self.pbar.setMinimum(0)
        self.pbar.setMaximum(100)
        self.pbar.setFont(QtGui.QFont('Arial', 15))
        layout.addWidget(self.pbar)

        #SpacerItem
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        layout.addItem(spacerItem)

        #QpXimap
        self.image = QtGui.QPixmap('./image/azure.png')
        self.label1 = QtWidgets.QLabel()
        self.label1.setPixmap(self.image)
        self.label1.setMaximumSize(QtCore.QSize(130, 40))
        self.label1.setScaledContents(True)
        layout.addWidget(self.label1, alignment=QtCore.Qt.AlignCenter)

        

        #Timer
        self.time = 0 #錄音檔長度
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.handleTimer)
        self.step = 0

        radius = 30.0
        path = QtGui.QPainterPath()
        self.resize(300,200)
        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)
        
    def handleTimer(self):
        self.step += 1
        self.pbar.setValue(self.step)

    def wait(self, time):
        print('waiting..')
        self.label.setText('<p style="font-size:10pt; color: black; font-weight: bold;">系統啟動中...</p>')
        self.show()
        self.time = time

    def start(self):
        self.label.setText('<p style="font-size:10pt; color: black; font-weight: bold;">轉錄中...</p>')
        self.step = 0
        self.timer.start(self.time * 10) #每1秒

    def stop(self):
        self.pbar.setValue(100)
        self.timer.stop()
        self.close()
        
       
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = LoadingBar()
    window.show()
    app.exec_()