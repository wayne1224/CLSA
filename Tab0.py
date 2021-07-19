# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tab0.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import database.DatabaseApi
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from datetime import datetime

class SearchTab(QtWidgets.QWidget):
    #用來傳Document到各頁
    procDoc = QtCore.pyqtSignal(dict)
    procMain = QtCore.pyqtSignal(int)
    procFind = QtCore.pyqtSignal()

    def __init__(self):
        super(SearchTab, self).__init__()
        font = QtGui.QFont()
        font.setPointSize(14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        #Form.setFont(font)
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.input_SLP = QtWidgets.QLineEdit()
        self.input_SLP.setObjectName("input_SLP")
        self.input_SLP.setSizePolicy(sizePolicy)
        self.input_SLP.setFont(font)
        self.horizontalLayout.addWidget(self.input_SLP)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.input_caseID = QtWidgets.QLineEdit()
        self.input_caseID.setObjectName("input_caseID")
        self.input_caseID.setSizePolicy(sizePolicy)
        self.input_caseID.setFont(font)
        self.horizontalLayout_2.addWidget(self.input_caseID)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.input_Name = QtWidgets.QLineEdit()
        self.input_Name.setObjectName("input_Name")
        self.input_Name.setSizePolicy(sizePolicy)
        self.input_Name.setFont(font)
        self.horizontalLayout_3.addWidget(self.input_Name)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.searchBtn = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(14)
        self.searchBtn.setFont(font)
        self.searchBtn.setObjectName("searchBtn")
        self.searchBtn.clicked.connect(self._search)
        self.searchBtn.setToolTip('若輸入皆為空白，可查詢所有個案')
        self.horizontalLayout_4.addWidget(self.searchBtn)
        self.horizontalLayout_4.addItem(spacerItem)

        layout.addLayout(self.horizontalLayout_4)
        
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        layout.addItem(spacerItem)

        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(8, QtWidgets.QHeaderView.Stretch)

        layout.addWidget(self.tableWidget)
        self.retranslateUi()

        #QSS
        
        self.setStyleSheet(open("C:/Users/HAO/Desktop/Code/Python/CLSA/QSS/Tab0.qss", "r").read())
        # self.setStyleSheet(open("QSS/Tab0.qss", "r").read())

    def _search(self):
        self.procFind.emit()
        cursor = database.DatabaseApi.findDocs(self.input_SLP.text() , self.input_caseID.text() , self.input_Name.text())

        # self.tableWidget.clear()
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(self.tableWidget.rowCount()-1)

        if cursor:
            for idx, doc in enumerate(cursor):
                self.tableWidget.insertRow(idx)        
                
                item = QtWidgets.QTableWidgetItem()
                item.setText(doc['recording']['SLP'])
                self.tableWidget.setItem(idx , 0 , item)

                item = QtWidgets.QTableWidgetItem()
                item.setText(doc['childData']['caseID'])
                self.tableWidget.setItem(idx , 1 , item)

                item = QtWidgets.QTableWidgetItem()
                item.setText(doc['childData']['name'])
                self.tableWidget.setItem(idx , 2 , item)

                item = QtWidgets.QTableWidgetItem()
                time = datetime.strftime(doc['recording']['date'],'%Y-%m-%d %H:%M')
                item.setText(time)
                self.tableWidget.setItem(idx , 3 , item)
                
                item = QtWidgets.QTableWidgetItem()
                item.setText(doc['recording']['scenario'])
                self.tableWidget.setItem(idx , 4 , item)
                
                item = QtWidgets.QTableWidgetItem()
                item.setText(doc['recording']['location'])
                self.tableWidget.setItem(idx , 5 , item)

                item = QtWidgets.QTableWidgetItem()
                item.setText(doc['recording']['inducement'])
                self.tableWidget.setItem(idx , 6 , item)
        
                importBtn = QtWidgets.QPushButton('匯入')
                deleteBtn = QtWidgets.QPushButton('刪除')
                importBtn.setStyleSheet("QPushButton {background-color: sandybrown;} QPushButton:hover {background-color: rgb(226, 149, 82);}")
                deleteBtn.setStyleSheet("QPushButton {background-color: rgb(235, 38, 78);} QPushButton:hover {background-color: rgb(219, 26, 65);}")
                self.tableWidget.setCellWidget(idx,7,importBtn)
                self.tableWidget.setCellWidget(idx,8,deleteBtn)
                importBtn.clicked.connect(partial(self.importDoc , doc))
                deleteBtn.clicked.connect(partial(self.deleteDoc , doc['documentObjID'] , idx)) # 只刪document
        else:
            informBox = QtWidgets.QMessageBox.information(self, '查詢','查無資料', QtWidgets.QMessageBox.Ok)

    @QtCore.pyqtSlot()
    def importDoc(self , obj):
        self.procDoc.emit(obj)
        #通知彙整完整
        informBox = QtWidgets.QMessageBox.information(self, '通知','匯入完成', QtWidgets.QMessageBox.Ok)
        self.procMain.emit(1)
        

    def deleteDoc(self , objID , idx):
        delete = QtWidgets.QMessageBox.warning(self,
                            "CLSA",
                            '<p style="font-size:13pt; color: red;">確定要刪除此資料嗎?</p>',
                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        if delete == QtWidgets.QMessageBox.Yes:
            if database.DatabaseApi.deleteDoc(objID):
                self.tableWidget.removeRow(idx)
                informBox = QtWidgets.QMessageBox.information(self, '成功','成功刪除個案', QtWidgets.QMessageBox.Ok)
            else:
                informBox = QtWidgets.QMessageBox.critical(self, '失敗','刪除個案失敗', QtWidgets.QMessageBox.Ok)
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        # Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "收錄者："))
        self.label_2.setText(_translate("Form", "個案編號："))
        self.label_3.setText(_translate("Form", "個案姓名："))
        self.searchBtn.setText(_translate("Form", "    查詢    "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "收錄者"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "個案編號"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "個案姓名"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "收錄日期"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "收錄情境"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "收錄地點"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "誘發題材"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen = SearchTab()
    screen.show()
    sys.exit(app.exec_())
