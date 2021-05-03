import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainTabWidget import MainTabWidget
# Subclass QMainWindow to customise your application's main window
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

        # self.label = QtWidgets.QLabel() 
        # self.label.setObjectName("loading")
        # self.label.show()
        # self.movie = QtGui.QMovie('loading.gif')
        # self.label.setMovie(self.movie) 
        # self.startAnimation() 

    def startAnimation(self): 
        self.movie.start() 

    @QtCore.pyqtSlot(int)
    def getAction(self, key):
        if key == 1:
            self.mainTab.setCurrentIndex(1)
        elif key == 2:
            pass
            #self.setGraphicsEffect(self.blur_effect)
        elif key == 3:
            pass
            #self.setGraphicsEffect(0)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()