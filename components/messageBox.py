from PyQt5 import QtCore, QtWidgets

class Table_MessageBox(QtWidgets.QMessageBox):
    def __init__(self, before=None, after=None): #Before, After: Dict型態
        QtWidgets.QMessageBox.__init__(self)
        #self.setSizeGripEnabled (True)

        a = "00757001"
        self.setWindowTitle("是否變更個案資料")
        # self.setIcon(self.Critical)
        # print(type(self.icon().))
        self.setText(f'個案編號: {a}')
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
        self.tableWidget.setRowCount(3)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #self.tableWidget.move(30,80)
        self.tableWidget.resize(0, 0)
        ## Horizon Headers
        item = QtWidgets.QTableWidgetItem("更改前")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem("更改後")
        self.tableWidget.setHorizontalHeaderItem(1, item)
        ##Vertical headers
        item = QtWidgets.QTableWidgetItem("姓名")
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem("性別")
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem("生日")
        self.tableWidget.setVerticalHeaderItem(2, item)
        
        self.layout().addWidget(self.tableWidget, 1, 0 ,1 ,3)

        currentClick = self.exec_()

        if currentClick==0 :
            print ('Accept')
        if currentClick==1 :
            print ('Reject')

        if before and after:
            item = QtWidgets.QTableWidgetItem()
            item.setText(before['name'])
            self.tableWidget.setItem(0, 0, item)
            item = QtWidgets.QTableWidgetItem()
            item.setText(before['gender'])
            self.tableWidget.setItem(1, 0, item)
            item = QtWidgets.QTableWidgetItem()
            item.setText(before['birthday'])
            self.tableWidget.setItem(2, 0, item)
            item = QtWidgets.QTableWidgetItem()
            item.setText(after['name'])
            self.tableWidget.setItem(0, 1, item)
            item = QtWidgets.QTableWidgetItem()
            item.setText(after['gender'])
            self.tableWidget.setItem(1, 1, item)
            item = QtWidgets.QTableWidgetItem()
            item.setText(after['birthday'])
            self.tableWidget.setItem(2, 1, item)

    def event(self, e):
        result = QtWidgets.QMessageBox.event(self, e)
        self.setMinimumWidth(0)
        self.setMaximumWidth(500)
        self.setMinimumHeight(0)
        self.setMaximumHeight(1000)
        self.resize(390, 300)
        return result

