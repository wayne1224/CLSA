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

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = LoadingScreen()
    window.show()
    app.exec_()