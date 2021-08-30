import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from Tab0 import SearchTab
from Tab2 import Tab2
from Tab1 import Myform
from Tab3 import AnalysisTab
from Tab4 import Tab4

class MainTabWidget(QtWidgets.QTabWidget):
    def __init__(self,parent=None):
        super(MainTabWidget, self).__init__(parent)
        self.setWindowTitle("CLSA")

        #創建4個tab
        self.tab0 = SearchTab()
        self.tab1 = Myform()
        self.tab2 = Tab2()
        self.tab3 = AnalysisTab()
        self.tab4 = Tab4()

        # #tab4裡的tab自動填滿
        # self.tab4.tabBar().setDocumentMode(True)
        # self.tab4.tabBar().setExpanding(True)

        #模糊特效
        self.blur_effect = QtWidgets.QGraphicsBlurEffect()

        #將tab加入MainWindow中
        self.addTab(self.tab0, "查詢頁面")
        self.addTab(self.tab1, "收錄表")
        self.addTab(self.tab2, "轉錄表")
        self.addTab(self.tab3, "彙整表")
        self.addTab(self.tab4, "圖表")

        #設定tab的css
        self.setStyleSheet(open("QSS/MainTabWidget.qss", "r").read())

        #設定Tab Signal
        self.currentChanged.connect(self.checkTab2Case)
        self.currentChanged.connect(self.checkTab2Changed)
        self.currentChanged.connect(self.leaveTab1)
        self.tab1.procStart.connect(self.tab2.setCaseRecord)
        self.tab2.procUtterNum.connect(self.tab1.getUtterNum)
        self.tab2.procChildUtter.connect(self.tab3.getChildUtterance)
        #self.tab2.procKey.connect(self.tab1.getCaseIDAndDate)
        self.tab2.procKey.connect(self.tab3.getDoc)
        self.tab2.procEdit.connect(self.tab3.setEdit)

        #搜尋頁面傳document給其他Tab
        self.tab0.procDoc.connect(self.tab1.getDoc)
        self.tab0.procDoc.connect(self.tab2.getDoc)
        self.tab0.procDoc.connect(self.tab3.getDoc)
        # self.tab0.procDoc.connect(self.tab4.create_piechart)
        # self.tab0.procDoc.connect(self.tab4.create_linechart)
        #self.tab0.procDoc.connect(self.tab4.create_linebarchart)

        #搜尋頁面按下搜尋時，其他頁面清空
        #self.tab0.procClear.connect(self.tab1.clearContent)
        self.tab1.procClear.connect(partial(self.tab2.clearTab, True))
        self.tab1.procClear.connect(self.tab3.clearContent)
        self.tab2.procClear.connect(self.tab3.clearContent)

    def leaveTab1(self) :
        if (self.currentIndex() != 1) :
            self.tab1.clearRedFrame()

    def checkTab2Case(self):
        if self.currentIndex() == 2 and not self.tab2.caseID:
            informBox = QtWidgets.QMessageBox.warning(self, '警告','請先建立新個案或匯入個案', QtWidgets.QMessageBox.Ok)

    def checkTab2Changed(self):
        if ((self.currentIndex() == 3 and self.tab2.isEdit()) or (self.currentIndex() == 3 and self.tab3.getEdit())):
            self.tab3.clearContent()
            informBox = QtWidgets.QMessageBox.warning(self, '警告','轉錄表已變動 請重新產生彙整表', QtWidgets.QMessageBox.Ok)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    demo = MainTabWidget()
    demo.show()
    sys.exit(app.exec_())
