import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from Mytable import Mytable
from Tab2 import Tab2
from Tab1 import Myform
class TabDemo(QtWidgets.QTabWidget):
    def __init__(self,parent=None):
        super(TabDemo, self).__init__(parent)
        self.resize(1393, 870)
    
        #創建3個tab
        self.tab1=Myform()
        self.tab2=Tab2()
        self.tab3=QtWidgets.QWidget()

        #將tab加入MainWindow中
        self.addTab(self.tab1, "CLSA 收錄表")
        self.addTab(self.tab2, "CLSA 轉錄表")
        self.addTab(self.tab3, "Tab 3")

        #設定tab的css
        self.setStyleSheet( "QTabBar::tab { height: 40px; width: 250px; }")

if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    demo=TabDemo()
    demo.show()
    sys.exit(app.exec_())
