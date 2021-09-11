import database.DatabaseApi as db
import qtawesome as qta
from datetime import date
from functools import partial
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QBarSeries, QLineSeries, QChartView, QPieSeries, QPieSlice, QBarSet, QPercentBarSeries, QBarCategoryAxis, QValueAxis
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import QPoint, Qt, QPointF
from components.statChart import statChartTab, createBarChart_POS, createLineChart
from components.norm import NormModifyTab

class Tab4(QtWidgets.QTabWidget):
    def __init__(self):
        super(Tab4, self).__init__()
        self.tab0 = chartTab()
        self.tab1 = statChartTab()
        self.tab2 = NormModifyTab()

        self.addTab(self.tab0, "個案分析圖表")
        self.addTab(self.tab1, "各年齡層分析圖表")
        tab3 = self.addTab(self.tab2, "常模設定頁面")
        self.setTabIcon(tab3, qta.icon('fa.gear'))

        #self.tab0.procCaseDocs.connect(self.tab1.lineChart)
        self.setStyleSheet(open("QSS/Tab4.qss", "r").read())

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

        # table font
        tfont = QtGui.QFont()
        tfont.setFamily("微軟正黑體")
        tfont.setPointSize(10)

        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 180))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)

        #change font
        self.tableWidget.horizontalHeader().setFont(tfont)
        self.tableWidget.setFont(tfont)

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
        font.setFamily("微軟正黑體")
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
        
    def search(self):
        #移除提示
        self.form.remindText.setHidden(True)
        self.form.icon.setHidden(True)

        cursor = db.findChildren(self.form.input_caseID.text() , self.form.input_name.text())
        # print(self.form.input_caseID.text(),self.form.input_name.text())
    
        while self.form.tableWidget.rowCount() > 0:
            self.form.tableWidget.removeRow(self.form.tableWidget.rowCount()-1)

        if cursor:
            idx = -1
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
                importBtn.clicked.connect(partial(self.create_linebarchart , child['document'], child['name']))
            if idx == -1:
                QtWidgets.QMessageBox.information(self, '查詢','查無資料', QtWidgets.QMessageBox.Ok)

        else:
            QtWidgets.QMessageBox.information(self, 'Database','資料庫讀取中', QtWidgets.QMessageBox.Ok)

    # #清除原本layout裡的Widget
    # def clearLayout(self):
    #     if self.scroll_vbox.count() > 0:
    #         self.POS_chart.hide()
    #         self.VOCD_chart.hide()
    #         self.MLU_chart.hide()
    #         #self.hintArea.hide()
    #     try:
    #         for i in reversed(range(self.scroll_vbox.count())):
    #             #print(self.scroll_vbox.itemAt(i))
    #             #self.scroll_vbox.removeItem(self.scroll_vbox.itemAt(i))
    #             if self.scroll_vbox.itemAt(i).layout():
    #                 for x in reversed(range(self.scroll_vbox.itemAt(i).layout().count())):
    #                     if self.scroll_vbox.itemAt(i).layout().itemAt(x).layout():
    #                         self.scroll_vbox.itemAt(i).layout().itemAt(x).layout().deleteLater()
    #                         self.scroll_vbox.itemAt(i).layout().removeItem(self.scroll_vbox.itemAt(i).layout().itemAt(x))

    #                 self.scroll_vbox.itemAt(i).layout().deleteLater()
    #                 self.scroll_vbox.removeItem(self.scroll_vbox.itemAt(i))
                    
    #             elif self.scroll_vbox.itemAt(i).widget():
    #                 self.scroll_vbox.itemAt(i).widget().deleteLater()
    #                 self.scroll_vbox.removeItem(self.scroll_vbox.itemAt(i))
    #     except Exception as e:
    #         print(e)
    def clearLayout(self, layout):
        try:
            while(layout.count() > 0):
                child = layout.takeAt(0)
                print(child)
                if child.layout():
                    self.clearLayout(child)
                elif isinstance(child, QtWidgets.QSpacerItem):
                    pass
                elif isinstance(child, QtWidgets.QWidgetItem):
                    child.widget().deleteLater()
        except Exception as e:
            print(e)

    def create_linebarchart(self, doc, name):
        #檢查是否轉錄過
        count = 0
        tempDoc = doc.copy()
        for b in tempDoc:
            if b['transcription']['analysis'] != None:
                count += 1

        #尚未轉錄過無法生成資料
        #self.clearLayout()
        if count == 0:
            QtWidgets.QMessageBox.information(self, '','尚未彙整過無法生成資料', QtWidgets.QMessageBox.Ok)
            return None
        
        # #清除所有Layout
        self.clearLayout(self.scroll_vbox)

        #詞性圖
        self.POS_chart = createBarChart_POS(doc.copy(), name)
        self.scroll_vbox.addWidget(self.POS_chart)

        #VOCD/MLU圖
        
        self.chartLayout = QtWidgets.QHBoxLayout()
        self.MLU_chart, len_mlu = createLineChart("MLU", doc.copy())
        self.VOCD_chart, len_vocd, invalid_dates = createLineChart("VOCD", doc.copy())
        self.chartLayout.addWidget(self.VOCD_chart)
        self.chartLayout.addWidget(self.MLU_chart)
        self.scroll_vbox.addLayout(self.chartLayout)
        
        if len_mlu > len_vocd and len_vocd == 0:
            self.VOCD_chart.hide()
            warnText = "資料過少無法產生VOCD圖表"
            self.createWarnLabel(warnText,two_graph=False)
            QtWidgets.QMessageBox.warning(self, "通知",warnText, QtWidgets.QMessageBox.Ok)
        elif len_mlu > len_vocd and len_vocd > 0:
            warnText = f"VOCD圖表有{len_mlu-len_vocd}筆紀錄因資料過少無法呈現於圖表"
            self.createWarnLabel(warnText)
            for d in invalid_dates:
                warnText += f"\n{d}"
            QtWidgets.QMessageBox.warning(self, "通知", warnText, QtWidgets.QMessageBox.Ok)

        self.layout.addWidget(self.scroll)
        

    def createWarnLabel(self, warnText, two_graph=True):
        #Font
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)

        # Hint Widget Under Graphs
        graph_hint_icon = QtWidgets.QLabel()
        graph_hint_icon.setPixmap(qta.icon('fa.info-circle',color='#eed202').pixmap(QtCore.QSize(25, 25)))
        graph_hint_icon.setMaximumSize(QtCore.QSize(30, 30))
        graph_hint_text = QtWidgets.QLabel(warnText) #"樣本數不足無法產生圖表"
        graph_hint_text.setMaximumSize(QtCore.QSize(16777215, 30))
        graph_hint_text.setFont(font)
        spacer = QtWidgets.QSpacerItem(40,20, QtWidgets.QSizePolicy.Expanding)

        self.remindHbox = QtWidgets.QHBoxLayout() #最外層HBOX
        leftHbox = QtWidgets.QHBoxLayout()
        leftHbox.addWidget(QtWidgets.QLabel(""))
        leftHbox.addWidget(graph_hint_icon)
        leftHbox.addWidget(graph_hint_text)
        leftHbox.addWidget(QtWidgets.QLabel(""))
        self.remindHbox.addLayout(leftHbox)

        
        #self.remindHbox.addWidget(QtWidgets.QLabel())
        #self.remindHbox.addItem(spacer)

        if two_graph:
            rightHbox = QtWidgets.QHBoxLayout()
            rightHbox.addWidget(QtWidgets.QLabel(" "))
            self.remindHbox.addLayout(rightHbox)

        self.scroll_vbox.addLayout(self.remindHbox)