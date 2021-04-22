import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from Tab2 import Tab2
from Tab1 import Myform
from Tab3 import Analysis
class MainTabWidget(QtWidgets.QTabWidget):
    def __init__(self,parent=None):
        super(MainTabWidget, self).__init__(parent)
        self.resize(1393, 870)
        self.setWindowTitle("CLSA")

        #創建3個tab
        self.tab1=Myform()
        self.tab2=Tab2()
        self.tab3=Analysis()

        #self.tab1.procStart.connect(self.tab2.onprocStart)

        #將tab加入MainWindow中
        self.addTab(self.tab1, "收錄表")
        self.addTab(self.tab2, "轉錄表")
        self.addTab(self.tab3, "彙整表")

        #設定tab的css
        self.setStyleSheet( "QTabBar::tab { height: 40px; width: 250px; }")

        self.tab1.procStart.connect(self.tab2.setCaseID)
        self.tab2.procStart.connect(self.tab3.getChildUtterance)
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    demo = MainTabWidget()
    demo.show()
    sys.exit(app.exec_())
