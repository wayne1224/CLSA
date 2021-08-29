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

    def lineChart(self):
        caseDocs = database.DatabaseApi.findDocs('','','')
        self.clearLayout()
        chart =  QChart()
        font = QtGui.QFont()
        font.setPixelSize(24)
        font.setBold(True)
        chart.setTitle('各年齡層分析圖表')
        chart.setTitleFont(font)
        font = QtGui.QFont()
        font.setPixelSize(24)
        # chart.setTitleFont(font)
        # print(caseDocs)
        axisY = QValueAxis()
        chart.addAxis(axisY, Qt.AlignLeft)
        # axisY.setRange(0.0, 100.0)
        biggestValue = 100.0

        categories = ['4~5', '6~7', '8~9', '10~11', '12~13', '14~15']
        axisX = QBarCategoryAxis()
        axisX.append(categories)
        chart.addAxis(axisX, Qt.AlignBottom)
        axisX.setRange("4~5", "14~15")
        sumContentw = {'4': 0, '6': 0, '8': 0, '10' : 0, '12': 0, '14' : 0}
        sumContentc = {'4': 0, '6': 0, '8': 0, '10' : 0, '12': 0, '14' : 0}
        count = 0
        for i, index in enumerate(caseDocs):
            set1 = QBarSet('VOCD-w')
            set1.setLabelFont(font)
            set2 = QBarSet('VOCD-c')
            set2.setLabelFont(font)
            caseDate = index['childData']['birthday']
            today = datetime.today()
            age = today.year - caseDate.year
            # print(age)
            if index['transcription']['analysis'] != None:
                if (index['transcription']['analysis']['VOCD-w'] != '樣本數不足') :
                    count += 1
                    if age >= 4 and age < 6: 
                        sumContentw['4'] += index['transcription']['analysis']['VOCD-w']
                        sumContentc['4'] += index['transcription']['analysis']['VOCD-c']
                    elif age >= 6 and age < 8: 
                        sumContentw['6'] += index['transcription']['analysis']['VOCD-w']
                        sumContentc['6'] += index['transcription']['analysis']['VOCD-c']
                    elif age >= 8 and age < 10: 
                        sumContentw['8'] += index['transcription']['analysis']['VOCD-w']
                        sumContentc['8'] += index['transcription']['analysis']['VOCD-c']
                    elif age >= 10 and age < 12: 
                        sumContentw['10'] += index['transcription']['analysis']['VOCD-w']
                        sumContentc['10'] += index['transcription']['analysis']['VOCD-c']
                    elif age >= 12 and age < 14: 
                        sumContentw['12'] += index['transcription']['analysis']['VOCD-w']
                        sumContentc['12'] += index['transcription']['analysis']['VOCD-c']
                    elif age >= 14: 
                        sumContentw['14'] += index['transcription']['analysis']['VOCD-w']
                        sumContentc['14'] += index['transcription']['analysis']['VOCD-c']

        barSeries = QBarSeries(self)
        chart.addSeries(barSeries)
        set1<< sumContentw['4']/count\
        <<  sumContentw['6']/count\
        << sumContentw['8']/count\
        << sumContentw['10']/count\
        << sumContentw['12']/count\
        << sumContentw['14']/count

        set2<< sumContentc['4']/count\
        <<  sumContentc['6']/count\
        << sumContentc['8']/count\
        << sumContentc['10']/count\
        << sumContentc['12']/count\
        << sumContentc['14']/count

        for i, (key, value) in enumerate(sumContentw.items()):
            if biggestValue < value/count:
                biggestValue+=20

        axisY.setRange(0.0, biggestValue)
        barSeries.append(set1)
        barSeries.append(set2)
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