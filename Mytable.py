#把第一第二格綁在一起
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import re
import os
# import prettytable as pt
import csv
from functools import partial

class Mytable(QtWidgets.QWidget):
    #keyboard key
    keyPressed = QtCore.pyqtSignal(QtCore.QEvent)
    def __init__(self):
        super(Mytable, self).__init__()
        #QtWidgets.QWidget.__init__(self)
        '''
        Todo: 自訂table位置和大小
        self.setGeometry(300, 300, 250, 150) 
        '''
        #trigger keyboard key
        self.keyPressed.connect(self.on_key)

        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)
        
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        layout.addWidget(self.tableWidget, 0, 0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        #column size
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)

        #轉碼
        self.retranslateUi()
        #set column width
        # self.tableWidget.setColumnWidth(0,100)
        # self.tableWidget.setColumnWidth(1,300)
        # self.tableWidget.setColumnWidth(2,300)
        # self.tableWidget.setColumnWidth(3,50)
        # self.tableWidget.setColumnWidth(4,350)

        #觸發孩童編號
        self.tableWidget.cellClicked['int','int'].connect(self._setChildID)

        #設成人編號
        self.tableWidget.cellClicked['int','int'].connect(self._setAdultID)
        
        #防無編號或無語句
        self.tableWidget.cellClicked['int','int'].connect(self._checkAdultClick)

        #防無編號
        #self.tableWidget.cellClicked['int','int'].connect(self._checkAdultUtter)

        #防多餘孩童編號
        self.tableWidget.cellClicked['int','int'].connect(self._checkChildID)

        

        #trigger mouse event
        self.tableWidget.viewport().installEventFilter(self)
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)

        #紀錄上次編輯的格子
        self.id_x = -1
        self.last_x = -1
        self.edit = True

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget.verticalHeaderItem(0)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "成人編號"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "成人語句"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "語境"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "兒童編號"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "兒童語句"))

    def keyPressEvent(self, event):
        super(Mytable, self).keyPressEvent(event)
        self.keyPressed.emit(event) 

    def on_key(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self._addRow()
    
    def _addRow(self):
        if self._checkAdult():
            row_count = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_count)
            self.tableWidget.scrollToBottom()

    # def _checkAdultUtter(self):
    #     #被選到的格子
    #     selected = self.tableWidget.selectedIndexes()
    #     x = selected[0].row()
    #     y = selected[0].column()

    #     print(self.last_x)
    #     if ((self.last_x != -1) and
    #         (x != self.last_x or y > 1) and #限定範圍
    #         (self.tableWidget.item(self.last_x,0) and self.tableWidget.item(self.last_x,0).text() != '') and #若有編號
    #         (self.tableWidget.item(self.last_x,1) is None or self.tableWidget.item(self.last_x,1).text() == '')): #若無語句
    #         msgBox = QtWidgets.QMessageBox()
    #         msgBox.setIcon(QtWidgets.QMessageBox.Warning)
    #         msgBox.setText("若有編號就應有語句!!!")
    #         msgBox.setWindowTitle("Warning")
    #         msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    #         msgBox.exec()
    #         self.tableWidget.setCurrentCell(self.last_x,1)
    #         self.edit = False

    #     elif ((self.last_x != -1 and (x != self.last_x or y > 1) and self.tableWidget.item(self.last_x,0) and self.tableWidget.item(self.last_x,0).text() != '') and
    #          (self.tableWidget.item(self.last_x,1).text() != '')): #若有語句
    #         self.last_x = -1
    #         self.edit = True

    # def _checkAdultID(self):
    #     #被選到的格子
    #     selected = self.tableWidget.selectedIndexes()
    #     x = selected[0].row()
    #     y = selected[0].column()

    #     if y == 1:
    #         if ((self.tableWidget.item(x,0) is None) or
    #             (self.tableWidget.item(x,0) and self.tableWidget.item(x,0).text() == '')):
    #             msgBox = QtWidgets.QMessageBox()
    #             msgBox.setIcon(QtWidgets.QMessageBox.Warning)
    #             msgBox.setText("請先輸入編號再輸入語句!!!")
    #             msgBox.setWindowTitle("Warning")
    #             msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    #             msgBox.exec()
    #             #self.tableWidget.setCurrentCell(x,0)
    #             return

    def _checkAdultClick(self):
        selected = self.tableWidget.selectedIndexes()
        x = selected[0].row()
        y = selected[0].column()
        print(self.last_x)
        if ((y == 0 or y == 1) and self.last_x == -1):
            self.last_x = x
        elif ((y == 0 or y == 1) and self.last_x == x):
            pass 
        elif self.last_x != -1:
            self._checkAdult()
                
    def _checkAdult(self):
        if ((self.tableWidget.item(self.last_x,0) == None or self.tableWidget.item(self.last_x,0).text() == '') and
            (self.tableWidget.item(self.last_x,1) and self.tableWidget.item(self.last_x,1).text() != '')):
            if self.tableWidget.item(self.last_x,1).font().bold() == False:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                msgBox.setText("需要成人編號!!!")
                msgBox.setWindowTitle("Warning")
                msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msgBox.exec()
                self.tableWidget.setCurrentCell(self.last_x,0)
                return False

        elif ((self.tableWidget.item(self.last_x,1) == None or self.tableWidget.item(self.last_x,1).text() == '') and
            (self.tableWidget.item(self.last_x,0) and self.tableWidget.item(self.last_x,0).text() != '')):
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            msgBox.setText("需要成人語句!!!")
            msgBox.setWindowTitle("Warning")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec()
            self.tableWidget.setCurrentCell(self.last_x,1)
            return False
        self.last_x = -1
        return True

    def _setAdultID(self):
        selected = self.tableWidget.selectedIndexes()
        x = selected[0].row()
        y = selected[0].column()

        #將ComboBox編號存成一般儲存格
        if self.id_x != -1:
            num = self.tableWidget.cellWidget(self.id_x,0).currentText()
            self.tableWidget.removeCellWidget(self.id_x,0)
            item = QtWidgets.QTableWidgetItem()
            item.setText(num)
            self.tableWidget.setItem(self.id_x,0,item)
            self.id_x = -1
                

            #設成人編號的Dict
        idDict = {}
        for i in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(i,0) and self.tableWidget.item(i,0).text() != '':
                pattern = r"[a-zA-Z]+"   
                key = re.search(pattern,self.tableWidget.item(i,0).text()).group()
                if key in idDict:
                    idDict[key] += 1
                else:
                    idDict[key] = 1
                key += str(idDict[key])
                item = QtWidgets.QTableWidgetItem()
                item.setText(key)
                self.tableWidget.setItem(i,0,item)

            #初始化ComboBox
        if y == 0 and self.edit:
            # if self.edit:
            idBox = QtWidgets.QComboBox()
            idBox.setEditable(True)

            #若成人語句不採計，無法設成人編號
            if self.tableWidget.item(x,1) and self.tableWidget.item(x,1).font().bold():
                idBox.setEnabled(False)

            opts = list(idDict)
            idBox.addItems(opts)
            idBox.clearEditText()

            #檢查原格中是否有字
            if self.tableWidget.item(x,0) and self.tableWidget.item(x,0).text() != '':
                t = self.tableWidget.item(x,0).text()
                idBox.setCurrentText(t)
                
            self.tableWidget.setCellWidget(x, y, idBox)
            self.id_x = x
            #self.last_x = x

            

    def _setChildID(self):
        #被選到的格子
        selected = self.tableWidget.selectedIndexes()
        x = selected[0].row()
        y = selected[0].column()

        if y == 4 and self.edit: #如果被選到的格子是兒童語句
            row_count = self.tableWidget.rowCount()
            num = 0
            for i in range(row_count): #數幾個格子是有字的
                if self.tableWidget.item(i,4) and self.tableWidget.item(i,4).font().bold():
                    self.tableWidget.item(i,3).setText('')
                elif self.tableWidget.item(i,4) and self.tableWidget.item(i,4).text() != '':
                    self.tableWidget.item(i,3).setText(str(num))
                    num += 1
                #清除沒文字的格子的編號
                elif self.tableWidget.item(i,4) and self.tableWidget.item(i,4).text() == '':
                    self.tableWidget.item(i,3).setText('')
                elif i == x:#正要寫
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(num))
                    self.tableWidget.setItem(i,3,item)
                    num += 1
                elif self.tableWidget.item(i,4) == None:
                    item = QtWidgets.QTableWidgetItem()
                    item.setText('')
                    self.tableWidget.setItem(i,3,item)
    
    def _checkChildID(self):
        #被選到的格子
        selected = self.tableWidget.selectedIndexes()
        # x = selected[0].row()
        y = selected[0].column()

        for i in range(self.tableWidget.rowCount()):
            if y != 4 and (self.tableWidget.item(i,4) == None or self.tableWidget.item(i,4).text() == ''):
                item = QtWidgets.QTableWidgetItem()
                item.setText('')
                self.tableWidget.setItem(i,3,item)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.RightButton:
                index = self.tableWidget.indexAt(event.pos())
                if index.isValid():
                    item = self.tableWidget.itemFromIndex(index)
                    if item is not None:
                        self.menu = QtWidgets.QMenu(self)
                        f = item.font()
                        if f.bold():
                            self.setValid = QtWidgets.QAction('採計')
                            self.setValid.setObjectName("setValid")
                            self.setValid.triggered.connect(partial(self.toValid,f,item))
                            self.menu.addAction(self.setValid)
                            self.menu.exec_(event.globalPos())
                            
                        else:
                            self.setNotValid = QtWidgets.QAction('不採計')
                            self.setNotValid.setObjectName("setNotValid")
                            self.setNotValid.triggered.connect(partial(self.toNotValid,f,item,index))
                            self.menu.addAction(self.setNotValid)
                            self.menu.exec_(event.globalPos())

        return super(Mytable,self).eventFilter(source, event)

    def toValid(self,f,item):
        f.setBold(False)
        item.setFont(f)

    def toNotValid(self,f,item,index):
        if index.column() == 1:
            if self.tableWidget.item(index.row(), 0):
                self.tableWidget.item(index.row(), 0).setText('')
            f.setBold(True)
            item.setFont(f)
        elif index.column() == 4:
            self.tableWidget.item(index.row(), 3).setText('') 
            f.setBold(True)
            item.setFont(f)
    
    def generateMenu(self, pos):
        self.menu.exec_(self.tableWidget.mapToGlobal(pos))
    '''
    Todo: 寫接資料的function
    def _addRow(self,adultID,adult,scenario,childID,child):
        row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_count)
        self.tableWidget.scrollToBottom()

        self.tableWidget.item(rowCount,0).setText()
        self.tableWidget.item(rowCount,1).setText()
        self.tableWidget.item(rowCount,2).setText()
        self.tableWidget.item(rowCount,3).setText()
        self.tableWidget.item(rowCount,4).setText()
    '''

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen = Mytable()
    screen.show()
    sys.exit(app.exec_())