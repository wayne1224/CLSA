# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'myself.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class DateEdit(QtWidgets.QDateEdit):
    def __init__(self, parent=None):
        super().__init__(parent, calendarPopup=True)
        # self.setDateTime(QtCore.QDateTime.currentDateTime())

class Myform(QtWidgets.QWidget):
    def __init__(self):
        super(Myform, self).__init__()
        self.setObjectName("self")
        self.resize(1393, 815)
        self.horizontalLayoutWidget_15 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_15.setGeometry(QtCore.QRect(870, 410, 301, 61))
        self.horizontalLayoutWidget_15.setObjectName("horizontalLayoutWidget_15")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_15)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.checkBox_7 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_15)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.horizontalLayout_15.addWidget(self.checkBox_7)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_15)
        self.lineEdit_10.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_15.addWidget(self.lineEdit_10)
        self.horizontalLayoutWidget_17 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_17.setGeometry(QtCore.QRect(251, 591, 991, 61))
        self.horizontalLayoutWidget_17.setObjectName("horizontalLayoutWidget_17")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_17)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget_17)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_17.addWidget(self.plainTextEdit)
        self.horizontalLayoutWidget_12 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_12.setGeometry(QtCore.QRect(600, 310, 351, 51))
        self.horizontalLayoutWidget_12.setObjectName("horizontalLayoutWidget_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_12)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_12.addWidget(self.label_13)
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget_12)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.timeEdit_2.setFont(font)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.horizontalLayout_12.addWidget(self.timeEdit_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(61, 111, 141, 401))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_2.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_2.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_2.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_2.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_2.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_2.addWidget(self.label_26)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(640, 50, 349, 49))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget_13 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_13.setGeometry(QtCore.QRect(600, 360, 301, 51))
        self.horizontalLayoutWidget_13.setObjectName("horizontalLayoutWidget_13")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget_13)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_13)
        self.lineEdit_8.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_13.addWidget(self.lineEdit_8)
        self.horizontalLayoutWidget_18 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_18.setGeometry(QtCore.QRect(200, 361, 331, 51))
        self.horizontalLayoutWidget_18.setObjectName("horizontalLayoutWidget_18")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_18)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_18)
        self.lineEdit_12.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_18.addWidget(self.lineEdit_12)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(200, 260, 331, 61))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_9)
        self.lineEdit_7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_9.addWidget(self.lineEdit_7)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(201, 110, 311, 51))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.lineEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_7.addWidget(self.lineEdit)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(870, 99, 391, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(31, 511, 221, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.verticalLayout.addWidget(self.label_20)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.verticalLayout.addWidget(self.label_19)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout.addWidget(self.label_18)
        self.horizontalLayoutWidget_19 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_19.setGeometry(QtCore.QRect(201, 411, 631, 61))
        self.horizontalLayoutWidget_19.setObjectName("horizontalLayoutWidget_19")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_19)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.checkBox_5 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_19)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_19.addWidget(self.checkBox_5)
        self.checkBox_3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_19)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_19.addWidget(self.checkBox_3)
        self.checkBox_6 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_19)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout_19.addWidget(self.checkBox_6)
        self.checkBox_4 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_19)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_19.addWidget(self.checkBox_4)
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_19)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_19.addWidget(self.checkBox_2)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(600, 260, 681, 51))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.radioButton_7 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setObjectName("radioButton_7")
        self.horizontalLayout_8.addWidget(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setObjectName("radioButton_8")
        self.horizontalLayout_8.addWidget(self.radioButton_8)
        self.radioButton_9 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton_9.setFont(font)
        self.radioButton_9.setObjectName("radioButton_9")
        self.horizontalLayout_8.addWidget(self.radioButton_9)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(600, 160, 271, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_5.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_5.addWidget(self.radioButton)
        self.horizontalLayoutWidget_20 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_20.setGeometry(QtCore.QRect(201, 461, 931, 61))
        self.horizontalLayoutWidget_20.setObjectName("horizontalLayoutWidget_20")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_20)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.radioButton_11 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_20)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton_11.setFont(font)
        self.radioButton_11.setObjectName("radioButton_11")
        self.horizontalLayout_20.addWidget(self.radioButton_11)
        self.radioButton_10 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_20)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton_10.setFont(font)
        self.radioButton_10.setObjectName("radioButton_10")
        self.horizontalLayout_20.addWidget(self.radioButton_10)
        self.radioButton_12 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_20)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton_12.setFont(font)
        self.radioButton_12.setObjectName("radioButton_12")
        self.horizontalLayout_20.addWidget(self.radioButton_12)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(201, 211, 1041, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout.addWidget(self.radioButton_4)
        self.radioButton_13 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton_13.setFont(font)
        self.radioButton_13.setObjectName("radioButton_13")
        self.horizontalLayout.addWidget(self.radioButton_13)
        self.radioButton_5 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout.addWidget(self.radioButton_5)
        self.horizontalLayoutWidget_21 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_21.setGeometry(QtCore.QRect(251, 671, 991, 56))
        self.horizontalLayoutWidget_21.setObjectName("horizontalLayoutWidget_21")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_21)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget_21)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.horizontalLayout_21.addWidget(self.plainTextEdit_2)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(201, 301, 331, 81))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        # self.dateEdit_2 = QtWidgets.QDateEdit(self.horizontalLayoutWidget_10)

        self.dateEdit_2 =DateEdit()
        self.dateEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout_10.addWidget(self.dateEdit_2)
        self.horizontalLayoutWidget_16 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_16.setGeometry(QtCore.QRect(251, 511, 881, 71))
        self.horizontalLayoutWidget_16.setObjectName("horizontalLayoutWidget_16")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_16)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.radioButton_15 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_16)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton_15.setFont(font)
        self.radioButton_15.setObjectName("radioButton_15")
        self.horizontalLayout_16.addWidget(self.radioButton_15)
        self.radioButton_17 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_16)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton_17.setFont(font)
        self.radioButton_17.setObjectName("radioButton_17")
        self.horizontalLayout_16.addWidget(self.radioButton_17)
        self.radioButton_16 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_16)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton_16.setFont(font)
        self.radioButton_16.setObjectName("radioButton_16")
        self.horizontalLayout_16.addWidget(self.radioButton_16)
        self.radioButton_14 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_16)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton_14.setFont(font)
        self.radioButton_14.setObjectName("radioButton_14")
        self.horizontalLayout_16.addWidget(self.radioButton_14)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(201, 161, 311, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(870, 160, 281, 51))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        # self.dateEdit = QtWidgets.QDateEdit(self.horizontalLayoutWidget_6)
        self.dateEdit = DateEdit()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_6.addWidget(self.dateEdit)
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(970, 310, 281, 51))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_11)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.timeEdit = QtWidgets.QTimeEdit(self.horizontalLayoutWidget_11)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.timeEdit.setFont(font)
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout_11.addWidget(self.timeEdit)
        self.horizontalLayoutWidget_14 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_14.setGeometry(QtCore.QRect(970, 360, 281, 51))
        self.horizontalLayoutWidget_14.setObjectName("horizontalLayoutWidget_14")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_14)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget_14)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_14.addWidget(self.label_15)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_14)
        self.lineEdit_9.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_14.addWidget(self.lineEdit_9)

        self.retranslateUi()
        # QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.checkBox_7.setText(_translate("self", " 其他"))
        self.label_13.setText(_translate("self", "收錄開始時間:"))
        self.label_21.setText(_translate("self", "收錄者:"))
        self.label_22.setText(_translate("self", "個案姓名:"))
        self.label_23.setText(_translate("self", "收錄情境:"))
        self.label_24.setText(_translate("self", "收錄地點:"))
        self.label_25.setText(_translate("self", "收錄日期:"))
        self.label_26.setText(_translate("self", "誘發題材:"))
        self.label_16.setText(_translate("self", "參與人員:"))
        self.label_17.setText(_translate("self", "記錄方式:"))
        self.label_3.setText(_translate("self", "CLSA分析"))
        self.label_14.setText(_translate("self", "兒童總語句數"))
        self.label_2.setText(_translate("self", "個案編號:"))
        self.label_20.setText(_translate("self", "需要引導協助:"))
        self.label_19.setText(_translate("self", "其他特殊情況:"))
        self.label_18.setText(_translate("self", "兒童焦慮情形:"))
        self.checkBox_5.setText(_translate("self", " 老師"))
        self.checkBox_3.setText(_translate("self", "爸爸"))
        self.checkBox_6.setText(_translate("self", "媽媽"))
        self.checkBox_4.setText(_translate("self", "施測者"))
        self.checkBox_2.setText(_translate("self", " 兒童"))
        self.label_8.setText(_translate("self", "互動形式:"))
        self.radioButton_7.setText(_translate("self", "交談"))
        self.radioButton_8.setText(_translate("self", "自由遊戲"))
        self.radioButton_9.setText(_translate("self", "敘事"))
        self.label_5.setText(_translate("self", "性別:"))
        self.radioButton_2.setText(_translate("self", "女"))
        self.radioButton.setText(_translate("self", "男"))
        self.radioButton_11.setText(_translate("self", "其他錄音設備"))
        self.radioButton_10.setText(_translate("self", "錄音筆"))
        self.radioButton_12.setText(_translate("self", "攝影機"))
        self.radioButton_3.setText(_translate("self", "情境1"))
        self.radioButton_4.setText(_translate("self", "情境2"))
        self.radioButton_13.setText(_translate("self", "情境3"))
        self.radioButton_5.setText(_translate("self", "情境4"))
        self.radioButton_15.setText(_translate("self", "很少 (幾乎不需要引導)"))
        self.radioButton_17.setText(_translate("self", "有時 (2~5次)"))
        self.radioButton_16.setText(_translate("self", "經常 (6~9次)"))
        self.radioButton_14.setText(_translate("self", "總是"))
        self.label_6.setText(_translate("self", "生日:"))
        self.label_11.setText(_translate("self", "結束時間:"))
        self.label_15.setText(_translate("self", "有效語句數:"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # self = QtWidgets.QWidget()
    ui = Myform()
    ui.show()
    sys.exit(app.exec_())
