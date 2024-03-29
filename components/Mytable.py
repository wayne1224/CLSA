# 把第一第二格綁在一起
from typing import Collection, List
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import re
import os
# import prettytable as pt
import csv
from functools import partial
from collections import OrderedDict

class Mytable(QtWidgets.QWidget):
    procChange = QtCore.pyqtSignal()
    procInsertRow_editAdultID_setColor = QtCore.pyqtSignal()
    procAllID = QtCore.pyqtSignal(dict)

    def __init__(self):
        super(Mytable, self).__init__()
        
        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)

        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        
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
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setFont(font)
        self.tableWidget.setFont(font)

        # column size
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)

        # 轉碼
        self.retranslateUi()

        # 設成人編號
        self.tableWidget.cellClicked['int','int'].connect(self._setAdultID)
        
        # 防違法動作
        self.tableWidget.cellClicked['int','int'].connect(self._checkAll)

        # trigger mouse event
        self.tableWidget.viewport().installEventFilter(self)
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)

        # 紀錄上次編輯的格子
        self.id_x = -1
        self.last_x = -1
        self.edit = True

        self.childID = 0
        self.adultID = {}
        
        # self.setStyleSheet(open("C:/Users/HAO/Desktop/Code/Python/CLSA/QSS/Mytable.qss", "r").read())
        self.setStyleSheet(open("QSS/Mytable.qss", "r").read())

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

    # 從Tab2接收AdultID
    @QtCore.pyqtSlot(dict)
    def getAdultID(self, adultID):
        self.adultID = adultID
        sorted(self.adultID)

    # 傳兒童、成人編號給Tab2
    @QtCore.pyqtSlot()
    def emitAllID(self, IDDict):
        self.procAllID.emit(IDDict)
                
    def _checkAll(self):
        selected = self.tableWidget.selectedIndexes()
        try:
            x = selected[0].row()
            y = selected[0].column()
        except:
            pass

        for i in range(self.tableWidget.rowCount()):
            self.checkAllID()

            if ((self.tableWidget.item(i,0) == None or self.tableWidget.item(i,0).text() == '') and
                (self.tableWidget.item(i,1) != None and self.tableWidget.item(i,1).text() != '')):
                if self.tableWidget.item(i,1).font().bold() == False:
                    if y != 0:
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                        msgBox.setText("需要成人編號!!!")
                        msgBox.setWindowTitle("Warning")
                        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                        msgBox.exec()
                        self.tableWidget.setCurrentCell(i,0)
                        return False

            if (((self.tableWidget.item(i,1) == None or self.tableWidget.item(i,1).text() == '') or
                (self.tableWidget.item(i,1) != None and self.tableWidget.item(i,1).font().bold())) and
                (self.tableWidget.item(i,0) != None and self.tableWidget.item(i,0).text() != '')):
                    if y != 1:
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                        msgBox.setText("需要成人語句!!!")
                        msgBox.setWindowTitle("Warning")
                        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                        msgBox.exec()
                        self.tableWidget.setCurrentCell(i,1)
                        return False

            if (((self.tableWidget.item(i,4) == None or self.tableWidget.item(i,4).text() == '') or
                (self.tableWidget.item(i,4) != None and self.tableWidget.item(i,4).font().bold())) and
                (self.tableWidget.item(i,3) != None and self.tableWidget.item(i,3).text() != '')):
                    if y != 4:
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                        msgBox.setText("需要兒童語句!!!")
                        msgBox.setWindowTitle("Warning")
                        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                        msgBox.exec()
                        self.tableWidget.setCurrentCell(i,1)
                        return False

            if (((self.tableWidget.item(i,0) != None and self.tableWidget.item(i,0).text() != '') or
                (self.tableWidget.item(i,1) != None and self.tableWidget.item(i,1).text() != '')) and
                (x == i) and (y == 3 or y == 4)):
                msgBox = QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                msgBox.setText("成人和孩童語句不能同時出現")
                msgBox.setWindowTitle("Warning")
                msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msgBox.exec()
                return False

            if ((self.tableWidget.item(i,4) != None and self.tableWidget.item(i,4).text() != '') and
                (x == i) and (y == 0 or y == 1)):
                msgBox = QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                msgBox.setText("成人和孩童語句不能同時出現")
                msgBox.setWindowTitle("Warning")
                msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msgBox.exec()
                return False

        self.checkAllID()
        return True


    def _setAdultID(self):
        selected = self.tableWidget.selectedIndexes()
        x = selected[0].row()
        y = selected[0].column()

        # 將ComboBox編號存成一般儲存格
        if self.id_x != -1 and self.tableWidget.cellWidget(self.id_x,0) != None:
            num = self.tableWidget.cellWidget(self.id_x,0).currentText()
            self.tableWidget.removeCellWidget(self.id_x,0)
            item = QtWidgets.QTableWidgetItem()
            item.setText(num)
            self.tableWidget.setItem(self.id_x,0,item)
            self.id_x = -1
            self.procInsertRow_editAdultID_setColor.emit()

        # 設成人編號的Dict
        idDict = self.adultID

        # 初始化ComboBox
        if y == 0:
            # if self.edit:
            idBox = QtWidgets.QComboBox()
            idBox.setEditable(True)

            # 若成人語句不採計，無法設成人編號
            if self.tableWidget.item(x,1) and self.tableWidget.item(x,1).font().bold():
                idBox.setEnabled(False)

            opts = list(idDict)
            idBox.addItems(opts)
            idBox.clearEditText()

            # 檢查原格中是否有字
            if self.tableWidget.item(x,0) and self.tableWidget.item(x,0).text() != '':
                t = self.tableWidget.item(x,0).text()
                idBox.setCurrentText(t)
                
            self.tableWidget.setCellWidget(x, y, idBox)
            self.id_x = x
            # self.last_x = x

    def checkAllID(self):
        checkChildID = 0
        checkAdultID = {}
        empty = QtWidgets.QTableWidgetItem('')

        for rowIndex in range(self.tableWidget.rowCount()):
            adultID = self.tableWidget.item(rowIndex, 0)
            adultUtter = self.tableWidget.item(rowIndex,1)
            childID = self.tableWidget.item(rowIndex,3)
            childUtter = self.tableWidget.item(rowIndex,4)

            # 阻擋使用者強行輸入
            if((childID != None and childID.text() != '' and childUtter != None and childUtter.text() != '') or
                childUtter.font().bold()):
                adultID.setText('')
                adultUtter.setText('')
            if((adultID != None and adultID.text() != '' and adultUtter != None and adultUtter.text() != '') or
                adultUtter.font().bold()):
                childID.setText('')
                childUtter.setText('')

            # 成人語句
            if adultUtter != None and adultUtter.text() != '' and not adultUtter.font().bold():
                if adultID == None:
                    self.tableWidget.setItem(rowIndex, 0, empty)
                    adultID = self.tableWidget.item(rowIndex, 0)
                if self.tableWidget.item(rowIndex,0).text() != '':
                    try:
                        pattern = r"[a-zA-Z]+"   
                        key = re.search(pattern,adultID.text()).group()
                        if key in checkAdultID:
                            checkAdultID[key] += 1
                        else:
                            checkAdultID[key] = 1
                        ID = key + str(checkAdultID[key])
                        adultID.setText(ID)
                    except Exception as e:
                        informBox = QtWidgets.QMessageBox.warning(self, '警告','編號只能輸入英文', QtWidgets.QMessageBox.Ok)
                        self.tableWidget.setItem(rowIndex,0,empty)
            # 兒童語句
            if childUtter != None and childUtter.text() != '' and not childUtter.font().bold():
                checkChildID += 1
                if childID == None:
                    self.tableWidget.setItem(rowIndex, 3, empty)
                    childID = self.tableWidget.item(rowIndex,3)
                childID.setText(str(checkChildID))

        self.childID = checkChildID
        self.adultID = OrderedDict(sorted(checkAdultID.items()))
        
        IDDict = {'childID':self.childID, 'adultID':self.adultID}
        self.emitAllID(IDDict)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.RightButton:
                index = self.tableWidget.indexAt(event.pos())
                if index.isValid():
                    item = self.tableWidget.itemFromIndex(index)
                    if item is not None:
                        self.menu = QtWidgets.QMenu(self)

                        # 插入選項
                        self.insert = QtWidgets.QMenu('插入', self)
                        self.insertUp = QtWidgets.QAction('向上插入一列')
                        self.insertUp.triggered.connect(partial(self.insertRow,index,'up'))
                        self.insert.addAction(self.insertUp)
                        self.insertDown = QtWidgets.QAction('向下插入一列')
                        self.insertDown.triggered.connect(partial(self.insertRow,index,'down'))
                        self.insert.addAction(self.insertDown)
                        self.menu.addMenu(self.insert)

                        if item.text():
                            # 是否採計
                            f = item.font()
                            if index.column() != 2:
                                if f.bold():
                                    self.setValid = QtWidgets.QAction('採計')
                                    self.setValid.setObjectName("setValid")
                                    self.setValid.triggered.connect(partial(self.toValid,f,item,index))
                                    self.menu.addAction(self.setValid)
                                else:
                                    self.setNotValid = QtWidgets.QAction('不採計')
                                    self.setNotValid.setObjectName("setNotValid")
                                    self.setNotValid.triggered.connect(partial(self.toNotValid,f,item,index))
                                    self.menu.addAction(self.setNotValid)
                            
                            # 兒童、成人語句轉換
                            if index.column() == 1:
                                self.toChild = QtWidgets.QAction('轉成兒童語句')
                                self.toChild.setObjectName("toChild")
                                if f.bold():    # 不採計的語句轉換
                                    self.toChild.triggered.connect(partial(self.changeRole,item,index,None,False))
                                else:           # 採計的語句轉換
                                    self.toChild.triggered.connect(partial(self.changeRole,item,index,None,True))
                                self.menu.addAction(self.toChild)
                            elif index.column() == 4:
                                if f.bold():    # 不採計的語句轉換
                                    self.toAdultNotValid = QtWidgets.QAction('轉成成人語句')
                                    self.toAdultNotValid.setObjectName("toAdultNotValid")
                                    self.toAdultNotValid.triggered.connect(partial(self.changeRole,item,index,'',False))
                                    self.menu.addAction(self.toAdultNotValid)
                                else:           # 採計的語句轉換
                                    self.toAdult = QtWidgets.QMenu('轉成成人語句', self)
                                    self.toAdult.setObjectName("toAdult")
                                    # 已有的成人編號
                                    self.oldID = []
                                    for ID in self.adultID.keys():
                                        self.temp = QtWidgets.QAction(ID)
                                        self.oldID.append(self.temp)
                                        self.oldID[len(self.oldID)-1].triggered.connect(partial(self.changeRole,item,index,ID,True))
                                        self.toAdult.addAction(self.oldID[len(self.oldID)-1])
                                    # 新增編號輸入欄
                                    self.inputID = QtWidgets.QLineEdit()
                                    self.inputID.setPlaceholderText('新增編號')
                                    self.inputID.setMaximumWidth(70)
                                    self.addID = QtWidgets.QWidgetAction(self)
                                    self.addID.setDefaultWidget(self.inputID)
                                    self.toAdult.addAction(self.addID)
                                    # 確認按鈕
                                    self.btnConfirmID = QtWidgets.QPushButton('確認')
                                    self.btnConfirmID.setMaximumWidth(70)
                                    self.btnConfirmID.clicked.connect(partial(self.addNewID,item,index))
                                    self.confirmID = QtWidgets.QWidgetAction(self)
                                    self.confirmID.setDefaultWidget(self.btnConfirmID)
                                    self.toAdult.addAction(self.confirmID)
                                    # 將子menu加入原本的menu裡
                                    self.menu.addMenu(self.toAdult)

                        self.menu.exec_(event.globalPos())

        return super(Mytable,self).eventFilter(source, event)

    def toValid(self,f,item,index):
        f.setBold(False)
        item.setFont(f)
        if index.column() == 1:
            self.tableWidget.item(index.row(), 0).setSelected(True)
        if index.column() == 4:
            self.checkAllID()

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
        self.checkAllID()
    
    def insertRow(self,index,opt):
        if opt == 'up':
            row = index.row()
        if opt == 'down':
            row = index.row()+1
        self.tableWidget.insertRow(row)
        for columnIndex in range(5):
            if self.tableWidget.item(row, columnIndex) == None:
                self.tableWidget.setItem(row, columnIndex, QtWidgets.QTableWidgetItem(''))
        # Tab2加上顏色
        self.procInsertRow_editAdultID_setColor.emit()

    def addNewID(self, item, index):
        if self.inputID.text() != '':
            if self.inputID.text().encode( 'UTF-8' ).isalpha():
                try:
                    pattern = r"[a-zA-Z]+"   
                    key = re.search(pattern,self.inputID.text()).group()
                    self.changeRole(item, index, self.inputID.text(), True)
                except Exception as e:
                    print(e)
                    informBox = QtWidgets.QMessageBox.warning(self, '警告','編號只能輸入英文', QtWidgets.QMessageBox.Ok)
            else:
                informBox = QtWidgets.QMessageBox.warning(self, '警告','編號只能輸入英文', QtWidgets.QMessageBox.Ok)

    def changeRole(self, item, index, ID, isValid):
        itemCopy = QtWidgets.QTableWidgetItem(item.text())
        item.setText('')
        tempFont = QtGui.QFont()
        tempFont.setBold(False)
        item.setFont(tempFont)
        # 如果轉換的語句不採計
        if not isValid:
            f = QtGui.QFont()
            f.setBold(True)
            itemCopy.setFont(f)
        # toChild
        if ID == None:
            self.tableWidget.setItem(index.row(), 4, itemCopy)
            if self.tableWidget.item(index.row(), 0) != None:
                self.tableWidget.item(index.row(), 0).setText("")
        # toAdult
        else:
            self.tableWidget.setItem(index.row(), 1, itemCopy)
            if self.tableWidget.item(index.row(), 3) != None:
                self.tableWidget.item(index.row(), 3).setText("")
            if self.tableWidget.item(index.row(), 0) == None:
                self.tableWidget.setItem(index.row(), 0, QtWidgets.QTableWidgetItem(ID))
            else:
                self.tableWidget.item(index.row(), 0).setText(ID)
        self.checkAllID()
        # Tab2同時更新
        self.procChange.emit()

    def generateMenu(self, pos):
        self.menu.exec_(self.tableWidget.mapToGlobal(pos))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen = Mytable()
    screen.show()
    sys.exit(app.exec_())