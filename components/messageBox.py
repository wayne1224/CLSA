from PyQt5 import QtCore, QtWidgets
from datetime import datetime

class Table_MessageBox(QtWidgets.QMessageBox):
    def __init__(self): #Before, After: Dict型態
        QtWidgets.QMessageBox.__init__(self)
        #self.setSizeGripEnabled (True)

       
        self.setWindowTitle("是否變更個案資料")
        # self.setIcon(self.Critical)
        # print(type(self.icon().))
    
        self.addButton (
            QtWidgets.QPushButton('確認更改'), 
            QtWidgets.QMessageBox.YesRole
        )
        self.addButton(
            QtWidgets.QPushButton('放棄更改'), 
            QtWidgets.QMessageBox.NoRole
        )

        #先加入spacer
        # spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        # self.layout().addItem(spacerItem, 2, 0)

        #Table
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setColumnCount(2)
        #self.tableWidget.setRowCount(3)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #self.tableWidget.move(30,80)
        self.tableWidget.resize(0, 0)
        ## Horizon Headers
        item = QtWidgets.QTableWidgetItem("更改前")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem("更改後")
        self.tableWidget.setHorizontalHeaderItem(1, item)

        self.layout().addWidget(self.tableWidget, 1, 0 ,1 ,3)
        # if currentClick==0 :
        #     print ('Accept')
        # if currentClick==1 :
        #     print ('Reject')

        # self.exec_()

    def event(self, e):
        result = QtWidgets.QMessageBox.event(self, e)
        self.setMinimumWidth(0)
        self.setMaximumWidth(500)
        self.setMinimumHeight(0)
        self.setMaximumHeight(1000)
       # self.resize(390, 100)
        return result

    def execute(self, before, after):
        #Clear Table
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(self.tableWidget.rowCount()-1)

        #載入資料
        a = before['caseID']
        self.setText(f'個案編號: {a}')
        
        rowCount = 0
        if before and after:
            if before['name'] != after['name']:
                self.tableWidget.insertRow(rowCount)
                item = QtWidgets.QTableWidgetItem("姓名")
                self.tableWidget.setVerticalHeaderItem(rowCount, item)

                item = QtWidgets.QTableWidgetItem()
                item.setText(before['name'])
                self.tableWidget.setItem(rowCount, 0, item)
                item = QtWidgets.QTableWidgetItem()
                item.setText(after['name'])
                self.tableWidget.setItem(rowCount, 1, item)
                rowCount += 1

            if before['gender'] != after['gender']:
                self.tableWidget.insertRow(rowCount)
                item = QtWidgets.QTableWidgetItem("性別")
                self.tableWidget.setVerticalHeaderItem(rowCount, item)

                item = QtWidgets.QTableWidgetItem()
                item.setText("男" if before['gender'] == "male" else "女")
                self.tableWidget.setItem(rowCount, 0, item)
                item = QtWidgets.QTableWidgetItem()
                item.setText("男" if after['gender'] == "male" else "女")
                self.tableWidget.setItem(rowCount, 1, item)
                rowCount += 1

            if before['birthday'] != after['birthday']:
                self.tableWidget.insertRow(rowCount)
                item = QtWidgets.QTableWidgetItem("生日")
                self.tableWidget.setVerticalHeaderItem(rowCount, item)

                item = QtWidgets.QTableWidgetItem()
                item.setText(before["birthday"].strftime( "%Y-%m-%d"))
                self.tableWidget.setItem(rowCount, 0, item)
                item = QtWidgets.QTableWidgetItem()
                item.setText(after["birthday"].strftime( "%Y-%m-%d"))
                self.tableWidget.setItem(rowCount, 1, item)
                rowCount += 1

        ##調整Table大小
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        for i in range(rowCount):
            self.tableWidget.verticalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setMinimumSize(QtCore.QSize(350, 40*(rowCount + 1)))
    
        return self.exec_()
