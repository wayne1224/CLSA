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
        for i in reversed(range(self.layout.count())):
            # print(self.layout.count())
            self.layout.removeItem(self.layout.itemAt(i))

    @QtCore.pyqtSlot(list)
    def lineChart(self, caseDocs):
        self.clearLayout()
        chart =  QChart()
        chart.setTitle(caseDocs[0]['caseID'] + "個案分析")
        font = QtGui.QFont()
        font.setPixelSize(24)
        chart.setTitleFont(font)

        axisX = QBarCategoryAxis()
        axisY = QValueAxis()
        chart.addAxis(axisY, Qt.AlignLeft)
        axisY.setRange(0.0, 100.0)

        categories = []
        lineSeriesVOCD_w = QLineSeries(self)
        lineSeriesVOCD_w.setName("VOCD-w")
        lineSeriesVOCD_c = QLineSeries(self)
        lineSeriesVOCD_c.setName("VOCD-c")
        analsisfail = 0
        for i, index in enumerate(caseDocs):
            if index['transcription']['analysis'] != None:
                if (index['transcription']['analysis']['VOCD-w'] != '樣本數不足') :
                    strDate = index['date'].strftime("%Y-%m-%d %H:%M")
                    categories.append(strDate)
                    lineSeriesVOCD_w.append(QPoint(i - analsisfail, index['transcription']['analysis']['VOCD-w']))
                    lineSeriesVOCD_c.append(QPoint(i - analsisfail, index['transcription']['analysis']['VOCD-c']))
                else : analsisfail += 1
        axisX.append(categories)
        chart.addAxis(axisX, Qt.AlignBottom)
        if len(categories) - 1 > 0 :
            axisX.setRange(categories[0], categories[len(categories) - 1])
        
        chart.addSeries(lineSeriesVOCD_w)
        chart.addSeries(lineSeriesVOCD_c)
        lineSeriesVOCD_w.attachAxis(axisX)
        lineSeriesVOCD_w.attachAxis(axisY)
        lineSeriesVOCD_c.attachAxis(axisX)
        lineSeriesVOCD_c.attachAxis(axisY)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        
        self.layout.addWidget(chartView)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen = lineChartTab()
    screen.show()
    sys.exit(app.exec_())