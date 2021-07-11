import database.DBapi
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QLineSeries, QChartView, QPieSeries, QPieSlice, QBarSet, QPercentBarSeries, QBarCategoryAxis, QValueAxis
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import QPoint, Qt, QPointF

class chartTab(QtWidgets.QWidget):
    def __init__(self):
        super(chartTab, self).__init__()
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

    @QtCore.pyqtSlot(dict)
    def create_piechart(self, Doc):
        if Doc == None:
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
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.darkGreen, 6))
        slice.setBrush(Qt.green)

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Pie Chart Example")
 
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
    def create_linechart(self, Doc):
        if Doc['transcription']['analysis'] == None:
            return
        self.clearlayout()
        caseDocs = database.DBapi.findDocsByCaseID(Doc['childData']['caseID'])
        caseDocs = list(caseDocs)
        
        chart =  QChart()
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
