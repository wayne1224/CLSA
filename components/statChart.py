import database.DatabaseApi as db
import math
import time
from datetime import datetime
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtChart import QChart, QBarSeries, QChartView, QBarSet, QBarCategoryAxis, QValueAxis, QAbstractBarSeries, QLineSeries, QScatterSeries
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QSize, QDateTime, QDate


class statChartTab(QtWidgets.QWidget):
    def __init__(self):
        super(statChartTab, self).__init__()
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)

    # #清除原本layout裡的Widget
    def clearLayout(self):
        for i in reversed(range(self.layout.count())):
            self.layout.removeItem(self.layout.itemAt(i))

    def createBarCharts(self):
        self.createBar("VOCD", title=True)
        self.createBar("MLU")
        self.layout.addWidget(self.vocd_barChart)
        self.layout.addWidget(self.mlu_barChart) 

    def createBar(self, type, title=False):
        #給定dict名稱
        w = type + '-w'
        c = type + '-c'

        if type == "MLU":
            maxValue = 12 #Y Range
            color_w = QColor(37, 150, 190)
            color_c = QColor(143, 186, 82)
        else:
            maxValue = 120
            color_w = QColor(246, 166, 38)
            color_c = QColor(191, 90, 63)
            

        #讀取所有documents
        caseDocs = db.findDocs('','','')
        norms = list(db.getNormAges())

        #共用字體
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPixelSize(20)
        font.setBold(True)

        #建立barset (資料集)
        set_W = QBarSet(w) 
        set_C = QBarSet(c)

        ## 統計資料
        sum_W = { n['ageNum']:0 for n in norms}
        sum_C = { n['ageNum']:0 for n in norms}
        nums_C = { n['ageNum']:0 for n in norms}
        nums_W = { n['ageNum']:0 for n in norms}

        ##開始統計
        for doc in caseDocs:
            if doc['transcription']['analysis']:
                age = round(math.modf(doc['recording']['age'])[1]) #統計用的年齡標準，先取整歲
                if math.modf(doc['recording']['age'])[0] >= 0.5: #取小數點後一位
                    age += 0.5
                #print(age,  math.modf(2.5)[0])

                #開始算sum
                if doc['transcription']['analysis'][w] != "樣本數不足":
                    sum_W[age] += doc['transcription']['analysis'][w]
                    nums_W[age] += 1

                if doc['transcription']['analysis'][c] != "樣本數不足":
                    sum_C[age] += doc['transcription']['analysis'][c]
                    nums_C[age] += 1

        list_W = []
        remove_W = []
        list_C = []
        remove_C = []

        for idx, (v,n) in enumerate(zip(sum_W.values(),nums_W.values())):
            
            if n != 0:
                
                list_W.append(round(v/n, 1))
            else:
                remove_W.append(idx)
    
        for idx, (v,n) in enumerate(zip(sum_C.values(),nums_C.values())):
            if n != 0:
                list_C.append(round(v/n, 1))  #留一個小數點
            else:
                remove_C.append(idx)
        
        if type == "MLU":
            while round(max(list_C + list_W)) >= maxValue:
                maxValue += 4
       
        #載入barset資料
        set_W.append(list_W)
        set_C.append(list_C)
        #設顏色
        set_W.setColor(color_w)
        set_W.setLabelColor(QColor('black'))
        set_C.setColor(color_c)
        set_C.setLabelColor(QColor('black'))
        #設字體
        ## Bar Font
        bfont = QtGui.QFont()
        bfont.setFamily("微軟正黑體")
        bfont.setBold(True)
        set_W.setLabelFont(bfont)
        set_C.setLabelFont(bfont)

        #Series
        series = QBarSeries()
        series.append(set_W)
        series.append(set_C)
        series.setLabelsVisible(True)
        series.setLabelsPosition(QAbstractBarSeries.LabelsOutsideEnd)

        #宣告Chart
        chart = QChart()
        chart.addSeries(series)
        chart.setFont(font)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.legend().setFont(font)
        chart.layout().setContentsMargins(0, 0, 0, 0)
        #設定title字體
        tfont = QtGui.QFont()
        tfont.setFamily("微軟正黑體")
        tfont.setPixelSize(25)
        tfont.setBold(True)
        chart.setTitleFont(tfont)

        if title:
            chart.setTitle('本系統中各年齡之平均字彙多樣性(VOCD)和平均語句長度(MLU)統計')


        ##建立x軸
        axisX = QBarCategoryAxis()
        categories = []
        for i, n in enumerate(norms): ##TODO: 判斷有c沒w的情境
            if i not in remove_C:
                categories.append(str(n['ageNum']))

        axisX.append(categories)
        axisX.setTitleText("歲數")
        axisX.setLabelsFont(font)
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)

        ##建立y軸
        axisY = QValueAxis()
        axisY.setRange(0, maxValue)
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)

        
        if type == "MLU":
            self.mlu_barChart = QChartView(chart)
            self.mlu_barChart.setMinimumSize(QSize(400, 400))
        else:
            self.vocd_barChart = QChartView(chart)
            self.vocd_barChart.setMinimumSize(QSize(400, 400))
        
def createBarChart_POS(doc, name): #建立詞性的柱狀圖
    caseDocs = doc
    chart = QChart()
    chart.setTitle(name + " 就診紀錄")
    font = QtGui.QFont()
    font.setFamily("微軟正黑體")
    font.setPixelSize(28)
    font.setBold(True)
    chart.setTitleFont(font)
    categories = ["名詞", "動詞", "形容詞", "數詞", "量詞", "代詞", "副詞", "虛詞"]
    axisX = QBarCategoryAxis()
    axisX.append(categories)
    chart.addAxis(axisX, Qt.AlignBottom)
    axisY = QValueAxis()
    chart.addAxis(axisY, Qt.AlignLeft)
    # axisY.setRange(0.0, 20.0)
    biggestValue = 50.0
    axisX.setRange("名詞", "虛詞")
    axisY.setTitleText("詞性百分比")
    axisY.setTitleFont(font)
    # sumContent = {'N': 0, 'V': 0, 'VH': 0, 'Neu' : 0, 'Nf': 0, 'Nh' : 0, 'D' : 0}
    # recordCount = 0
    labelFont = QtGui.QFont()
    labelFont.setFamily("微軟正黑體")
    labelFont.setBold(True)
    labelFont.setPixelSize(20)
    barSeries = QBarSeries()
    chart.addSeries(barSeries)
    for index in caseDocs:
        if index['transcription']['analysis'] != None:
            strDate = index['date'].strftime("%Y-%m-%d %H:%M")
            set = QBarSet(strDate)
            set.setLabelFont(labelFont)
            # for i, (key, value) in enumerate(index['transcription']['analysis']['Content'].items()) :
            #     if key != 'percentage':
            #         if key == 'sum': recordCount += 1
            #         else : sumContent[key] += value
            set << index['transcription']['analysis']['Content']['N'] / index['transcription']['analysis']['wordCount'] * 100.0\
                <<  index['transcription']['analysis']['Content']['V'] / index['transcription']['analysis']['wordCount'] * 100.0\
                << index['transcription']['analysis']['Content']['VH'] / index['transcription']['analysis']['wordCount'] * 100.0\
                << index['transcription']['analysis']['Content']['Neu']/ index['transcription']['analysis']['wordCount'] * 100.0\
                << index['transcription']['analysis']['Content']['Nf']/ index['transcription']['analysis']['wordCount'] * 100.0\
                << index['transcription']['analysis']['Content']['Nh']/ index['transcription']['analysis']['wordCount'] * 100.0\
                << index['transcription']['analysis']['Content']['D']/ index['transcription']['analysis']['wordCount']  * 100.0\
                << index['transcription']['analysis']['Function']['sum']/ index['transcription']['analysis']['wordCount'] * 100.0
            # for i, (key, value) in enumerate(index['transcription']['analysis']['Content'].items()):
            #     while(value > biggestValue and key != 'sum') :
            #         # print(str(i) + str(key)+ str(value)) 
            #         biggestValue+=10.0
            for i in set:
                while(i > biggestValue) :
                    biggestValue+=25.0
            barSeries.append(set)
    axisY.setRange(0, biggestValue)
    # print('last:' + str(biggestValue))
    barSeries.attachAxis(axisX)
    barSeries.attachAxis(axisY)

    axisX.setLabelsFont(labelFont)
    axisY.setLabelsFont(labelFont)

    # lineSeries = QLineSeries(self)
    # lineSeries.setName("平均值")
    # for i, (key, value) in enumerate(sumContent.items()):
    #     if recordCount > 0:
    #         lineSeries.append(QPoint(i, value/recordCount))
    #     else :
    #         lineSeries.append(QPoint(i, 0))
    # chart.addSeries(lineSeries)
    # lineSeries.attachAxis(axisX)
    # lineSeries.attachAxis(axisY)
    # lineSeries.setColor(Qt.red)
    # pen = lineSeries.pen()
    # pen.setWidth(3)
    # lineSeries.setPen(pen)

    barFont =  QtGui.QFont()
    barFont.setPixelSize(20)
    barFont.setFamily("微軟正黑體")
    barFont.setBold(True)
    chart.legend().setFont(barFont)
    chart.legend().setVisible(True)
    chart.legend().setAlignment(Qt.AlignBottom)

    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)
    chartView.setMinimumSize(800, 500)

    return chartView  

def createLineChart(type, documents):
    w = type + '-w'
    c = type + '-c'

    title = ""
    if type == "MLU":
        maxValue = 12 #Y Range
        title = "平均語句長度"
    elif type == "VOCD":
        maxValue = 100
        title = "詞彙多樣性/字的多樣性"

    #共用字體
    font = QtGui.QFont()
    font.setFamily("微軟正黑體")
    font.setPixelSize(20)
    font.setBold(True)

    #建立資料series
    seriesW = QLineSeries()
    seriesW.setName(w)
    seriesC = QLineSeries()
    seriesC.setName(c)

    #載入資料
    dates = []
    i = 0
    for doc in documents:
        if doc['transcription']['analysis']:
            if type == "MLU":
                dates.append(doc['date'].strftime("%Y-%m-%d %H:%M"))
                seriesW.append(i, doc['transcription']['analysis'][w])
                seriesC.append(i, doc['transcription']['analysis'][c])
                i += 1
            elif type == "VOCD":
                if doc['transcription']['analysis'][w] != "樣本數不足":
                    dates.append(doc['date'].strftime("%Y-%m-%d %H:%M"))
                    seriesW.append(i, doc['transcription']['analysis'][w])
                    seriesC.append(i, doc['transcription']['analysis'][c])
                    i += 1
        else:
            print("沒彙整過:",doc['date'].year, doc['date'].month, doc['date'].day)
    

    if len(seriesC) == 1 and len(seriesW) == 1:
        #暫存原本的資料
        tempW = seriesW.at(0)
        tempC = seriesC.at(0)
        #並改用QScatter
        seriesW = QScatterSeries()
        seriesW.setName(w)
        seriesC = QScatterSeries()
        seriesC.setName(c)
        seriesW.setMarkerShape(QScatterSeries.MarkerShapeCircle)
        seriesC.setMarkerShape(QScatterSeries.MarkerShapeCircle)
        seriesW.append(tempW)
        seriesC.append(tempC)
       
    
    #宣告Chart
    chart = QChart()
    chart.setFont(font)
    chart.setAnimationOptions(QChart.SeriesAnimations)
    chart.legend().setAlignment(Qt.AlignBottom)
    chart.legend().setFont(font)
    chart.layout().setContentsMargins(0, 0, 0, 0)
    chart.setTitle(title)
    #設定title字體
    tfont = QtGui.QFont()
    tfont.setFamily("微軟正黑體")
    tfont.setPixelSize(25)
    tfont.setBold(True)
    chart.setTitleFont(tfont)

    #加入資料集
    chart.addSeries(seriesW)
    chart.addSeries(seriesC)

    ##建立x軸
    axisX = QBarCategoryAxis()
    axisX.append(dates)
    chart.setAxisX(axisX, seriesW)
    chart.setAxisX(axisX, seriesC)
    #axisX.setRange(dates[0], dates[-1])
    
    ##建立y軸
    axisY = QValueAxis()
    axisY.setRange(0, maxValue)
    chart.setAxisY(axisY, seriesW)
    chart.setAxisY(axisY, seriesC)

    chartView = QChartView(chart)
    chartView.setMinimumSize(QSize(400, 400))
    chartView.setRenderHint(QPainter.Antialiasing)
    return chartView  