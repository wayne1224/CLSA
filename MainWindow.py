import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Tab0 import SearchTab
from Tab2 import Tab2
from Tab1 import Myform
from Tab3 import AnalysisTab
class MainTabWidget(QtWidgets.QTabWidget):
    def __init__(self,parent=None):
        super(MainTabWidget, self).__init__(parent)
        self.resize(1393, 870)
        self.setWindowTitle("CLSA")

        #創建4個tab
        self.tab0 = SearchTab()
        self.tab1 = Myform()
        self.tab2 = Tab2()
        self.tab3 = AnalysisTab()

        #self.tab1.procStart.connect(self.tab2.onprocStart)

        #將tab加入MainWindow中
        self.addTab(self.tab0, "查詢頁面")
        self.addTab(self.tab1, "收錄表")
        self.addTab(self.tab2, "轉錄表")
        self.addTab(self.tab3, "彙整表")

        #設定tab的css
        self.setStyleSheet( "QTabBar::tab { height: 40px; width: 250px; }")

        #self.tab1.procStart.connect(self.tab2.setCaseID)
        #self.tab2.procUtterNum.connect(self.tab3.)
        self.tab2.procChildUtter.connect(self.tab3.getChildUtterance)
        self.tab2.procKey.connect(self.tab3.getKey)

    def closeEvent(self, event):
        close = QtWidgets.QMessageBox.question(self,
                        "CLSA",
                        "要儲存變更嗎?",
                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
        if close == QtWidgets.QMessageBox.Yes and self.tab1.save():
            event.accept()
        elif close == QtWidgets.QMessageBox.No:
            event.accept()
        else:
            event.ignore()
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    demo = MainTabWidget()
    demo.show()
    sys.exit(app.exec_())
