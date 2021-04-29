# -*- coding: utf-8 -*-

#  implementation generated from reading ui file 'c:\Users\fuhan\Desktop\NLP\CLSA\Tab2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import database.DBapi
from Mytable import Mytable
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets


class Tab2(QtWidgets.QWidget):
    procUtterNum = QtCore.pyqtSignal(list)
    procChildUtter = QtCore.pyqtSignal(list)
    procKey = QtCore.pyqtSignal(dict)

    def __init__(self):
        super(Tab2, self).__init__()

        #self.setGeometry(QtCore.QRect(-1, 0, 1121, 801))

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lbl_trans = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_trans.sizePolicy().hasHeightForWidth())
        self.lbl_trans.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_trans.setFont(font)
        self.lbl_trans.setObjectName("lbl_trans")
        self.horizontalLayout.addWidget(self.lbl_trans)
        self.input_trans = QtWidgets.QLineEdit()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_trans.sizePolicy().hasHeightForWidth())
        self.input_trans.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_trans.setFont(font)
        self.input_trans.setObjectName("input_trans")
        self.horizontalLayout.addWidget(self.input_trans)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lbl_caseID = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_caseID.sizePolicy().hasHeightForWidth())
        self.lbl_caseID.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_caseID.setFont(font)
        self.lbl_caseID.setObjectName("lbl_caseID")
        self.horizontalLayout.addWidget(self.lbl_caseID)
        self.input_caseID = QtWidgets.QLineEdit()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_caseID.sizePolicy().hasHeightForWidth())
        self.input_caseID.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_caseID.setFont(font)
        self.input_caseID.setObjectName("input_caseID")
        self.horizontalLayout.addWidget(self.input_caseID)
        self.btn_searchCase = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_searchCase.setFont(font)
        self.btn_searchCase.setObjectName("btn_searchCase")
        self.horizontalLayout.addWidget(self.btn_searchCase)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        layout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        layout.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 7, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lbl_searchResult = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_searchResult.sizePolicy().hasHeightForWidth())
        self.lbl_searchResult.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_searchResult.setFont(font)
        self.lbl_searchResult.setText("")
        self.lbl_searchResult.setObjectName("lbl_searchResult")
        #self.verticalLayout_6.addWidget(self.lbl_searchResult)
        self.cmb_caseDates = QtWidgets.QComboBox()
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.cmb_caseDates.sizePolicy().hasHeightForWidth())
        #self.cmb_caseDates.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cmb_caseDates.setFont(font)
        self.cmb_caseDates.setObjectName("cmb_caseDates")
        #self.verticalLayout_6.addWidget(self.cmb_caseDates)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lbl_rolePrompt = QtWidgets.QLabel()
        self.lbl_rolePrompt.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lbl_rolePrompt.setObjectName("lbl_rolePrompt")
        self.verticalLayout_5.addWidget(self.lbl_rolePrompt)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_role = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_role.sizePolicy().hasHeightForWidth())
        self.lbl_role.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_role.setFont(font)
        self.lbl_role.setObjectName("lbl_role")
        self.horizontalLayout_3.addWidget(self.lbl_role)
        self.cmb_role = QtWidgets.QComboBox()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_role.sizePolicy().hasHeightForWidth())
        self.cmb_role.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cmb_role.setFont(font)
        self.cmb_role.setEditable(True)
        self.cmb_role.setObjectName("cmb_role")
        self.cmb_role.addItem("")
        self.cmb_role.addItem("")
        self.horizontalLayout_3.addWidget(self.cmb_role)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbl_utterance = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_utterance.sizePolicy().hasHeightForWidth())
        self.lbl_utterance.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_utterance.setFont(font)
        self.lbl_utterance.setObjectName("lbl_utterance")
        self.horizontalLayout_5.addWidget(self.lbl_utterance)
        self.input_utterance = QtWidgets.QTextEdit()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_utterance.sizePolicy().hasHeightForWidth())
        self.input_utterance.setSizePolicy(sizePolicy)
        self.input_utterance.setMinimumSize(QtCore.QSize(400, 40))
        self.input_utterance.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_utterance.setFont(font)
        self.input_utterance.setObjectName("input_utterance")
        self.horizontalLayout_5.addWidget(self.input_utterance)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbl_scenario = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_scenario.sizePolicy().hasHeightForWidth())
        self.lbl_scenario.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_scenario.setFont(font)
        self.lbl_scenario.setObjectName("lbl_scenario")
        self.horizontalLayout_6.addWidget(self.lbl_scenario)
        self.input_scenario = QtWidgets.QTextEdit()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_scenario.sizePolicy().hasHeightForWidth())
        self.input_scenario.setSizePolicy(sizePolicy)
        self.input_scenario.setMinimumSize(QtCore.QSize(400, 40))
        self.input_scenario.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_scenario.setFont(font)
        self.input_scenario.setObjectName("input_scenario")
        self.horizontalLayout_6.addWidget(self.input_scenario)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cbx_notCount = QtWidgets.QCheckBox()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbx_notCount.setFont(font)
        self.cbx_notCount.setObjectName("cbx_notCount")
        self.verticalLayout_4.addWidget(self.cbx_notCount)
        self.btn_add = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)
        self.btn_add.setMinimumSize(QtCore.QSize(101, 51))
        self.btn_add.setMaximumSize(QtCore.QSize(101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        self.verticalLayout_4.addWidget(self.btn_add)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = Mytable()
        Mytable.__init__(self.tableWidget)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.btn_delete = QtWidgets.QPushButton()
        self.btn_delete.setMinimumSize(QtCore.QSize(101, 51))
        self.btn_delete.setMaximumSize(QtCore.QSize(101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_delete.setFont(font)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout_4.addWidget(self.btn_delete)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.btn_save = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QtCore.QSize(101, 51))
        self.btn_save.setMaximumSize(QtCore.QSize(101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_save.setFont(font)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_4.addWidget(self.btn_save)
        self.btn_generateAndSave = QtWidgets.QPushButton()
        self.btn_generateAndSave.setMinimumSize(QtCore.QSize(0, 51))
        self.btn_generateAndSave.setMaximumSize(QtCore.QSize(16777215, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_generateAndSave.setFont(font)
        self.btn_generateAndSave.setObjectName("btn_generateAndSave")
        self.horizontalLayout_4.addWidget(self.btn_generateAndSave)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        layout.addLayout(self.verticalLayout)
        layout.setStretch(1, 1)
        layout.setStretch(2, 2)

        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName()

        #事件
        self.btn_add.clicked.connect(self._addRow)
        self.btn_delete.clicked.connect(self._deleteRow)
        self.btn_save.clicked.connect(self._save)
        self.btn_searchCase.clicked.connect(self._searchCase)
        self.btn_generateAndSave.clicked.connect(self._generateAndSave)
        self.cmb_caseDates.activated.connect(self._dateSearch)
        self.tableWidget.tableWidget.cellClicked.connect(self._syncTableCmbRoleNum)
        #self.tableWidget.tableWidget.cellChanged.connect(self._isEdit)

        self.caseID = ''    #個案編號
        self.caseData = {}  #個案紀錄
        self.childNum = 0   #兒童編號
        self.adultNums = {}  #成人編號
        self.childUtternace = []    #兒童語句
        self.checkFirstSearch = True    #檢查是不是第一次查詢
        self.isEdit = False #檢查內容有無編輯

        #未輸入語句提示視窗
        self.msg_noInp = QtWidgets.QMessageBox()
        self.msg_noInp.setWindowTitle("提示")
        self.msg_noInp.setText("請輸入語句！")
        self.msg_noInp.setIcon(QtWidgets.QMessageBox.Question)
        #成人、兒童同時輸入提示視窗
        self.msg_multiInp = QtWidgets.QMessageBox()
        self.msg_multiInp.setWindowTitle("提示")
        self.msg_multiInp.setText("成人與兒童語句不能同時輸入！")
        self.msg_multiInp.setIcon(QtWidgets.QMessageBox.Warning)
        #未輸入個案編號
        self.msg_noCaseID = QtWidgets.QMessageBox()
        self.msg_noCaseID.setWindowTitle("提示")
        self.msg_noCaseID.setText("未輸入個案編號！")
        self.msg_noCaseID.setIcon(QtWidgets.QMessageBox.Warning)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_trans.setText(_translate("", "轉錄者："))
        self.lbl_caseID.setText(_translate("", "個案編號："))
        self.btn_searchCase.setText(_translate("", "查詢"))
        #self.lbl_searchResult.setText(_translate("", "啥小啦幹"))
        self.lbl_rolePrompt.setText(_translate("", "成人請自行輸入編號 ex: A, B"))
        self.lbl_role.setText(_translate("", "編號："))
        self.cmb_role.setItemText(0, _translate("Form", "兒童"))
        self.cmb_role.setItemText(1, _translate("Form", "語境"))
        self.lbl_utterance.setText(_translate("", "語句："))
        self.lbl_scenario.setText(_translate("", "語境："))
        self.cbx_notCount.setText(_translate("", "此句不採計"))
        self.btn_add.setText(_translate("", "新增"))
        self.btn_delete.setText(_translate("", "刪除"))
        self.btn_save.setText(_translate("", "儲存"))
        self.btn_generateAndSave.setText(_translate("", "產生彙整表並儲存"))

    '''
    #從Tab1接收個案編號
    @QtCore.pyqtSlot(str)
    def setCaseID(self, caseID):
        self.input_caseID.setText(caseID)
        self.raise_()
    '''

    #傳總語句數和有效語句數給Tab1
    @QtCore.pyqtSlot()
    def emitUtterNum(self, utteranceNum):
        self.procUtterNum.emit(utteranceNum)

    #傳孩童語句給Tab3
    @QtCore.pyqtSlot()
    def emitChildUtter(self, utterance):
        self.procChildUtter.emit(utterance)
        
    #傳個案編號、日期給Tab3
    @QtCore.pyqtSlot()
    def emitKey(self, key):
        self.procKey.emit(key)

    #新增列
    def _addRow(self):
        utterance = QtWidgets.QTableWidgetItem(self.input_utterance.toPlainText())
        scenario = QtWidgets.QTableWidgetItem(self.input_scenario.toPlainText())

        if self.cmb_role.currentText() == "兒童":   #新增兒童語句
            if self.input_utterance.toPlainText():  #檢查有輸入句子
                rowCount = self.tableWidget.tableWidget.rowCount()    #取得目前總列數
                self.tableWidget.tableWidget.insertRow(rowCount)  #插入一列

                if not self.cbx_notCount.isChecked():   #此句採計
                    self.childNum += 1
                    role = QtWidgets.QTableWidgetItem(self.childNum.__str__())
                    self.tableWidget.tableWidget.setItem(rowCount, 3, role)
                else:   #不採計
                    role = QtWidgets.QTableWidgetItem('')
                    self.tableWidget.tableWidget.setItem(rowCount, 3, role)
                
                self.tableWidget.tableWidget.setItem(rowCount, 4, utterance)
                self.tableWidget.tableWidget.setItem(rowCount, 2, scenario)
                self.tableWidget.tableWidget.scrollToBottom() #新增完會保持置底

                #清空、復原輸入欄
                self.cmb_role.setCurrentIndex(0)
                self.input_utterance.clear()
                self.input_scenario.clear()
                self.cbx_notCount.setChecked(False)
                self.input_caseID.setStyleSheet("border: 1px solid initial;")
                self.input_utterance.setStyleSheet("border: 1px solid initial;")
            else:   #沒輸入句子
                self.msg_noInp.exec_()    #跳出提示視窗
                self.input_utterance.setStyleSheet("border: 1px solid red;")

        elif self.cmb_role.currentText() == "語境":   #只新增語境
            rowCount = self.tableWidget.tableWidget.rowCount()    #取得目前總列數
            self.tableWidget.tableWidget.insertRow(rowCount)  #插入一列
            self.tableWidget.tableWidget.setItem(rowCount, 2, scenario)
            self.tableWidget.tableWidget.scrollToBottom() #新增完會保持置底

            #清空、復原輸入欄
            self.cmb_role.setCurrentIndex(0)
            self.input_utterance.clear()
            self.input_scenario.clear()
            self.cbx_notCount.setChecked(False)
            self.input_caseID.setStyleSheet("border: 1px solid initial;")
            self.input_utterance.setStyleSheet("border: 1px solid initial;")

        else:   #新增成人語句
            if self.input_utterance.toPlainText():  #檢查有輸入句子
                rowCount = self.tableWidget.tableWidget.rowCount()    #取得目前總列數
                self.tableWidget.tableWidget.insertRow(rowCount)  #插入一列

                if not self.cbx_notCount.isChecked():   #此句採計
                    if not self.cmb_role.currentText() in self.adultNums:  #新的成人編號
                        self.adultNums[self.cmb_role.currentText()] = 1
                        self.cmb_role.addItem(self.cmb_role.currentText())  #在編號選單新增新的編號
                    else:   #已有的成人編號
                        self.adultNums[self.cmb_role.currentText()] += 1
                    roleNum = self.cmb_role.currentText() + self.adultNums[self.cmb_role.currentText()].__str__()
                    role = QtWidgets.QTableWidgetItem(roleNum)
                    self.tableWidget.tableWidget.setItem(rowCount, 0, role)
                else:   #不採計
                    role = QtWidgets.QTableWidgetItem('')
                    self.tableWidget.tableWidget.setItem(rowCount, 0, role)

                self.tableWidget.tableWidget.setItem(rowCount, 1, utterance)
                self.tableWidget.tableWidget.setItem(rowCount, 2, scenario)
                self.tableWidget.tableWidget.scrollToBottom() #新增完會保持置底

                #清空、復原輸入欄
                self.cmb_role.setCurrentIndex(0)
                self.input_utterance.clear()
                self.input_scenario.clear()
                self.cbx_notCount.setChecked(False)
                self.input_caseID.setStyleSheet("border: 1px solid initial;")
                self.input_utterance.setStyleSheet("border: 1px solid initial;")
            else:   #沒輸入句子
                self.msg_noInp.exec_()    #跳出提示視窗
                self.input_utterance.setStyleSheet("border: 1px solid red;")

    #刪除列
    def _deleteRow(self):
        indexes = self.tableWidget.tableWidget.selectionModel().selectedRows()
        for index in sorted(indexes, reverse = True):
            if self.tableWidget.tableWidget.item(index.row(), 0): #刪除成人語句
                self.adultNums[self.tableWidget.tableWidget.item(index.row(), 0).text()[0]] -= 1   #成人編號-1
                if self.adultNums[self.tableWidget.tableWidget.item(index.row(), 0).text()[0]] == 0:
                    self.cmb_role.removeItem(self.cmb_role.findText(self.tableWidget.tableWidget.item(index.row(), 0).text()[0]))
            if self.tableWidget.tableWidget.takeItem(index.row(), 3):   #刪除兒童語句
                self.childNum -= 1  #兒童編號-1
            self.tableWidget.tableWidget.removeRow(index.row())
        self._checkRoleNumAdding()
        self._syncTableCmbRoleNum()

    #新增時檢查編號
    def _checkRoleNumAdding(self):
        checkAdultNum = {}
        checkChildNum = 0
        for index in range(self.tableWidget.tableWidget.rowCount()):
            if self.tableWidget.tableWidget.item(index, 0):   #成人語句
                if not self.tableWidget.tableWidget.item(index, 0).text().__len__() == 0:   #不是空字串
                    if not self.tableWidget.tableWidget.item(index, 0).text()[0] in checkAdultNum:
                        checkAdultNum[self.tableWidget.tableWidget.item(index, 0).text()[0]] = 1
                    else:
                        checkAdultNum[self.tableWidget.tableWidget.item(index, 0).text()[0]] += 1
                    #如果編號不對
                    if not self.tableWidget.tableWidget.item(index, 0).text()[1:] == checkAdultNum[self.tableWidget.tableWidget.item(index, 0).text()[0]].__str__():
                        currectNumStr = self.tableWidget.tableWidget.item(index, 0).text()[0] + checkAdultNum[self.tableWidget.tableWidget.item(index, 0).text()[0]].__str__()
                        currectNum = QtWidgets.QTableWidgetItem(currectNumStr)
                        self.tableWidget.tableWidget.setItem(index, 0, currectNum)
            if self.tableWidget.tableWidget.item(index, 3): #兒童語句
                if not self.tableWidget.tableWidget.item(index, 3).text().__len__() == 0:   #不是空字串
                    checkChildNum += 1
                    #如果編號不對
                    if not self.tableWidget.tableWidget.item(index, 3).text() == checkChildNum.__str__():
                        currectNum = QtWidgets.QTableWidgetItem(checkChildNum.__str__())
                        self.tableWidget.tableWidget.setItem(index, 3, currectNum)
    
    #更改table時同步更新comboBox編號
    def _syncTableCmbRoleNum(self):
        checkAdultNum = {}
        checkChildNum = 0
        for index in range(self.tableWidget.tableWidget.rowCount()):
            if self.tableWidget.tableWidget.item(index, 0):   #成人語句
                if not self.tableWidget.tableWidget.item(index, 0).text().__len__() == 0:   #不是空字串
                    if not self.tableWidget.tableWidget.item(index, 0).text()[0] in checkAdultNum:
                        checkAdultNum[self.tableWidget.tableWidget.item(index, 0).text()[0]] = 1
                        if not self.tableWidget.tableWidget.item(index, 0).text()[0] in self.adultNums: #此編號不在原本的成人編號裡
                            self.cmb_role.addItem(self.tableWidget.tableWidget.item(index, 0).text()[0])    #加進comboBox
                    else:
                        checkAdultNum[self.tableWidget.tableWidget.item(index, 0).text()[0]] += 1
            if self.tableWidget.tableWidget.item(index, 3): #兒童語句
                if not self.tableWidget.tableWidget.item(index, 3).text().__len__() == 0:   #不是空字串
                    checkChildNum += 1
        self.adultNums = checkAdultNum  #更新成人編號
        self.childNum = checkChildNum   #更新兒童編號

    #更改content
    def _isEdit(self):
        self.isEdit = True
        print(self.isEdit)

    #查詢個案編號紀錄
    def _searchCase(self):
        self.caseID = self.input_caseID.text()
        self.caseData = database.DBapi.findDateAndFirstContent(self.input_caseID.text())
        print(self.caseData)

        if self.caseData:
            #清空、復原Tab2
            self.cmb_caseDates.clear()
            self.cmb_role.clear()
            self.cmb_role.addItem("兒童")
            self.cmb_role.addItem("語境")
            self.tableWidget.tableWidget.setRowCount(0)
            self.childNum = 0   #兒童編號
            self.adultNums = {}  #成人編號

            self.lbl_searchResult.setText("此個案總共有" + len(self.caseData["dates"]).__str__() + "筆資料")
            for i in range(len(self.caseData['dates'])):
                self.cmb_caseDates.addItem(self.caseData['dates'][i].strftime("%Y-%m-%d %H:%M"))

            #set table
            for i in range(len(self.caseData["FirstContent"])):
                rowCount = self.tableWidget.tableWidget.rowCount()    #取得目前總列數
                self.tableWidget.tableWidget.insertRow(rowCount)  #插入一列
                utterance = QtWidgets.QTableWidgetItem(self.caseData["FirstContent"][i]["utterance"])
                scenario = QtWidgets.QTableWidgetItem(self.caseData["FirstContent"][i]["scenario"])

                if self.caseData["FirstContent"][i]["role"] == "adult":  #成人
                    if self.caseData["FirstContent"][i]["ID"]:   #如果有編號(有採計)
                        if not self.caseData["FirstContent"][i]["ID"][0] in self.adultNums:  #新的成人編號
                            self.adultNums[self.caseData["FirstContent"][i]["ID"][0]] = 1
                            self.cmb_role.addItem(self.caseData["FirstContent"][i]["ID"][0])  #在編號選單新增新的編號
                        else:   #已有的成人編號
                            self.adultNums[self.caseData["FirstContent"][i]["ID"][0]] += 1
                    role = QtWidgets.QTableWidgetItem(self.caseData["FirstContent"][i]["ID"])
                    self.tableWidget.tableWidget.setItem(rowCount, 0, role)
                    self.tableWidget.tableWidget.setItem(rowCount, 1, utterance)
                elif self.caseData["FirstContent"][i]["role"] == "child":    #兒童
                    if self.caseData["FirstContent"][i]["ID"]:   #如果有編號(有採計)
                        self.childNum += 1
                    role = QtWidgets.QTableWidgetItem(self.caseData["FirstContent"][i]["ID"])
                    self.tableWidget.tableWidget.setItem(rowCount, 3, role)
                    self.tableWidget.tableWidget.setItem(rowCount, 4, utterance)
                self.tableWidget.tableWidget.setItem(rowCount, 2, scenario)

                if self.checkFirstSearch:   #第一次查詢
                    #顯示出查詢結果
                    self.verticalLayout_6.addWidget(self.lbl_searchResult)
                    self.verticalLayout_6.addWidget(self.cmb_caseDates)
                    self.verticalLayout_3.addLayout(self.verticalLayout_6)
                    self.checkFirstSearch = False
        else:
            print("empty")
    
    #用日期選擇個案紀錄
    def _dateSearch(self):
        content = database.DBapi.findContent(self.caseID, self.caseData["dates"][self.cmb_caseDates.currentIndex()])
        print(content)
        #清空、復原Tab2
        self.cmb_role.clear()
        self.cmb_role.addItem("兒童")
        self.cmb_role.addItem("語境")
        self.tableWidget.tableWidget.setRowCount(0)
        self.childNum = 0   #兒童編號
        self.adultNums = {}  #成人編號

        #set table
        if content:
            for i in range(content.__len__()):
                    rowCount = self.tableWidget.tableWidget.rowCount()    #取得目前總列數
                    self.tableWidget.tableWidget.insertRow(rowCount)  #插入一列
                    utterance = QtWidgets.QTableWidgetItem(content[i]["utterance"])
                    scenario = QtWidgets.QTableWidgetItem(content[i]["scenario"])

                    if content[i]["role"] == "adult":  #成人
                        if content[i]["ID"]:   #如果有編號(有採計)
                            if not content[i]["ID"][0] in self.adultNums:  #新的成人編號
                                self.adultNums[content[i]["ID"][0]] = 1
                                self.cmb_role.addItem(content[i]["ID"][0])  #在編號選單新增新的編號
                            else:   #已有的成人編號
                                self.adultNums[content[i]["ID"][0]] += 1
                        role = QtWidgets.QTableWidgetItem(content[i]["ID"])
                        self.tableWidget.tableWidget.setItem(rowCount, 0, role)
                        self.tableWidget.tableWidget.setItem(rowCount, 1, utterance)
                    elif content[i]["role"] == "child":    #兒童
                        if content[i]["ID"]:   #如果有編號(有採計)
                            self.childNum += 1
                        role = QtWidgets.QTableWidgetItem(content[i]["ID"])
                        self.tableWidget.tableWidget.setItem(rowCount, 3, role)
                        self.tableWidget.tableWidget.setItem(rowCount, 4, utterance)
                    self.tableWidget.tableWidget.setItem(rowCount, 2, scenario)

    #儲存至資料庫
    def _save(self):
        if self.input_caseID.text():
            content = []    #對話內容
            childUtterance = [] #兒童語句
            totalUtterance = 0  #總語句數
            validUtterance = 0  #採計語句數

            for rowIndex in range(self.tableWidget.tableWidget.rowCount()):
                data = {'ID': '', 'role': '', 'utterance': '', 'scenario': ''}
                if self.tableWidget.tableWidget.item(rowIndex, 0):  #adult
                    data['ID'] = self.tableWidget.tableWidget.item(rowIndex, 0).text()
                    data['role'] = 'adult'
                    if self.tableWidget.tableWidget.item(rowIndex, 1) == None:
                        item = QtWidgets.QTableWidgetItem()
                        item.setText('')
                        self.tableWidget.tableWidget.setItem(rowIndex, 1, item)
                    data['utterance'] = self.tableWidget.tableWidget.item(rowIndex, 1).text()
                elif self.tableWidget.tableWidget.item(rowIndex, 3):    #child
                    if not self.tableWidget.tableWidget.item(rowIndex, 3).text().__len__() == 0:    #採計語句
                        validUtterance += 1
                    totalUtterance += 1
                    data['ID'] = self.tableWidget.tableWidget.item(rowIndex, 3).text()
                    data['role'] = 'child'
                    if self.tableWidget.tableWidget.item(rowIndex, 4) == None:
                        item = QtWidgets.QTableWidgetItem()
                        item.setText('')
                        self.tableWidget.tableWidget.setItem(rowIndex, 4, item)
                    data['utterance'] = self.tableWidget.tableWidget.item(rowIndex, 4).text()
                    childUtterance.append(self.tableWidget.tableWidget.item(rowIndex, 4).text()) # 傳給Tab3
                if self.tableWidget.tableWidget.item(rowIndex, 2):
                    if self.tableWidget.tableWidget.item(rowIndex, 2) == None:
                        item = QtWidgets.QTableWidgetItem()
                        item.setText('')
                        self.tableWidget.tableWidget.setItem(rowIndex, 2, item)
                    data['scenario'] = self.tableWidget.tableWidget.item(rowIndex, 2).text()
                content.append(data)
            
            database.DBapi.updateContent(self.caseID, self.caseData["dates"][self.cmb_caseDates.currentIndex()], 
                                            self.input_trans.text(), content, totalUtterance, validUtterance)
            utteranceNum = [totalUtterance, validUtterance]
            self.emitUtterNum(utteranceNum)
            self.childUtterance = childUtterance

            #復原輸入框
            self.input_caseID.setStyleSheet("border: 1px solid initial;")
            self.input_utterance.setStyleSheet("border: 1px solid initial;")
        else:   #未輸入個案編號
            self.msg_noCaseID.exec_()
            self.input_caseID.setStyleSheet("border: 1px solid red;")

    #產生彙整表並儲存至資料庫
    def _generateAndSave(self):
        self._save()
        key = {'caseID':self.caseID,
                'date':self.caseData["dates"][self.cmb_caseDates.currentIndex()] }
        self.emitKey(key)
        self.emitChildUtter(self.childUtterance)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Tab2()
    ui.show()
    sys.exit(app.exec_())
