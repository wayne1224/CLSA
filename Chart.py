import database.DBapi
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QBarSeries, QLineSeries, QChartView, QPieSeries, QPieSlice, QBarSet, QPercentBarSeries, QBarCategoryAxis, QValueAxis
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import QPoint, Qt, QPointF

class chartTab(QtWidgets.QWidget):
    def __init__(self):
        super(chartTab, self).__init__()
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

    @QtCore.pyqtSlot(dict)
    def create_piechart(self, Doc):
        if Doc['transcription']['analysis'] == None:
            return
        self.clearlayout()
        series = QPieSeries()
        series.append("名詞", Doc['transcription']['analysis']['Content']['N'])
        series.append("動詞", Doc['transcription']['analysis']['Content']['V'])
        series.append("形容詞", Doc['transcription']['analysis']['Content']['VH'])
        series.append("數詞", Doc['transcription']['analysis']['Content']['Neu'])
        series.append("量詞", Doc['transcription']['analysis']['Content']['Nf'])
        series.append("代詞", Doc['transcription']['analysis']['Content']['Nh'])
        series.append("副詞", Doc['transcription']['analysis']['Content']['D'])
 
        #adding slice
        slice = QPieSlice()
        slice = series.slices()[3]
        slice.setExploded(True)
        # slice.setPen(QPen(Qt.darkGreen, 6))
        # slice.setBrush(Qt.green)

        # series.setLabelsPosition(QtChart.QPieSlice.LabelInsideHorizontal)
        for slice in series.slices():
            slice.setLabel("{:.2f}%".format(100 * slice.percentage()))
            slice.setLabelVisible(True)

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("實詞百分比")
        font = QtGui.QFont()
        font.setPixelSize(24)
        chart.setTitleFont(font)
        
        chart.legend().markers(series)[0].setLabel("名詞")
        chart.legend().markers(series)[1].setLabel("動詞")
        chart.legend().markers(series)[2].setLabel("形容詞")
        chart.legend().markers(series)[3].setLabel("數詞")
        chart.legend().markers(series)[4].setLabel("量詞")
        chart.legend().markers(series)[5].setLabel("代詞")
        chart.legend().markers(series)[6].setLabel("副詞")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
 
        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        self.layout.addWidget(chartview)
    #清除原本layout裡的Widget
    def clearlayout(self):
        for i in reversed(range(self.layout.count())):
            print(self.layout.count())
            self.layout.removeItem(self.layout.itemAt(i))

    @QtCore.pyqtSlot(dict)
    def create_linebarchart(self, Doc):
        if Doc['transcription']['analysis'] == None:
            return
        self.clearlayout()
        caseDocs = database.DBapi.findDocsByCaseID(Doc['childData']['caseID'])
        caseDocs = list(caseDocs)
        
        chart =  QChart()
        chart.setTitle("個案" + Doc['childData']['caseID'] + "就診紀錄")
        font = QtGui.QFont()
        font.setPixelSize(24)
        chart.setTitleFont(font)
        categories = ["名詞", "動詞", "形容詞", "數詞", "量詞", "代詞", "副詞"]
        axisX = QBarCategoryAxis()
        axisX.append(categories)
        chart.addAxis(axisX, Qt.AlignBottom)
        axisY = QValueAxis()
        chart.addAxis(axisY, Qt.AlignLeft)

        averageContent = {'N': 0, 'V': 0, 'VH': 0, 'Neu' : 0, 'Nf': 0, 'Nh' : 0, 'D' : 0}
        recordCount = 0
        for index in caseDocs:
            if index['transcription']['analysis'] != None:
                barSeries = QBarSeries(self)
                strDate = index['recording']['date'].strftime("%Y-%m-%d %H:%M:%S")
                set0 = QBarSet(strDate)
                for i, (key, value) in enumerate(index['transcription']['analysis']['Content'].items()) :
                    # print(str(key) + ' ' + str(value))
                    if key != 'percentage':
                        if key == 'sum': recordCount += 1
                        else : averageContent[key] += value
                set0<< index['transcription']['analysis']['Content']['N']\
                    <<  index['transcription']['analysis']['Content']['V']\
                    << index['transcription']['analysis']['Content']['VH']\
                    << index['transcription']['analysis']['Content']['Neu']\
                    << index['transcription']['analysis']['Content']['Nf']\
                    << index['transcription']['analysis']['Content']['Nh']\
                    << index['transcription']['analysis']['Content']['D']
                barSeries.append(set0)
                chart.addSeries(barSeries)
                barSeries.attachAxis(axisX)
                barSeries.attachAxis(axisY)
        lineSeries = QLineSeries(self)
        lineSeries.setName("平均值")
        for i, (key, value) in enumerate(averageContent.items()):
            lineSeries.append(QPoint(i, value/recordCount))
        chart.addSeries(lineSeries)
        lineSeries.attachAxis(axisX)
        lineSeries.attachAxis(axisY)
        pen = lineSeries.pen()
        pen.setWidth(4)
        lineSeries.setPen(pen)

        axisY.setRange(0, 20)
        axisX.setRange("名詞", "副詞")
        axisY.setTitleText("詞的個數")
        axisY.setTitleFont(font)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        
        self.layout.addWidget(chartView)

    @QtCore.pyqtSlot(dict)
    def create_linechart(self, Doc):
        if Doc['transcription']['analysis'] == None:
            return
        self.clearlayout()
        caseDocs = database.DBapi.findDocsByCaseID(Doc['childData']['caseID'])
        caseDocs = list(caseDocs)
        
        chart =  QChart()
        chart.setTitle("個案" + Doc['childData']['caseID'] + "就診紀錄")
        font = QtGui.QFont()
        font.setPixelSize(24)
        chart.setTitleFont(font)
        
        categories = ["名詞", "動詞", "形容詞", "數詞", "量詞", "代詞", "副詞"]
        axisX = QBarCategoryAxis()
        axisX.append(categories)
        chart.addAxis(axisX, Qt.AlignBottom)
        axisY = QValueAxis()
        chart.addAxis(axisY, Qt.AlignLeft)

        for index in caseDocs:
            if index['transcription']['analysis'] != None:
                series = QLineSeries(self)
                strDate = index['recording']['date'].strftime("%Y-%m-%d %H:%M:%S")
                series.setName(strDate)
                series.append(QPoint(0, index['transcription']['analysis']['Content']['N']))
                series.append(QPoint(1, index['transcription']['analysis']['Content']['V']))
                series.append(QPoint(2, index['transcription']['analysis']['Content']['VH']))
                series.append(QPoint(3, index['transcription']['analysis']['Content']['Neu']))
                series.append(QPoint(4, index['transcription']['analysis']['Content']['Nf']))
                series.append(QPoint(5, index['transcription']['analysis']['Content']['Nh']))
                series.append(QPoint(6, index['transcription']['analysis']['Content']['D']))
                chart.addSeries(series)
                series.attachAxis(axisX)
                series.attachAxis(axisY)
        axisY.setRange(0, 20)
        axisX.setRange("名詞", "副詞")
        axisY.setTitleText("詞的個數")
        axisY.setTitleFont(font)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        
        self.layout.addWidget(chartView)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen = chartTab()
    screen.show()
    sys.exit(app.exec_())
