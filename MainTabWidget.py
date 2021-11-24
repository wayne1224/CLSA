import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from Tab0 import SearchTab
from Tab2 import Tab2
from Tab1 import Myform
from Tab3 import AnalysisTab
from Tab4 import GraphTab
from Tab5 import GeneralTab

class MainTabWidget(QtWidgets.QTabWidget):
    def __init__(self,parent=None):
        super(MainTabWidget, self).__init__(parent)
        self.setWindowTitle("CLSA")

        #創建4個tab
        self.tab0 = SearchTab()
        self.tab1 = Myform()
        self.tab2 = Tab2()
        self.tab3 = AnalysisTab()
        self.tab4 = GraphTab()
        self.tab5 = GeneralTab()


        #模糊特效
        self.blur_effect = QtWidgets.QGraphicsBlurEffect()

        #將tab加入MainWindow中
        self.addTab(self.tab0, "查詢頁面")
        self.addTab(self.tab1, "收錄表")
        self.addTab(self.tab2, "轉錄表")
        self.addTab(self.tab3, "彙整表")
        self.addTab(self.tab4, "圖表")
        self.addTab(self.tab5, "設定頁面")

        #設定tab的css
        self.setStyleSheet(open("QSS/MainTabWidget.qss", "r").read())

        #切換Tab時，進行檢查
        self.currentChanged.connect(self.checkTab2Case) #檢查是否已有紀錄匯入
        self.currentChanged.connect(self.checkTab2Changed) #檢查TAB2是否有更動
        self.currentChanged.connect(self.leaveTab1) 

        self.tab1.procStart.connect(self.tab2.setCaseRecord)
        self.tab2.procUtterNum.connect(self.tab1.getUtterNum)
        self.tab2.procChildUtter.connect(self.tab3.getChildUtterance)
        self.tab2.procKey.connect(self.tab3.getDoc)
        self.tab2.procEdit.connect(self.tab3.setEdit)

        #搜尋頁面傳document給其他Tab
        self.tab0.procDoc.connect(self.tab1.getDoc)
        self.tab0.procDoc.connect(self.tab2.getDoc)
        self.tab0.procDoc.connect(self.tab3.getDoc)

        #搜尋頁面按下搜尋時，其他頁面清空
       # self.tab0.procClear.connect(self.tab1.clearContent)
        self.tab1.procClear.connect(partial(self.tab2.clearTab, True))
        self.tab1.procClear.connect(partial(self.tab2._setWidgetEnabled, False))
        self.tab1.procClear.connect(self.tab3.clearContent)
        self.tab2.procClear.connect(self.tab3.clearContent)

        #Tab1新增一筆紀錄時，Tab1傳document ID給Tab0 : 避免刪到正在改的紀錄
        self.tab1.procID.connect(self.tab0.getDocID)

    def leaveTab1(self) : #用途???
        if (self.currentIndex() != 1):
            self.tab1.clearRedFrame()

    def checkTab2Case(self):
        if self.currentIndex() == 2 and not self.tab2.caseID:
            informBox = QtWidgets.QMessageBox.warning(self, '警告',"<p style='font-size:12pt;'>請先建立新個案或匯入個案</p>", QtWidgets.QMessageBox.Ok)

    def checkTab2Changed(self):
        if ((self.currentIndex() == 3 and self.tab2.isEdit()) or (self.currentIndex() == 3 and self.tab3.getEdit())):
            self.tab3.clearContent()
            informBox = QtWidgets.QMessageBox.warning(self, '警告',"<p style='font-size:12pt;'>轉錄表已變動 請重新產生彙整表</p>", QtWidgets.QMessageBox.Ok)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    demo = MainTabWidget()
    demo.show()
    sys.exit(app.exec_())
