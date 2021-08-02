import database.DatabaseApi
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
        # self.lineChart()

    # #清除原本layout裡的Widget
    def clearLayout(self):
        for i in reversed(range(self.layout.count())):
            # print(self.layout.count())
            self.layout.removeItem(self.layout.itemAt(i))

    @QtCore.pyqtSlot()
    def lineChart(self):
        caseDocs = database.DatabaseApi.findDocs('','','')
        self.clearLayout()
        chart =  QChart()
        # chart.setTitle(caseDocs[0]['caseID'] + "個案分析")
        font = QtGui.QFont()
        font.setPixelSize(24)
        # chart.setTitleFont(font)
        print(caseDocs)

        axisY = QValueAxis()
        chart.addAxis(axisY, Qt.AlignLeft)
        # axisY.setRange(0.0, 100.0)
        biggestValue = 100.0

        categories = ['4~5', '6~7', '8~9', '10~11', '12~13', '14~15']
        axisX = QBarCategoryAxis()
        axisX.append(categories)
        chart.addAxis(axisX, Qt.AlignBottom)
        axisX.setRange("4~5", "14~15")
        sumContent = {'4': 0, '6': 0, '8': 0, '10' : 0, '12': 0, '14' : 0}
        count = 0
        for i, index in enumerate(caseDocs):
            set = QBarSet('VOCD')
            set.setLabelFont(font)
            caseDate = index['date']
            today = datetime.today()
            age = today.year - caseDate.year - ((today.month, today.day) < (caseDate.month, caseDate.day))
            if index['transcription']['analysis'] != None:
                if (index['transcription']['analysis']['VOCD-w'] != '樣本數不足') :
                    count += 1
                    if age >= 4 and age < 6: sumContent['4'] += index['transcription']['analysis']['VOCD-w']
                    elif age >= 6 and age < 8: sumContent['6'] += index['transcription']['analysis']['VOCD-w']
                    elif age >= 8 and age < 10: sumContent['8'] += index['transcription']['analysis']['VOCD-w']
                    elif age >= 10 and age < 12: sumContent['10'] += index['transcription']['analysis']['VOCD-w']
                    elif age >= 12 and age < 14: sumContent['12'] += index['transcription']['analysis']['VOCD-w']
                    elif age >= 14: sumContent['14'] += index['transcription']['analysis']['VOCD-w']

        barSeries = QBarSeries(self)
        set<< sumContent['4']/count\
        <<  sumContent['6']/count\
        << sumContent['8']/count\
        << sumContent['10']/count\
        << sumContent['12']/count\
        << sumContent['14']/count
        for i, (key, value) in enumerate(sumContent):
            if biggestValue < value/count:
                biggestValue+=20

        axisY.setRange(0.0, biggestValue)
        barSeries.append(set)
        barSeries.attachAxis(axisX)
        barSeries.attachAxis(axisY)

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