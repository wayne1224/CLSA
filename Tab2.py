# -*- coding: utf-8 -*-

#  implementation generated from reading ui file 'c:\Users\fuhan\Desktop\NLP\CLSA\Tab2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import Mytable
from PyQt5 import QtCore, QtGui, QtWidgets


class Tab2(QtWidgets.QWidget):
    def __init__(self):
        super(Tab2, self).__init__()

        #self.setGeometry(QtCore.QRect(-1, 0, 1121, 801))

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, 10, 0, 0)
        self.gridLayout.setSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_trans = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(91)
        sizePolicy.setVerticalStretch(31)
        sizePolicy.setHeightForWidth(self.lbl_trans.sizePolicy().hasHeightForWidth())
        self.lbl_trans.setSizePolicy(sizePolicy)
        self.lbl_trans.setMaximumSize(QtCore.QSize(91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_trans.setFont(font)
        self.lbl_trans.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_trans.setObjectName("lbl_trans")
        self.gridLayout.addWidget(self.lbl_trans, 1, 0, 1, 1)
        self.input_caseNum = QtWidgets.QLineEdit()
        self.input_caseNum.setMinimumSize(QtCore.QSize(101, 31))
        self.input_caseNum.setMaximumSize(QtCore.QSize(101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_caseNum.setFont(font)
        self.input_caseNum.setObjectName("input_caseNum")
        self.gridLayout.addWidget(self.input_caseNum, 1, 3, 1, 1)
        self.input_trans = QtWidgets.QLineEdit()
        self.input_trans.setMinimumSize(QtCore.QSize(101, 31))
        self.input_trans.setMaximumSize(QtCore.QSize(101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_trans.setFont(font)
        self.input_trans.setObjectName("input_trans")
        self.gridLayout.addWidget(self.input_trans, 1, 1, 1, 1)
        self.lbl_caseNum = QtWidgets.QLabel()
        self.lbl_caseNum.setMinimumSize(QtCore.QSize(111, 31))
        self.lbl_caseNum.setMaximumSize(QtCore.QSize(111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_caseNum.setFont(font)
        self.lbl_caseNum.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_caseNum.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_caseNum.setObjectName("lbl_caseNum")
        self.gridLayout.addWidget(self.lbl_caseNum, 1, 2, 1, 1)
        layout.addLayout(self.gridLayout)
        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        layout.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, -1, 50, 0)
        self.gridLayout_2.setVerticalSpacing(7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_scenario = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_scenario.setFont(font)
        self.lbl_scenario.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_scenario.setObjectName("lbl_scenario")
        self.gridLayout_2.addWidget(self.lbl_scenario, 0, 4, 1, 1)
        self.lbl_utterance = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_utterance.setFont(font)
        self.lbl_utterance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_utterance.setObjectName("lbl_utterance")
        self.gridLayout_2.addWidget(self.lbl_utterance, 0, 2, 1, 1)
        self.input_scenario = QtWidgets.QLineEdit()
        self.input_scenario.setMinimumSize(QtCore.QSize(241, 131))
        self.input_scenario.setMaximumSize(QtCore.QSize(241, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_scenario.setFont(font)
        self.input_scenario.setObjectName("input_scenario")
        self.gridLayout_2.addWidget(self.input_scenario, 0, 5, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cbx_notCount = QtWidgets.QCheckBox()
        self.cbx_notCount.setMinimumSize(QtCore.QSize(131, 41))
        self.cbx_notCount.setMaximumSize(QtCore.QSize(131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbx_notCount.setFont(font)
        self.cbx_notCount.setObjectName("cbx_notCount")
        self.verticalLayout_3.addWidget(self.cbx_notCount)
        self.btn_add = QtWidgets.QPushButton()
        self.btn_add.setMinimumSize(QtCore.QSize(101, 51))
        self.btn_add.setMaximumSize(QtCore.QSize(101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        self.verticalLayout_3.addWidget(self.btn_add)
        self.btn_delete = QtWidgets.QPushButton()
        self.btn_delete.setMinimumSize(QtCore.QSize(101, 51))
        self.btn_delete.setMaximumSize(QtCore.QSize(101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_delete.setFont(font)
        self.btn_delete.setObjectName("btn_delete")
        self.verticalLayout_3.addWidget(self.btn_delete)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 6, 1, 1)
        self.cmb_role = QtWidgets.QComboBox()
        self.cmb_role.setMinimumSize(QtCore.QSize(81, 31))
        self.cmb_role.setMaximumSize(QtCore.QSize(81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cmb_role.setFont(font)
        self.cmb_role.setEditable(True)
        self.cmb_role.setObjectName("cmb_role")
        self.cmb_role.addItem("")
        self.cmb_role.addItem("")
        self.gridLayout_2.addWidget(self.cmb_role, 0, 1, 1, 1)
        self.lbl_role = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_role.setFont(font)
        self.lbl_role.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_role.setObjectName("lbl_role")
        self.gridLayout_2.addWidget(self.lbl_role, 0, 0, 1, 1)
        self.input_utterance = QtWidgets.QLineEdit()
        self.input_utterance.setMinimumSize(QtCore.QSize(241, 131))
        self.input_utterance.setMaximumSize(QtCore.QSize(241, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_utterance.setFont(font)
        self.input_utterance.setObjectName("input_utterance")
        self.gridLayout_2.addWidget(self.input_utterance, 0, 3, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.tableWidget = Mytable.Mytable()
        Mytable.Mytable.__init__(self.tableWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.verticalLayout.addWidget(self.tableWidget)
        layout.addLayout(self.verticalLayout)
        layout.setStretch(1, 1)
        layout.setStretch(2, 2)

        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName()

        #按鈕事件
        self.btn_add.clicked.connect(self._addRow)
        self.btn_delete.clicked.connect(self._deleteRow)

        self.childNum = 0   #兒童編號
        self.adultNums = {}  #成人編號

        #未輸入語句提示視窗
        self.noInpMsg = QtWidgets.QMessageBox()
        self.noInpMsg.setWindowTitle("提示")
        self.noInpMsg.setText("請輸入語句！")
        self.noInpMsg.setIcon(QtWidgets.QMessageBox.Question)
        #成人、兒童同時輸入提示視窗
        self.multiInpMsg = QtWidgets.QMessageBox()
        self.multiInpMsg.setWindowTitle("提示")
        self.multiInpMsg.setText("成人與兒童語句不能同時輸入！")
        self.multiInpMsg.setIcon(QtWidgets.QMessageBox.Warning)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_trans.setText(_translate("", "轉錄者："))
        self.lbl_caseNum.setText(_translate("", "個案編號："))
        self.lbl_role.setText(_translate("", "編號："))
        self.cmb_role.setItemText(0, _translate("Form", "兒童"))
        self.cmb_role.setItemText(1, _translate("Form", "語境"))
        self.lbl_utterance.setText(_translate("", "語句："))
        self.lbl_scenario.setText(_translate("", "語境："))
        self.cbx_notCount.setText(_translate("", "此句不採計"))
        self.btn_add.setText(_translate("", "新增"))
        self.btn_delete.setText(_translate("", "刪除"))

    #新增列
    def _addRow(self):
        sentence = QtWidgets.QTableWidgetItem(self.input_utterance.text())
        context = QtWidgets.QTableWidgetItem(self.input_scenario.text())

        if self.cmb_role.currentText() == "兒童":   #新增兒童語句
            if self.input_utterance.text():  #檢查有輸入句子
                rowCount = self.tableWidget.tableWidget.rowCount()    #取得目前總列數
                self.tableWidget.tableWidget.insertRow(rowCount)  #插入一列

                if not self.cbx_notCount.isChecked():   #此句採計
                    self.childNum += 1
                    role = QtWidgets.QTableWidgetItem(self.childNum.__str__())
                    self.tableWidget.tableWidget.setItem(rowCount, 3, role)
                
                self.tableWidget.tableWidget.setItem(rowCount, 4, sentence)
                self.tableWidget.tableWidget.setItem(rowCount, 2, context)
                self.tableWidget.tableWidget.scrollToBottom() #新增完會保持置底

                #清空、復原輸入欄
                self.cmb_role.setCurrentIndex(0)
                self.input_utterance.clear()
                self.input_scenario.clear()
                self.cbx_notCount.setChecked(False)
            else:   #沒輸入句子
                self.noInpMsg.exec_()    #跳出提示視窗

        elif self.cmb_role.currentText() == "語境":   #只新增語境
            rowCount = self.tableWidget.tableWidget.rowCount()    #取得目前總列數
            self.tableWidget.tableWidget.insertRow(rowCount)  #插入一列
            self.tableWidget.tableWidget.setItem(rowCount, 2, context)
            self.tableWidget.tableWidget.scrollToBottom() #新增完會保持置底

            #清空、復原輸入欄
            self.cmb_role.setCurrentIndex(0)
            self.input_utterance.clear()
            self.input_scenario.clear()
            self.cbx_notCount.setChecked(False)

        else:   #新增成人語句
            if self.input_utterance.text():  #檢查有輸入句子
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

                self.tableWidget.tableWidget.setItem(rowCount, 1, sentence)
                self.tableWidget.tableWidget.setItem(rowCount, 2, context)
                self.tableWidget.tableWidget.scrollToBottom() #新增完會保持置底

                #清空、復原輸入欄
                self.cmb_role.setCurrentIndex(0)
                self.input_utterance.clear()
                self.input_scenario.clear()
                self.cbx_notCount.setChecked(False)
            else:   #沒輸入句子
                self.noInpMsg.exec_()    #跳出提示視窗

    #刪除列
    def _deleteRow(self):
        indexes = self.tableWidget.tableWidget.selectionModel().selectedRows()
        for index in sorted(indexes, reverse = True):
            if self.tableWidget.tableWidget.item(index.row(), 0): #刪除成人語句
                self.adultNums[self.tableWidget.item(index.row(), 0).text()[0]] -= 1   #成人編號-1
            elif self.tableWidget.tableWidget.takeItem(index.row(), 3):   #刪除兒童語句
                self.childNum -= 1  #兒童編號-1
            self.tableWidget.tableWidget.removeRow(index.row())
        self._checkRoleNum()

    #檢查編號
    def _checkRoleNum(self):
        checkAdultNum = {}
        checkChildNum = 0
        for index in range(self.tableWidget.tableWidget.rowCount()):
            if self.tableWidget.tableWidget.item(index, 0):   #如果此列是成人語句
                if not self.tableWidget.tableWidget.item(index, 0).text()[0] in checkAdultNum:
                    checkAdultNum[self.tableWidget.tableWidget.item(index, 0).text()[0]] = 1
                else:
                    checkAdultNum[self.tableWidget.tableWidget.item(index, 0).text()[0]] += 1
                #如果編號不對
                if not self.tableWidget.tableWidget.item(index, 0).text()[1:] == checkAdultNum[self.tableWidget.tableWidget.item(index, 0).text()[0]].__str__():
                    currectNumStr = self.tableWidget.tableWidget.item(index, 0).text()[0] + checkAdultNum[self.tableWidget.tableWidget.item(index, 0).text()[0]].__str__()
                    currectNum = QtWidgets.QTableWidgetItem(currectNumStr)
                    self.tableWidget.tableWidget.setItem(index, 0, currectNum)
            elif self.tableWidget.tableWidget.item(index, 3): #如果此列是兒童語句
                checkChildNum += 1
                #如果編號不對
                if not self.tableWidget.tableWidget.item(index, 3).text() == checkChildNum.__str__():
                    currectNum = QtWidgets.QTableWidgetItem(checkChildNum.__str__())
                    self.tableWidget.tableWidget.setItem(index, 3, currectNum)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Tab2()
    ui.show()
    sys.exit(app.exec_())
