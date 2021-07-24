import database.DatabaseApi as db
import sys
from functools import partial
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QBarSeries, QLineSeries, QChartView, QPieSeries, QPieSlice, QBarSet, QPercentBarSeries, QBarCategoryAxis, QValueAxis
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import QPoint, Qt, QPointF

class lineChartTab(QtWidgets.QWidget):
    def __init__(self):
        super(lineChartTab, self).__init__()
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

    # #清除原本layout裡的Widget
    def clearLayout(self):
        for i in reversed(range(self.layout.count()-1)):
            print(self.layout.count())
            self.layout.removeItem(self.layout.itemAt(i+1))

    def lineChart(self, doc):
        self.clearLayout()
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen = lineChartTab()
    screen.show()
    sys.exit(app.exec_())