from PyQt5 import QtCore, QtGui, QtWidgets
import qtawesome as qta
import database.DatabaseApi as db

class NormModifyTab(QtWidgets.QWidget):
    def __init__(self):
        super(NormModifyTab, self).__init__()

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.setLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        #Title
        self.hbox_title = QtWidgets.QHBoxLayout()

        title_font = QtGui.QFont()
        title_font.setFamily("微軟正黑體")
        title_font.setPointSize(20)
        title_font.setBold(True)
        self.title = QtWidgets.QLabel("常模設定頁面")
        self.title.setFont(title_font)

        self.hbox_title.addItem(spacerItem)
        self.hbox_title.addWidget(self.title)
        self.hbox_title.addItem(spacerItem)
        self.verticalLayout.addLayout(self.hbox_title)

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.comboBox = QtWidgets.QComboBox()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_7.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.mlu_box = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.mlu_box.setFont(font)
        self.mlu_box.setObjectName("mlu_box")
        self.horizontalLayout_9.addWidget(self.mlu_box)
        self.vocd_box = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.vocd_box.setFont(font)
        self.vocd_box.setObjectName("vocd_box")
        self.horizontalLayout_9.addWidget(self.vocd_box)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.updateBtn = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.updateBtn.setFont(font)
        self.updateBtn.setObjectName("updateBtn")
        self.horizontalLayout_8.addWidget(self.updateBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_8)

        #新增GroupBox
        self.newAge_box = QtWidgets.QGroupBox("新增常模年紀選項")
        self.newAge_box.setMaximumSize(QtCore.QSize(350, 140))
        self.newAge_box.setFont(font)
        
        self.hbox_newAge = QtWidgets.QHBoxLayout()
        
        # self.label_newAge = QtWidgets.QLabel("新增年齡:")
        # self.label_newAge.setMaximumSize(QtCore.QSize(250, 50))
        # self.label_newAge.setFont(font)
        # self.hbox_newAge.addWidget(self.label_newAge)
        reg_ex = QtCore.QRegExp("十[一二]|[一兩二三四五六七八九]")
        numValid = QtGui.QRegExpValidator(reg_ex)
        
        self.input_newAge = QtWidgets.QLineEdit()
        self.input_newAge.setMaximumSize(QtCore.QSize(80, 50))
        self.input_newAge.setFont(font)
        self.input_newAge.setMaxLength(2)
        self.input_newAge.setValidator(numValid)
        self.hbox_newAge.addWidget(self.input_newAge)

        self.label_Age = QtWidgets.QLabel("歲")
        self.label_Age.setMaximumSize(QtCore.QSize(40, 50))
        self.label_Age.setFont(font)
        self.hbox_newAge.addWidget(self.label_Age)

        self.comboBox_age = QtWidgets.QComboBox()
        self.comboBox_age.setMaximumSize(QtCore.QSize(80, 50))
        self.comboBox_age.setFont(font)
        self.comboBox_age.addItems(["整", "半"])
        self.hbox_newAge.addWidget(self.comboBox_age)

        self.newAgeBtn = QtWidgets.QPushButton("新增")
        self.newAgeBtn.setFont(font)
        self.newAgeBtn.setObjectName("newAgeBtn")
        self.hbox_newAge.addWidget(self.newAgeBtn)

        #Remind Text
        self.hbox_age_reminder = QtWidgets.QHBoxLayout()
        self.icon = QtWidgets.QLabel()
        self.icon.setPixmap(qta.icon('fa.info-circle',color='#eed202').pixmap(QtCore.QSize(25, 25)))
        self.icon.setMaximumSize(QtCore.QSize(25, 25))
        self.remindText = QtWidgets.QLabel("空格只能輸入二到十二的中文數字")
        self.remindText.setMaximumSize(QtCore.QSize(16777215, 25))
        self.hbox_age_reminder.addWidget(self.icon)
        self.hbox_age_reminder.addWidget(self.remindText)
        
        #Set Gropubox layout
        self.vbox_addAge = QtWidgets.QVBoxLayout() #GroupBox Layout
        self.vbox_addAge.addLayout(self.hbox_newAge)
        self.vbox_addAge.addLayout(self.hbox_age_reminder)
        self.newAge_box.setLayout(self.vbox_addAge)
        self.horizontalLayout_7.addWidget(self.newAge_box)

        #Horizontal Line
        # self.line = QtWidgets.QFrame()
        # self.line.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.verticalLayout.addWidget(self.line)
        

        #NEW delete GroupBox
        self.deleteAge_box = QtWidgets.QGroupBox("刪除常模年紀選項")
        self.deleteAge_box.setMaximumSize(QtCore.QSize(350, 140))
        self.deleteAge_box.setFont(font)
        
        self.hbox_deleteAge = QtWidgets.QHBoxLayout()

        ## delete comboBox
        self.comboBox_delete = QtWidgets.QComboBox()
        self.comboBox_delete.setFont(font)
        self.hbox_deleteAge.addWidget(self.comboBox_delete)

        ##delete button
        self.deleteAgeBtn = QtWidgets.QPushButton("  刪除  ")
        self.deleteAgeBtn.setFont(font)
        self.deleteAgeBtn.setObjectName("deleteAgeBtn")
        self.hbox_deleteAge.addWidget(self.deleteAgeBtn)

        self.deleteAge_box.setLayout(self.hbox_deleteAge)
        self.horizontalLayout_7.addWidget(self.deleteAge_box)

        #New and Delete Area
        # self.new_delete_hbox = QtWidgets.QHBoxLayout()
        # self.new_delete_hbox.addWidget(self.newAge_box)
        # self.new_delete_hbox.addWidget(self.deleteAge_box)
        # self.verticalLayout.addLayout(self.new_delete_hbox)

        #Validator
        valid = QtGui.QDoubleValidator(0, 10, 2, notation=QtGui.QDoubleValidator.StandardNotation)

        #MLU GroupBox layout
        self.mlu_vbox = QtWidgets.QVBoxLayout()

        self.hbox_1 = QtWidgets.QHBoxLayout()
        self.label_mlu_c = QtWidgets.QLabel("MLU-c: ")
        self.label_mlu_c.setFont(font)
        self.input_mlu_c = QtWidgets.QLineEdit()
        self.input_mlu_c.setFont(font)
        self.input_mlu_c.setValidator(valid)

        self.hbox_1.addWidget(self.label_mlu_c)
        self.hbox_1.addWidget(self.input_mlu_c)

        self.hbox_2 = QtWidgets.QHBoxLayout()
        self.label_mlu_w = QtWidgets.QLabel("MLU-w: ")
        self.label_mlu_w.setFont(font)
        self.input_mlu_w = QtWidgets.QLineEdit()
        self.input_mlu_w.setFont(font)
        self.input_mlu_w.setValidator(valid)

        self.hbox_2.addWidget(self.label_mlu_w)
        self.hbox_2.addWidget(self.input_mlu_w)

        self.mlu_vbox.addLayout(self.hbox_1)
        self.mlu_vbox.addLayout(self.hbox_2)

        self.mlu_box.setLayout(self.mlu_vbox)
        self.mlu_box.setMaximumSize(QtCore.QSize(16777215, 250))

        #VOCD GroupBox Layout
        self.vocd_vbox = QtWidgets.QVBoxLayout()

        self.hbox_3 = QtWidgets.QHBoxLayout()
        self.label_vocd_c = QtWidgets.QLabel("VOCD-c: ")
        self.label_vocd_c.setFont(font)
        self.input_vocd_c = QtWidgets.QLineEdit()
        self.input_vocd_c.setFont(font)
        self.input_vocd_c.setValidator(valid)
        self.hbox_3.addWidget(self.label_vocd_c)
        self.hbox_3.addWidget(self.input_vocd_c)

        self.hbox_4 = QtWidgets.QHBoxLayout()
        self.label_vocd_w = QtWidgets.QLabel("VOCD-w: ")
        self.label_vocd_w.setFont(font)
        self.input_vocd_w = QtWidgets.QLineEdit()
        self.input_vocd_w.setFont(font)
        self.input_vocd_w.setValidator(valid)
        self.hbox_4.addWidget(self.label_vocd_w)
        self.hbox_4.addWidget(self.input_vocd_w)

        self.vocd_vbox.addLayout(self.hbox_3)
        self.vocd_vbox.addLayout(self.hbox_4)

        self.vocd_box.setLayout(self.vocd_vbox)
        self.vocd_box.setMaximumSize(QtCore.QSize(16777215, 250))

        #SpacerItem
        spacerItemV = QtWidgets.QSpacerItem(40, 400, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItemV)

        #Store values
        self.lastIndex = 0
        self.mluC = ""
        self.mluW = ""
        self.vocdC = ""
        self.vocdW = ""

        #Signal
        #self.comboBox.currentIndexChanged.connect(self.getCurrentNorm)
        self.comboBox.textActivated.connect(self.getCurrentNorm)
        self.updateBtn.clicked.connect(self.save)
        self.newAgeBtn.clicked.connect(self.addAge)
        self.deleteAgeBtn.clicked.connect(self.deleteAge)
        self.input_newAge.textChanged.connect(self.checkLimitAge)

        self.retranslateUi()
        self.setStyleSheet(open("./QSS/norm.qss", "r").read())

    def getCurrentNorm(self):
        #check if change value didn't store
        if self.comboBox.currentIndex() != self.lastIndex:
            if (self.mluC != self.input_mlu_c.text()) or (self.mluW != self.input_mlu_w.text()) or (self.vocdC != self.input_vocd_c.text()) or (self.vocdW != self.input_vocd_w.text()):
                warnText = f'<p style="font-size:13pt; color: #3778bf;">要儲存 {self.comboBox.itemText(self.lastIndex)} 的變更嗎?</p>\n'
                close = QtWidgets.QMessageBox.warning(self,
                                "CLSA",
                                warnText,
                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
                
                if close == QtWidgets.QMessageBox.Yes:
                    self.save()
                if close == QtWidgets.QMessageBox.Cancel:
                    self.comboBox.setCurrentIndex(self.lastIndex)
                    return

        #store index 
        self.lastIndex = self.comboBox.currentIndex()

        #Value
        key = self.comboBox.currentText()
        n = db.findNormByAge(key)
        self.storeValue(n)

    def getNorms(self):
        norms = db.getNormAges()
        self.comboBox.clear()
        self.comboBox_delete.clear()

        for idx, n in enumerate(norms):
            if idx == 0:
                self.storeValue(n)

            self.comboBox.addItem(n['age'])
            self.comboBox_delete.addItem(n['age'])
    
    def storeValue(self, n):  #將值存在格子和變數中
        
        self.input_mlu_c.setText(n['data']['mlu-c'])
        self.mluC = n['data']['mlu-c']
    
        self.input_mlu_w.setText(n['data']['mlu-w'])
        self.mluW = n['data']['mlu-w']
    
        self.input_vocd_c.setText(n['data']['vocd-c'])
        self.vocdC = n['data']['vocd-c']
    
        self.input_vocd_w.setText(n['data']['vocd-w'])
        self.vocdW = n['data']['vocd-w']
    
    def save(self):
        data = {
            "mlu-c": self.input_mlu_c.text(),
            "mlu-w": self.input_mlu_w.text(),
            "vocd-c": self.input_vocd_c.text(),
            "vocd-w": self.input_vocd_w.text()
        }

        #更新暫存值
        self.mluC = data['mlu-c']
        self.mluW = data['mlu-w']
        self.vocdC = data['vocd-c']
        self.vocdW = data['vocd-w']

        age = self.comboBox.itemText(self.lastIndex)

        db.upsertNorm(age, self.chineseToNum(age), data)
        QtWidgets.QMessageBox.information(self, '通知','更新成功', QtWidgets.QMessageBox.Ok)

    def addAge(self):
        newAge = ''
        if self.input_newAge.text() == '':
            return
        else:
            if self.input_newAge.text() == '兩': #特例
                newAge = '二歲'
            else:
                newAge += (self.input_newAge.text() + '歲')
            if self.comboBox_age.currentText() == '半':
                newAge += '半'
        
        ages = [self.comboBox.itemText(i) for i in range(self.comboBox.count())]
        if newAge in ages:
            QtWidgets.QMessageBox.warning(self, '警告','年齡已存在', QtWidgets.QMessageBox.Ok)
            return
        else:
            data = {
                "mlu-c": "",
                "mlu-w": "",
                "vocd-c": "",
                "vocd-w": ""
            }

            db.upsertNorm(newAge, self.chineseToNum(newAge) ,data)
            self.getNorms()

            QtWidgets.QMessageBox.information(self, '警告','成功新增', QtWidgets.QMessageBox.Ok)

    def deleteAge(self):
        warnText = f'<p style="font-size:13pt; color: #525252;">確定要刪除 {self.comboBox_delete.currentText()}嗎?</p>\n'
        delete = QtWidgets.QMessageBox.question(self,
                                "CLSA",
                                warnText,
                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                
        if delete == QtWidgets.QMessageBox.Yes:
            db.deleteNorm(self.comboBox_delete.currentText())
            QtWidgets.QMessageBox.information(self, '警告','成功刪除', QtWidgets.QMessageBox.Ok)
            #重刷
            self.getNorms()
        if delete == QtWidgets.QMessageBox.No:
            pass


    def chineseToNum(self, text):
        numToChinese = {
            "一": 1,"二": 2,"三": 3,"四": 4,"五": 5,"六": 6,"七": 7,"八": 8,"九": 9,"十": 10
        }

        if len(text) == 2: #兩歲, 三歲...十歲
            return numToChinese[text[0]]
        elif len(text) == 3:  # (1)兩歲半, 三歲半...十歲半 (2) 十一歲, 十二歲...
            if text[2] == '半':
                return numToChinese[text[0]] + 0.5
            elif text[2] == '歲':
                return 10 + numToChinese[text[1]]
        elif len(text) == 4:
                return 10 + numToChinese[text[1]] + 0.5
    
    def checkLimitAge(self):
        if self.input_newAge.text() == '十二':
            if self.comboBox_age.count() == 2:
                self.comboBox_age.removeItem(1)
        else:
            if self.comboBox_age.count() == 1:
                self.comboBox_age.addItem('半')

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_5.setText(_translate("", "欲設定之常模年紀: "))
        self.mlu_box.setTitle(_translate("", "平均語句長度"))
        self.vocd_box.setTitle(_translate("", "詞彙多樣性"))
        self.updateBtn.setText(_translate("", "    更新    "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = NormModifyTab()
    ui.show()
    sys.exit(app.exec_())
