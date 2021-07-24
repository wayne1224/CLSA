import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Chart import chartTab
from lineChart import lineChartTab

class Tab4(QtWidgets.QTabWidget):
    def __init__(self):
        super(Tab4, self).__init__()
        self.tab0 = chartTab()
        self.tab1 = lineChartTab()

        self.addTab(self.tab0, "個案查詢")
        self.addTab(self.tab1, "個案分析")

        self.tab0.procCaseDocs.connect(self.tab1.lineChart)
