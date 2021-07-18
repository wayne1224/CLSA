import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Chart import chartTab

class Tab4(QtWidgets.QTabWidget):
    def __init__(self):
        super(Tab4, self).__init__()
        self.tab0 = chartTab()
        #self.tab1 = Myform()

        self.addTab(self.tab0, "個案查詢")