import database.DatabaseApi as db
import qtawesome as qta
from functools import partial
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QBarSeries, QLineSeries, QChartView, QPieSeries, QPieSlice, QBarSet, QPercentBarSeries, QBarCategoryAxis, QValueAxis
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import QPoint, Qt, QPointF
from components.lineChart import lineChartTab

class Tab4(QtWidgets.QTabWidget):
    def __init__(self):
        super(Tab4, self).__init__()
        self.tab0 = chartTab()
        self.tab1 = lineChartTab()

        self.addTab(self.tab0, "個案分析圖表")
        self.addTab(self.tab1, "各年齡層分析圖表")

        #self.tab0.procCaseDocs.connect(self.tab1.lineChart)

class searchForm(QtWidgets.QWidget):
    def __init__(self):
        super(searchForm, self).__init__()
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.setLayout(self.verticalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 180))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 1)

        self.upperLayout = QtWidgets.QHBoxLayout()
        self.upperLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.upperLayout.setObjectName("upperLayout")

        #test addition QWidget
        self.upperContainer = QtWidgets.QWidget()
        self.upperContainer.setLayout(self.upperLayout)
        self.upperContainer.setMaximumSize(QtCore.QSize(16777215, 60))


        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.input_caseID = QtWidgets.QLineEdit()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_caseID.sizePolicy().hasHeightForWidth())
        self.input_caseID.setSizePolicy(sizePolicy)
        self.input_caseID.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.input_caseID.setFont(font)
        self.input_caseID.setObjectName("input_caseID")
        self.horizontalLayout_2.addWidget(self.input_caseID)
        self.upperLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.input_name = QtWidgets.QLineEdit()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_name.sizePolicy().hasHeightForWidth())
        self.input_name.setSizePolicy(sizePolicy)
        self.input_name.setMaximumSize(QtCore.QSize(16777215, 50))
        self.input_name.setObjectName("input_name")
        self.input_name.setFont(font)

        #提示字
        self.icon = QtWidgets.QLabel()
        self.icon.setPixmap(qta.icon('fa.info-circle',color='#eed202').pixmap(QtCore.QSize(25, 25)))
        self.icon.setMaximumSize(QtCore.QSize(25, 25))
        self.remindText = QtWidgets.QLabel()
        self.remindText.setMaximumSize(QtCore.QSize(16777215, 25))
        self.remindHorizontal = QtWidgets.QHBoxLayout()

        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        self.remindHorizontal.addItem(spacerItem)
        self.remindHorizontal.addWidget(self.icon)
        self.remindHorizontal.addWidget(self.remindText)
        
        self.gridLayout.addLayout(self.remindHorizontal, 2, 0, 1, 1)

        self.horizontalLayout_3.addWidget(self.input_name)
        self.search_btn = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy)
        self.search_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.search_btn.setFont(font)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_3.addWidget(self.search_btn)
        self.upperLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addWidget(self.upperContainer, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.retranslateUi()
        # self.setStyleSheet(open("C:/Users/HAO/Desktop/Code/Python/CLSA/QSS/Chart.qss", "r").read())
        self.setStyleSheet(open("QSS/Chart.qss", "r").read())
        
    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("", "名字"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("", "性別"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("", "生日"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("", "就診次數"))
        self.label_2.setText(_translate("", "個案編號："))
        self.label.setText(_translate("", "個案姓名："))
        self.search_btn.setText(_translate("", "  查詢個案  "))
        self.remindText.setText(_translate("", "輸入欄都空白，則顯示所有孩童"))


class chartTab(QtWidgets.QWidget):
    def __init__(self):
        super(chartTab, self).__init__()
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.layout)
        self.form = searchForm()

        #add searchForm
        self.layout.addWidget(self.form)
        self.form.search_btn.clicked.connect(self.search)

        #ScrollArea
        self.scroll = QtWidgets.QScrollArea()
        self.virtualWidget = QtWidgets.QWidget() #Widget that contains collection of VBOX
        self.scroll_vbox = QtWidgets.QVBoxLayout()
        self.virtualWidget.setLayout(self.scroll_vbox)
        ## Properties
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.virtualWidget)
        ##
        

    def search(self):
        #移除提示
        # self.form.remindText.setHidden(True)
        # self.form.icon.setHidden(True)

        cursor = db.findChildren(self.form.input_caseID.text() , self.form.input_name.text())
        print(self.form.input_caseID.text(),self.form.input_name.text())
    
        while self.form.tableWidget.rowCount() > 0:
            self.form.tableWidget.removeRow(self.form.tableWidget.rowCount()-1)

        if cursor:
            idx = 0
            for idx, child in enumerate(cursor):
                self.form.tableWidget.insertRow(idx)        
                
                item = QtWidgets.QTableWidgetItem()
                item.setText(child['name'])
                self.form.tableWidget.setItem(idx , 0 , item)

                item = QtWidgets.QTableWidgetItem()
                if child['gender'] == 'male':
                    item.setText('男')
                elif child['gender'] == 'female':
                    item.setText('女')
                self.form.tableWidget.setItem(idx , 1 , item)

                item = QtWidgets.QTableWidgetItem()
                time = datetime.strftime(child['birthday'],'%Y-%m-%d')
                item.setText(time)
                self.form.tableWidget.setItem(idx , 2 , item)

                item = QtWidgets.QTableWidgetItem()
                item.setText(str(len(child['document'])))
                self.form.tableWidget.setItem(idx , 3 , item)
                
                importBtn = QtWidgets.QPushButton('顯示圖表')
                importBtn.setStyleSheet("QPushButton {background-color: cornflowerblue;} QPushButton:hover{background-color: rgb(90, 138, 226);}")
                self.form.tableWidget.setCellWidget(idx, 4,importBtn)
                importBtn.clicked.connect(partial(self.create_linebarchart , child['document']))
            if idx == 0:
                QtWidgets.QMessageBox.information(self, '查詢','查無資料', QtWidgets.QMessageBox.Ok)

        else:
            QtWidgets.QMessageBox.information(self, 'Database','資料庫讀取中', QtWidgets.QMessageBox.Ok)

    # #清除原本layout裡的Widget
    def clearLayout(self):
        for i in reversed(range(self.scroll_vbox.count())):
            # print(self.scroll_vbox.count())
            self.scroll_vbox.removeItem(self.scroll_vbox.itemAt(i))


    def create_linebarchart(self, doc):
        #self.procCaseDocs.emit(doc)

        #檢查是否轉錄過
        count = 0
        tempDoc = doc.copy()
        for b in tempDoc:
            print(b['transcription']['analysis'])
            if b['transcription']['analysis'] != None:
                count += 1

        if count == 0:
            self.clearLayout()
            QtWidgets.QMessageBox.information(self, '','尚未轉錄過無法生成資料', QtWidgets.QMessageBox.Ok)
            return
        

        
        # if Doc['transcription']['analysis'] == None: #是否已分析過
        #     return
        self.clearLayout()
        # caseDocs = db.findDocsByCaseID(caseID) #查詢個案紀錄
        caseDocs = doc

        chart =  QChart()
        chart.setTitle("個案" + caseDocs[0]['caseID'] + "就診紀錄")
        font = QtGui.QFont()
        font.setPixelSize(24)
        chart.setTitleFont(font)
        categories = ["名詞", "動詞", "形容詞", "數詞", "量詞", "代詞", "副詞"]
        axisX = QBarCategoryAxis()
        axisX.append(categories)
        chart.addAxis(axisX, Qt.AlignBottom)
        axisY = QValueAxis()
        chart.addAxis(axisY, Qt.AlignLeft)
        # axisY.setRange(0.0, 20.0)
        biggestValue = 20.0
        axisX.setRange("名詞", "副詞")
        axisY.setTitleText("詞的個數")
        axisY.setTitleFont(font)
        # sumContent = {'N': 0, 'V': 0, 'VH': 0, 'Neu' : 0, 'Nf': 0, 'Nh' : 0, 'D' : 0}
        # recordCount = 0
        barSeries = QBarSeries(self)
        chart.addSeries(barSeries)
        for index in caseDocs:
            if index['transcription']['analysis'] != None:
                strDate = index['date'].strftime("%Y-%m-%d %H:%M")
                set = QBarSet(strDate)
                set.setLabelFont(font)
                # for i, (key, value) in enumerate(index['transcription']['analysis']['Content'].items()) :
                #     if key != 'percentage':
                #         if key == 'sum': recordCount += 1
                #         else : sumContent[key] += value
                set<< index['transcription']['analysis']['Content']['N']\
                    <<  index['transcription']['analysis']['Content']['V']\
                    << index['transcription']['analysis']['Content']['VH']\
                    << index['transcription']['analysis']['Content']['Neu']\
                    << index['transcription']['analysis']['Content']['Nf']\
                    << index['transcription']['analysis']['Content']['Nh']\
                    << index['transcription']['analysis']['Content']['D']
                for i, (key, value) in enumerate(index['transcription']['analysis']['Content'].items()):
                    while(value > biggestValue and key != 'sum') :
                        # print(str(i) + str(key)+ str(value)) 
                        biggestValue+=10.0
                barSeries.append(set)
        axisY.setRange(0, biggestValue)
        # print('last:' + str(biggestValue))
        barSeries.attachAxis(axisX)
        barSeries.attachAxis(axisY)
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

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        chartView.setMinimumSize(800, 500)
        
        #VOCD
        chart2 =  QChart()
        chart2.setTitle("詞彙多樣性/字的多樣性")
        chart2.setTitleFont(font)

        axisX2 = QBarCategoryAxis()
        axisY2 = QValueAxis()
        chart2.addAxis(axisY2, Qt.AlignLeft)
        # axisY2.setRange(0.0, 100.0)
        biggestValue2 = 100.0

        categories2 = []
        lineSeriesVOCD_w = QLineSeries(self)
        lineSeriesVOCD_w.setName("VOCD-w")
        lineSeriesVOCD_c = QLineSeries(self)
        lineSeriesVOCD_c.setName("VOCD-c")
        analsisfail = 0
        for i, index in enumerate(caseDocs):
            if index['transcription']['analysis'] != None:
                if (index['transcription']['analysis']['VOCD-w'] != '樣本數不足') :
                    strDate = index['date'].strftime("%Y-%m-%d %H:%M")
                    categories2.append(strDate)
                    lineSeriesVOCD_w.append(QPoint(i - analsisfail, index['transcription']['analysis']['VOCD-w']))
                    lineSeriesVOCD_c.append(QPoint(i - analsisfail, index['transcription']['analysis']['VOCD-c']))
                    while (index['transcription']['analysis']['VOCD-w'] > biggestValue2 or\
                           index['transcription']['analysis']['VOCD-c'] > biggestValue2) :
                        biggestValue2 += 20
                else : analsisfail += 1
        axisY2.setRange(0.0, biggestValue2)
        axisX2.append(categories2)
        chart2.addAxis(axisX2, Qt.AlignBottom)
        if len(categories2) - 1 > 0 :
            axisX2.setRange(categories2[0], categories2[len(categories2) - 1])
        
        chart2.addSeries(lineSeriesVOCD_w)
        chart2.addSeries(lineSeriesVOCD_c)
        lineSeriesVOCD_w.attachAxis(axisX2)
        lineSeriesVOCD_w.attachAxis(axisY2)
        lineSeriesVOCD_c.attachAxis(axisX2)
        lineSeriesVOCD_c.attachAxis(axisY2)
        penVOCD_w = lineSeriesVOCD_w.pen()
        penVOCD_c = lineSeriesVOCD_c.pen()
        penVOCD_w.setWidth(5)
        penVOCD_c.setWidth(5)
        lineSeriesVOCD_w.setPen(penVOCD_w)
        lineSeriesVOCD_c.setPen(penVOCD_c)
        
        chart2.legend().setVisible(True)
        chart2.legend().setAlignment(Qt.AlignBottom)

        chartView2 = QChartView(chart2)
        chartView2.setRenderHint(QPainter.Antialiasing)
        chartView2.setMinimumSize(500, 500)

        #MLU
        chart3 =  QChart()
        chart3.setTitle("平均語句長度")
        chart3.setTitleFont(font)

        axisX3 = QBarCategoryAxis()
        axisY3 = QValueAxis()
        chart3.addAxis(axisY3, Qt.AlignLeft)
        biggestValue3 = 20.0

        categories3 = []
        lineSeriesMLU_w = QLineSeries(self)
        lineSeriesMLU_w.setName("MLU-w")
        lineSeriesMLU_c = QLineSeries(self)
        lineSeriesMLU_c.setName("MLU-c")
        for i, index in enumerate(caseDocs):
            if index['transcription']['analysis'] != None:
                strDate = index['date'].strftime("%Y-%m-%d %H:%M")
                categories3.append(strDate)
                lineSeriesMLU_w.append(QPoint(i, index['transcription']['analysis']['MLU-w']))
                lineSeriesMLU_c.append(QPoint(i, index['transcription']['analysis']['MLU-c']))
                while (index['transcription']['analysis']['MLU-w'] > biggestValue3 or\
                        index['transcription']['analysis']['MLU-c'] > biggestValue3) :
                    biggestValue3 += 10
        axisY3.setRange(0.0, biggestValue3)
        axisX3.append(categories3)
        chart3.addAxis(axisX3, Qt.AlignBottom)
        if len(categories3) - 1 > 0 :
            axisX3.setRange(categories3[0], categories3[len(categories3) - 1])
        
        chart3.addSeries(lineSeriesMLU_w)
        chart3.addSeries(lineSeriesMLU_c)
        lineSeriesMLU_w.attachAxis(axisX3)
        lineSeriesMLU_w.attachAxis(axisY3)
        lineSeriesMLU_c.attachAxis(axisX3)
        lineSeriesMLU_c.attachAxis(axisY3)
        penMLU_w = lineSeriesMLU_w.pen()
        penMLU_c = lineSeriesMLU_c.pen()
        penMLU_w.setWidth(5)
        penMLU_c.setWidth(5)
        lineSeriesMLU_w.setPen(penMLU_w)
        lineSeriesMLU_c.setPen(penMLU_c)
        
        chart3.legend().setVisible(True)
        chart3.legend().setAlignment(Qt.AlignBottom)

        chartView3 = QChartView(chart3)
        chartView3.setRenderHint(QPainter.Antialiasing)
        chartView3.setMinimumSize(500, 500)

        #self.layout.addWidget(chartView)
        self.scroll_vbox.addWidget(chartView)

        self.chartLayout = QtWidgets.QHBoxLayout()
        self.chartLayout.addWidget(chartView2)
        self.chartLayout.addWidget(chartView3)
        self.scroll_vbox.addLayout(self.chartLayout)

        self.layout.addWidget(self.scroll)
