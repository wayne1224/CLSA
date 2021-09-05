import database.DatabaseApi as db
import math
from datetime import datetime
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtChart import QChart, QBarSeries, QChartView, QBarSet, QBarCategoryAxis, QValueAxis
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt


class statChartTab(QtWidgets.QWidget):
    def __init__(self):
        super(statChartTab, self).__init__()
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

    # #清除原本layout裡的Widget
    def clearLayout(self):
        for i in reversed(range(self.layout.count())):
            self.layout.removeItem(self.layout.itemAt(i))

    def createBarCharts(self):
        self.createBar("VOCD", title=True)
        self.createBar("MLU")

    def createBar(self, type, title=False):
        #給定dict名稱
        w = type + '-w'
        c = type + '-c'

        if type == "MLU":
            #maxValue = 25 #Y Range
            color_w = QColor(37, 150, 190)
            color_c = QColor(143, 186, 82)
        else:
            color_w = QColor(246, 166, 38)
            color_c = QColor(191, 90, 63)
            #maxValue = 100

        #讀取所有documents
        caseDocs = db.findDocs('','','')
        norms = list(db.getNormAges())

        #共用字體
        font = QtGui.QFont()
        font.setPixelSize(24)
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
                
                list_W.append(v/n)
            else:
                remove_W.append(idx)
    
        for idx, (v,n) in enumerate(zip(sum_C.values(),nums_C.values())):
            if n != 0:
                list_C.append(v/n)
            else:
                remove_C.append(idx)
        
        maxValue = max(list_C + list_W) + 5
                
        set_W.append(list_W)
        set_C.append(list_C)
        #設顏色
        set_W.setColor(color_w)
        set_C.setColor(color_c)

        #Series
        series = QBarSeries()
        series.append(set_W)
        series.append(set_C)

        #宣告vocd圖
        chart = QChart()
        chart.addSeries(series)
        chart.setTitleFont(font)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.layout().setContentsMargins(0, 0, 0, 0)
        chart.setBackgroundRoundness(0);

        if title:
            chart.setTitle('系統中各年齡層VOCD和MLU統計')


        ##建立x軸
        axisX = QBarCategoryAxis()
        categories = []
        for i, n in enumerate(norms): ##TODO: 判斷有c沒w的情境
            if i not in remove_C:
                categories.append(str(n['ageNum']))

        axisX.append(categories)
        axisX.setTitleText("歲數")
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)

        ##建立y軸
        axisY = QValueAxis()
        axisY.setRange(0, maxValue)
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)
        
        chartView = QChartView(chart)
        chartView.setMinimumSize(500, 200)
        self.layout.addWidget(chartView)
 

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     screen = lineChartTab()
#     screen.show()
#     sys.exit(app.exec_())