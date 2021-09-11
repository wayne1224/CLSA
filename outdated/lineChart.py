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

#算年紀
        # today = date.today()
        # ageNum = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
        # if birthday.month >= 6:
        #     ageNum += 0.5
        # norm = db.findClosestNorm(ageNum) 

        
        # if Doc['transcription']['analysis'] == None: #是否已分析過
        #     return
        
        # caseDocs = db.findDocsByCaseID(caseID) #查詢個案紀錄
        
       
        # #VOCD
        # self.chart2 =  QChart()
        # self.chart2.setTitle("詞彙多樣性/字的多樣性")
        # self.chart2.setTitleFont(font)

        # axisX2 = QBarCategoryAxis()
        # axisY2 = QValueAxis()
        # self.chart2.addAxis(axisY2, Qt.AlignLeft)
        # # axisY2.setRange(0.0, 100.0)
        # biggestValue2 = 100.0

        # categories2 = []
        # lineSeriesAverageVOCD_w = QLineSeries(self)
        # lineSeriesAverageVOCD_w.setName('VOCD-w('+ norm['age'] + ')')
        # lineSeriesVOCD_w = QLineSeries(self)
        # lineSeriesVOCD_w.setName("VOCD-w")
        # lineSeriesVOCD_c = QLineSeries(self)
        # lineSeriesVOCD_c.setName("VOCD-c")
        # analysisFail = 0
        # # print(norm['data']['vocd-w'])
        # for i, index in enumerate(caseDocs):
        #     if index['transcription']['analysis'] != None:
        #         if (index['transcription']['analysis']['VOCD-w'] != '樣本數不足') :
        #             strDate = index['date'].strftime("%Y-%m-%d %H:%M")
        #             categories2.append(strDate)
        #             lineSeriesAverageVOCD_w.append(QPoint(i - analysisFail, float(norm['data']['vocd-w'])))
        #             lineSeriesVOCD_w.append(QPoint(i - analysisFail, index['transcription']['analysis']['VOCD-w']))
        #             lineSeriesVOCD_c.append(QPoint(i - analysisFail, index['transcription']['analysis']['VOCD-c']))
        #             while (index['transcription']['analysis']['VOCD-w'] > biggestValue2 or\
        #                    index['transcription']['analysis']['VOCD-c'] > biggestValue2) :
        #                 biggestValue2 += 20
        #         else: 
        #             analysisFail += 1

        # axisY2.setRange(0.0, biggestValue2)
        # axisX2.append(categories2)
        # self.chart2.addAxis(axisX2, Qt.AlignBottom)
        # if len(categories2) - 1 > 0 :
        #     axisX2.setRange(categories2[0], categories2[len(categories2) - 1])
        
        # self.chart2.addSeries(lineSeriesVOCD_w)
        # self.chart2.addSeries(lineSeriesVOCD_c)
        # self.chart2.addSeries(lineSeriesAverageVOCD_w)
        # lineSeriesAverageVOCD_w.attachAxis(axisX2)
        # lineSeriesAverageVOCD_w.attachAxis(axisY2)
        # lineSeriesVOCD_w.attachAxis(axisX2)
        # lineSeriesVOCD_w.attachAxis(axisY2)
        # lineSeriesVOCD_c.attachAxis(axisX2)
        # lineSeriesVOCD_c.attachAxis(axisY2)
        # #設線的寬度
        # penAverageVOCD_w = lineSeriesVOCD_w.pen()
        # penVOCD_w = lineSeriesVOCD_w.pen()
        # penVOCD_c = lineSeriesVOCD_c.pen()
        # penAverageVOCD_w.setWidth(5)
        # penVOCD_w.setWidth(5)
        # penVOCD_c.setWidth(5)
        # lineSeriesAverageVOCD_w.setPen(penAverageVOCD_w)
        # lineSeriesVOCD_w.setPen(penVOCD_w)
        # lineSeriesVOCD_c.setPen(penVOCD_c)
        # #虛線
        # lineSeriesAverageVOCD_w.setPen(QPen(Qt.red, 3, Qt.DashLine,  Qt.RoundCap, Qt.RoundJoin))
        # #axisX2.setLabelsFont(labelFont)
        # axisY2.setLabelsFont(labelFont)

        # self.chart2.legend().setFont(barFont)
        # self.chart2.legend().setVisible(True)
        # self.chart2.legend().setAlignment(Qt.AlignBottom)

        # self.chartView2 = QChartView(self.chart2)
        # self.chartView2.setRenderHint(QPainter.Antialiasing)
        # self.chartView2.setMinimumSize(500, 500)

        # #MLU
        # self.chart3 =  QChart()
        # self.chart3.setTitle("平均語句長度")
        # self.chart3.setTitleFont(font)

        # axisX3 = QBarCategoryAxis()
        # axisY3 = QValueAxis()
        # self.chart3.addAxis(axisY3, Qt.AlignLeft)
        # biggestValue3 = 20.0

        # categories3 = []
        # lineSeriesAverageMLU_w = QLineSeries(self)
        # lineSeriesAverageMLU_w.setName('MLU-w('+ norm['age'] + ')')
        # lineSeriesMLU_w = QLineSeries(self)
        # lineSeriesMLU_w.setName("MLU-w")
        # lineSeriesMLU_c = QLineSeries(self)
        # lineSeriesMLU_c.setName("MLU-c")
        # for i, index in enumerate(caseDocs):
        #     if index['transcription']['analysis'] != None:
        #         strDate = index['date'].strftime("%Y-%m-%d %H:%M")
        #         categories3.append(strDate)
        #         lineSeriesAverageMLU_w.append(QPoint(i, float(norm['data']['mlu-w'])))
        #         lineSeriesMLU_w.append(QPoint(i, index['transcription']['analysis']['MLU-w']))
        #         lineSeriesMLU_c.append(QPoint(i, index['transcription']['analysis']['MLU-c']))
        #         while (index['transcription']['analysis']['MLU-w'] > biggestValue3 or\
        #                 index['transcription']['analysis']['MLU-c'] > biggestValue3) :
        #             biggestValue3 += 10
        # axisY3.setRange(0.0, biggestValue3)
        # axisX3.append(categories3)
        # self.chart3.addAxis(axisX3, Qt.AlignBottom)
        # if len(categories3) - 1 > 0 :
        #     axisX3.setRange(categories3[0], categories3[len(categories3) - 1])
        
        # self.chart3.addSeries(lineSeriesMLU_w)
        # self.chart3.addSeries(lineSeriesMLU_c)
        # self.chart3.addSeries(lineSeriesAverageMLU_w)
        # lineSeriesAverageMLU_w.attachAxis(axisX3)
        # lineSeriesAverageMLU_w.attachAxis(axisY3)

        # lineSeriesMLU_w.attachAxis(axisX3)
        # lineSeriesMLU_w.attachAxis(axisY3)
        # lineSeriesMLU_c.attachAxis(axisX3)
        # lineSeriesMLU_c.attachAxis(axisY3)
        # #設線的寬度
        # penAverageMLU_w = lineSeriesMLU_w.pen()
        # penMLU_w = lineSeriesMLU_w.pen()
        # penMLU_c = lineSeriesMLU_c.pen()
        # penAverageMLU_w.setWidth(5)
        # penMLU_w.setWidth(5)
        # penMLU_c.setWidth(5)
        # lineSeriesAverageMLU_w.setPen(penAverageMLU_w)
        # lineSeriesMLU_w.setPen(penMLU_w)
        # lineSeriesMLU_c.setPen(penMLU_c)
        # #虛線
        # lineSeriesAverageMLU_w.setPen(QPen(Qt.red, 3, Qt.DashLine,  Qt.RoundCap, Qt.RoundJoin))
        # axisX3.setLabelsFont(labelFont)
        # axisY3.setLabelsFont(labelFont)

        # self.chart3.legend().setFont(barFont)
        # self.chart3.legend().setVisible(True)
        # self.chart3.legend().setAlignment(Qt.AlignBottom)

        # self.chartView3 = QChartView(self.chart3)
        # self.chartView3.setRenderHint(QPainter.Antialiasing)
        # self.chartView3.setMinimumSize(500, 500)

        # #self.layout.addWidget(chartView)
        
        # #如果樣本數不足，則須提示
        # if analysisFail != 0:
        #     self.hintArea = QtWidgets.QHBoxLayout()
        #     self.hintArea.addWidget(self.graph_hint_icon)
        #     self.hintArea.addWidget(self.graph_hint_text)
        #     self.scroll_vbox.addLayout(self.hintArea) 