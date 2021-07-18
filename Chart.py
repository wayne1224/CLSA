import database.DatabaseApi as db
import sys
from functools import partial
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QBarSeries, QLineSeries, QChartView, QPieSeries, QPieSlice, QBarSet, QPercentBarSeries, QBarCategoryAxis, QValueAxis
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import QPoint, Qt, QPointF


class searchForm(QtWidgets.QWidget):
    def __init__(self):
        super(searchForm, self).__init__()
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.setLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.input_caseID = QtWidgets.QLineEdit()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.input_caseID.setFont(font)
        self.input_caseID.setObjectName("input_caseID")
        self.horizontalLayout_2.addWidget(self.input_caseID)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.input_name = QtWidgets.QLineEdit()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.input_name.setFont(font)
        self.input_name.setObjectName("input_name")
        self.horizontalLayout_3.addWidget(self.input_name)
        self.search_btn = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.search_btn.setFont(font)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_3.addWidget(self.search_btn)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.retranslateUi()
        

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("Form", "個案編號："))
        self.label.setText(_translate("Form", "個案姓名："))
        self.search_btn.setText(_translate("Form", "查詢"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "名字"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "性別"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "生日"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "就診次數"))


class chartTab(QtWidgets.QWidget):
    def __init__(self):
        super(chartTab, self).__init__()
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        self.form = searchForm()
        #add searchForm
        self.layout.addWidget(self.form)
        self.form.search_btn.clicked.connect(self.search)


    def search(self):
        #API還沒寫
        cursor = db.findChildren(self.form.input_caseID.text() , self.form.input_name.text())

        while self.form.tableWidget.rowCount() > 0:
            self.form.tableWidget.removeRow(self.form.tableWidget.rowCount()-1)

        if cursor:
            for idx, child in enumerate(cursor):
                self.tableWidget.insertRow(idx)        
                
                item = QtWidgets.QTableWidgetItem()
                item.setText(child['name'])
                self.tableWidget.setItem(idx , 0 , item)

                item = QtWidgets.QTableWidgetItem()
                item.setText(child['gender'])
                self.tableWidget.setItem(idx , 1 , item)

                item = QtWidgets.QTableWidgetItem()
                time = datetime.strftime(child['birthday'],'%Y-%m-%d')
                item.setText(time)
                self.tableWidget.setItem(idx , 2 , item)

                item = QtWidgets.QTableWidgetItem()
                item.setText(len(child['documents']))
                self.tableWidget.setItem(idx , 3 , item)
                
                importBtn = QtWidgets.QPushButton('確認')
                self.tableWidget.setCellWidget(idx, 4,importBtn)
                importBtn.clicked.connect(partial(self.create_linebarchart , child['documents']))
        else:
            informBox = QtWidgets.QMessageBox.information(self, '查詢','查無資料', QtWidgets.QMessageBox.Ok)



    # @QtCore.pyqtSlot(dict)
    # def create_piechart(self, Doc):
    #     if Doc['transcription']['analysis'] == None:
    #         return
    #     self.clearlayout()
    #     series = QPieSeries()
    #     series.append("名詞", Doc['transcription']['analysis']['Content']['N'])
    #     series.append("動詞", Doc['transcription']['analysis']['Content']['V'])
    #     series.append("形容詞", Doc['transcription']['analysis']['Content']['VH'])
    #     series.append("數詞", Doc['transcription']['analysis']['Content']['Neu'])
    #     series.append("量詞", Doc['transcription']['analysis']['Content']['Nf'])
    #     series.append("代詞", Doc['transcription']['analysis']['Content']['Nh'])
    #     series.append("副詞", Doc['transcription']['analysis']['Content']['D'])
 
    #     #adding slice
    #     slice = QPieSlice()
    #     slice = series.slices()[3]
    #     slice.setExploded(True)
    #     # slice.setPen(QPen(Qt.darkGreen, 6))
    #     # slice.setBrush(Qt.green)

    #     # series.setLabelsPosition(QtChart.QPieSlice.LabelInsideHorizontal)
    #     for slice in series.slices():
    #         slice.setLabel("{:.2f}%".format(100 * slice.percentage()))
    #         slice.setLabelVisible(True)

    #     chart = QChart()
    #     chart.legend().hide()
    #     chart.addSeries(series)
    #     chart.createDefaultAxes()
    #     chart.setAnimationOptions(QChart.SeriesAnimations)
    #     chart.setTitle("實詞百分比")
    #     font = QtGui.QFont()
    #     font.setPixelSize(24)
    #     chart.setTitleFont(font)
        
    #     chart.legend().markers(series)[0].setLabel("名詞")
    #     chart.legend().markers(series)[1].setLabel("動詞")
    #     chart.legend().markers(series)[2].setLabel("形容詞")
    #     chart.legend().markers(series)[3].setLabel("數詞")
    #     chart.legend().markers(series)[4].setLabel("量詞")
    #     chart.legend().markers(series)[5].setLabel("代詞")
    #     chart.legend().markers(series)[6].setLabel("副詞")

    #     chart.legend().setVisible(True)
    #     chart.legend().setAlignment(Qt.AlignBottom)
 
    #     chartview = QChartView(chart)
    #     chartview.setRenderHint(QPainter.Antialiasing)
    #     self.layout.addWidget(chartview)
    # #清除原本layout裡的Widget
    # def clearlayout(self):
    #     for i in reversed(range(self.layout.count())):
    #         print(self.layout.count())
    #         self.layout.removeItem(self.layout.itemAt(i))


    def create_linebarchart(self, doc):
        # if Doc['transcription']['analysis'] == None: #是否已分析過
        #     return
        self.clearlayout()
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
        axisY.setRange(0, 20)
        axisX.setRange("名詞", "副詞")
        axisY.setTitleText("詞的個數")
        axisY.setTitleFont(font)
        sumContent = {'N': 0, 'V': 0, 'VH': 0, 'Neu' : 0, 'Nf': 0, 'Nh' : 0, 'D' : 0}
        recordCount = 0
        for index in caseDocs:
            if index['transcription']['analysis'] != None:
                barSeries = QBarSeries(self)
                strDate = index['recording']['date'].strftime("%Y-%m-%d %H:%M:%S")
                set0 = QBarSet(strDate)
                set0.setLabelFont(font)
                for i, (key, value) in enumerate(index['transcription']['analysis']['Content'].items()) :
                    # print(str(key) + ' ' + str(value))
                    if key != 'percentage':
                        if key == 'sum': recordCount += 1
                        else : sumContent[key] += value
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
        for i, (key, value) in enumerate(sumContent.items()):
            lineSeries.append(QPoint(i, value/recordCount))
        chart.addSeries(lineSeries)
        lineSeries.attachAxis(axisX)
        lineSeries.attachAxis(axisY)
        pen = lineSeries.pen()
        pen.setWidth(4)
        lineSeries.setPen(pen)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        
        self.layout.addWidget(chartView)

    # @QtCore.pyqtSlot(dict)
    # def create_linechart(self, Doc):
    #     if Doc['transcription']['analysis'] == None:
    #         return
    #     self.clearlayout()
    #     caseDocs = database.DBapi.findDocsByCaseID(Doc['childData']['caseID'])
    #     caseDocs = list(caseDocs)
        
    #     chart =  QChart()
    #     chart.setTitle("個案" + Doc['childData']['caseID'] + "就診紀錄")
    #     font = QtGui.QFont()
    #     font.setPixelSize(24)
    #     chart.setTitleFont(font)
        
    #     categories = ["名詞", "動詞", "形容詞", "數詞", "量詞", "代詞", "副詞"]
    #     axisX = QBarCategoryAxis()
    #     axisX.append(categories)
    #     chart.addAxis(axisX, Qt.AlignBottom)
    #     axisY = QValueAxis()
    #     chart.addAxis(axisY, Qt.AlignLeft)

    #     for index in caseDocs:
    #         if index['transcription']['analysis'] != None:
    #             series = QLineSeries(self)
    #             strDate = index['recording']['date'].strftime("%Y-%m-%d %H:%M:%S")
    #             series.setName(strDate)
    #             series.append(QPoint(0, index['transcription']['analysis']['Content']['N']))
    #             series.append(QPoint(1, index['transcription']['analysis']['Content']['V']))
    #             series.append(QPoint(2, index['transcription']['analysis']['Content']['VH']))
    #             series.append(QPoint(3, index['transcription']['analysis']['Content']['Neu']))
    #             series.append(QPoint(4, index['transcription']['analysis']['Content']['Nf']))
    #             series.append(QPoint(5, index['transcription']['analysis']['Content']['Nh']))
    #             series.append(QPoint(6, index['transcription']['analysis']['Content']['D']))
    #             chart.addSeries(series)
    #             series.attachAxis(axisX)
    #             series.attachAxis(axisY)
    #     axisY.setRange(0, 20)
    #     axisX.setRange("名詞", "副詞")
    #     axisY.setTitleText("詞的個數")
    #     axisY.setTitleFont(font)
    #     chart.legend().setVisible(True)
    #     chart.legend().setAlignment(Qt.AlignBottom)

    #     chartView = QChartView(chart)
    #     chartView.setRenderHint(QPainter.Antialiasing)
        
    #     self.layout.addWidget(chartView)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen = chartTab()
    screen.show()
    sys.exit(app.exec_())
