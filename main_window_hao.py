# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1033, 584)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        Form.setFont(font)
        Form.setLayoutDirection(QtCore.Qt.RightToLeft)
        Form.setAutoFillBackground(False)
        self.main_label = QtWidgets.QLabel(Form)
        self.main_label.setGeometry(QtCore.QRect(380, 30, 251, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        self.main_label.setFont(font)
        self.main_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.main_label.setAutoFillBackground(True)
        self.main_label.setTextFormat(QtCore.Qt.AutoText)
        self.main_label.setScaledContents(False)
        self.main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_label.setObjectName("main_label")
        self.label_adult_name = QtWidgets.QLabel(Form)
        self.label_adult_name.setGeometry(QtCore.QRect(60, 100, 71, 21))
        self.label_adult_name.setObjectName("label_adult_name")
        self.input_adult_sentence = QtWidgets.QLineEdit(Form)
        self.input_adult_sentence.setGeometry(QtCore.QRect(500, 100, 311, 21))
        self.input_adult_sentence.setText("")
        self.input_adult_sentence.setObjectName("input_adult_sentence")
        self.label_adult_sentence = QtWidgets.QLabel(Form)
        self.label_adult_sentence.setGeometry(QtCore.QRect(420, 100, 81, 21))
        self.label_adult_sentence.setObjectName("label_adult_sentence")
        self.label_child_sentence = QtWidgets.QLabel(Form)
        self.label_child_sentence.setGeometry(QtCore.QRect(60, 130, 81, 16))
        self.label_child_sentence.setObjectName("label_child_sentence")
        self.input_child_sentence = QtWidgets.QLineEdit(Form)
        self.input_child_sentence.setGeometry(QtCore.QRect(140, 130, 271, 20))
        self.input_child_sentence.setObjectName("input_child_sentence")
        self.label_tone = QtWidgets.QLabel(Form)
        self.label_tone.setGeometry(QtCore.QRect(450, 130, 41, 21))
        self.label_tone.setObjectName("label_tone")
        self.input_tone = QtWidgets.QLineEdit(Form)
        self.input_tone.setGeometry(QtCore.QRect(500, 130, 311, 20))
        self.input_tone.setObjectName("input_tone")
        self.pb_insert = QtWidgets.QPushButton(Form)
        self.pb_insert.setGeometry(QtCore.QRect(860, 100, 71, 23))
        self.pb_insert.setObjectName("pb_insert")
        self.label_writer = QtWidgets.QLabel(Form)
        self.label_writer.setGeometry(QtCore.QRect(720, 30, 61, 21))
        self.label_writer.setObjectName("label_writer")
        self.input_writer = QtWidgets.QLineEdit(Form)
        self.input_writer.setGeometry(QtCore.QRect(790, 30, 121, 20))
        self.input_writer.setObjectName("input_writer")
        self.label_num = QtWidgets.QLabel(Form)
        self.label_num.setGeometry(QtCore.QRect(710, 60, 81, 21))
        self.label_num.setObjectName("label_num")
        self.input_num = QtWidgets.QLineEdit(Form)
        self.input_num.setGeometry(QtCore.QRect(790, 60, 121, 20))
        self.input_num.setObjectName("input_num")
        self.pb_done = QtWidgets.QPushButton(Form)
        self.pb_done.setGeometry(QtCore.QRect(920, 550, 81, 23))
        self.pb_done.setObjectName("pb_done")
        self.label_insert = QtWidgets.QLabel(Form)
        self.label_insert.setGeometry(QtCore.QRect(60, 160, 221, 16))
        self.label_insert.setObjectName("label_insert")
        self.input_insert_row = QtWidgets.QLineEdit(Form)
        self.input_insert_row.setGeometry(QtCore.QRect(280, 160, 131, 20))
        self.input_insert_row.setObjectName("input_insert_row")
        self.label_delete = QtWidgets.QLabel(Form)
        self.label_delete.setGeometry(QtCore.QRect(420, 160, 221, 21))
        self.label_delete.setObjectName("label_delete")
        self.input_delete_row = QtWidgets.QLineEdit(Form)
        self.input_delete_row.setGeometry(QtCore.QRect(640, 160, 171, 20))
        self.input_delete_row.setObjectName("input_delete_row")
        self.pb_delete = QtWidgets.QPushButton(Form)
        self.pb_delete.setGeometry(QtCore.QRect(860, 130, 71, 23))
        self.pb_delete.setObjectName("pb_delete")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 210, 1041, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table.setObjectName("table")
        self.table.setColumnCount(5)
        self.table.setRowCount(0)

        self.table.setColumnWidth(0 , 100)
        self.table.setColumnWidth(1 , 290)
        self.table.setColumnWidth(2 , 200)
        self.table.setColumnWidth(3 , 100)
        self.table.horizontalHeader().setSectionResizeMode(4 , QtWidgets.QHeaderView.Stretch)

        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.table)
        self.checkbox_sentence = QtWidgets.QCheckBox(Form)
        self.checkbox_sentence.setGeometry(QtCore.QRect(840, 160, 111, 21))
        self.checkbox_sentence.setObjectName("checkbox_sentence")
        self.combobox_adult_name = QtWidgets.QComboBox(Form)
        self.combobox_adult_name.setGeometry(QtCore.QRect(140, 100, 271, 22))
        self.combobox_adult_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.combobox_adult_name.setObjectName("combobox_adult_name")
        self.combobox_adult_name.setEditable(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.adult_list = list()
        self.pb_insert.clicked.connect(self.insert_row)
        self.pb_delete.clicked.connect(self.remove_row)
        self.pb_done.clicked.connect(self.output)


    def insert_row(self): # input = [成人編號 , 成人語句 , 語境 , 兒童編號 , 兒童語句]
        index = 0
        data = list()
        
        row = self.table.rowCount()
        input_index = self.input_insert_row.text()
        adult_name = self.combobox_adult_name.currentText()
        adult_sentence = self.input_adult_sentence.text()
        child_sentence = self.input_child_sentence.text()
        tone = self.input_tone.text()
        
        # 判斷要插入哪一列
        if input_index == "":
            index = row
        else:
            index = int(input_index) - 1

            if index >= row:
                print("invaild insert row")
                return

        # case 1 採計 成人輸入 => 必要 : 成人編號 , 成人語句 / 不需要 : 兒童編號 , 兒童語句 , 不採計 / Optional : 語境 
        if adult_name != "" and adult_sentence != "" and child_sentence == "" and not self.checkbox_sentence.isChecked():  
            if adult_name not in self.adult_list: # 第一次出現的成人
                self.adult_list.append(adult_name) # 將第一次出現的成人加進adult_list裡
                self.combobox_adult_name.addItem(adult_name) # 將第一次出現的成人加進下拉式選單中

                data = [adult_name + "1" , adult_sentence , tone , "" , ""] 
            else: # 此成人編號已經有了
                count = 1
                string = str()
                
                if self.table.item(i , 0).text() != "":
                    tmp = re.findall("[a-zA-Z]+" , self.table.item(i , 0).text())[0] # ex: apple1 => apple
                else:
                    tmp = ""

                for i in range(index - 1 , -1 , -1): # range => (index - 1) ~ 0 , 計算到index列前，成人已經講幾句話了                                      
                    if adult_name == tmp: 
                        count = count + 1
                
                data = [adult_name + str(count) , adult_sentence , tone , "" , ""]          
     
                for i in range(index , row): # range => index ~ rowcount - 1 , 將後面相同編號的數字都 + 1
                    if adult_name == tmp:
                        count = count + 1
                        string = adult_name + str(count)
                        item = QtWidgets.QTableWidgetItem()
                        item.setText(string)
                        item.setFlags(QtCore.Qt.ItemIsEnabled)
                        self.table.setItem(i , 0 , item)

        # case 2 採計 兒童輸入 => 必要 : 兒童編號 , 兒童語句 / 不需要 : 成人編號 , 成人語句 , 不採計 / Optional : 語境 
        elif child_sentence != "" and adult_name == "" and adult_sentence == "" and not self.checkbox_sentence.isChecked():
            count = 1

            for i in range(0 , index): # range => 0 ~ (index - 1) , 算到index之前 兒童已經說過幾句話了
                if self.table.item(i , 3).text() != "":
                    count = count + 1
             
            data = ["" , "" , tone , str(count) , child_sentence]  

            for i in range(index , row): # range => index ~ (rowcount - 1) , 將後面的數字都 + 1
                if self.table.item(i , 3).text() != "":
                    count = count + 1
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(count))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.table.setItem(i , 3 , item)
            
        # case 3 採計 只有語境輸入 => 必要 : 語境 / 不需要 : 成人編號 , 成人語句 , 兒童編號 , 兒童語句 , 不採計
        elif tone != "" and adult_name == "" and adult_sentence == "" and child_sentence == "" and not self.checkbox_sentence.isChecked():
            data = ["" , "" , tone , "" , ""]
        
        # case 4 不採計 成人輸入 => 必要 : 成人語句 , 不採計 / 不需要 : 兒童編號 , 兒童語句 / Optional : 成人編號 , 語境
        elif adult_sentence != "" and child_sentence == "" and self.checkbox_sentence.isChecked():
            data = ["" , adult_sentence , tone , "" , ""]
        
        # case 5 不採計 兒童輸入 => 必要 : 兒童語句 , 不採計 / 不需要 : 成人編號 , 成人語句 / Optional : 兒童編號 , 語境
        elif child_sentence != "" and adult_name == "" and adult_sentence == "" and self.checkbox_sentence.isChecked():
            data = ["" , "" , tone , "" , child_sentence]
        
        else:
            print("invaild input")
            return
              
        self.table.insertRow(index)

        for i in range(5):
            item = QtWidgets.QTableWidgetItem()
            item.setText(data[i])
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.table.setItem(index , i , item)
        
        self.clear_input()
        self.table.scrollToBottom() # 自動讓表格到最底下
    
    def remove_row(self):
        row = self.table.rowCount()
        delete_index = self.input_delete_row.text()
        
        if delete_index == '':
            index = row - 1
        else:
            index = int(delete_index) - 1

            if index >= row:
                print("invaild remove row")
                return

        if index >= 0:
            if self.table.item(index , 0).text() != "": # 刪除成人的列
                adult_name = re.findall("[a-zA-Z]+", self.table.item(index , 0).text())[0] # 找到adult的名字 ex: apple1 => apple
                adult_num = int(re.findall("[0-9]+", self.table.item(index , 0).text())[0]) # 找到adult的名字後面的數字 ex: apple1 => 1
                count = 0

                for i in range(index + 1 , row): # range => index + 1 ~ (rowcount - 1) , 將後面相同編號的數字都 - 1
                    if adult_name in self.table.item(i , 0).text():
                        item = QtWidgets.QTableWidgetItem()
                        item.setText(adult_name + str(adult_num))
                        item.setFlags(QtCore.Qt.ItemIsEnabled)
                        self.table.setItem(i , 0 , item)
                        adult_num = adult_num + 1
                
                for i in range(row): # range => 0 ~ (rowcount - 1) 檢查要不要從adult_list剔除adult
                    if adult_name in self.table.item(i , 0).text():
                        count = count + 1
                
                if count == 1: # 此adult只剩一句話，把他從adult_list中刪除
                    self.adult_list.remove(adult_name)     # 從adult_list中刪除
                    self.combobox_adult_name.clear()  # 從combobox中刪除

                    for i in self.adult_list:
                        self.combobox_adult_name.addItem(i)

            elif self.table.item(index , 3).text() != "": # 刪除兒童的列
                for i in range(index , row): # range => index ~ (rowcount - 1) , 將後面的數字都 - 1
                    if self.table.item(i , 3).text() != "":
                        item = QtWidgets.QTableWidgetItem()
                        item.setText(str(int(self.table.item(i , 3).text()) - 1))
                        item.setFlags(QtCore.Qt.ItemIsEnabled)
                        self.table.setItem(i , 3 , item)

            self.table.removeRow(index)
            self.clear_input()
    
    def clear_input(self):
        self.input_insert_row.clear()
        self.input_delete_row.clear()
        self.input_adult_sentence.clear()
        self.input_child_sentence.clear()
        self.input_tone.clear()
        self.checkbox_sentence.setChecked(False)

    def output(self):
        data = list()
        row = self.table.rowCount()
        column = 5

        for i in range(row):
            data.append([])
            for j in range(column):
                data[i].append(self.table.item(i , j).text())

        with open("output.csv" , "w" , newline = "") as f:
            writer = csv.writer(f)
            writer.writerow(["成人編號" , "成人語句" , "語境" , "兒童編號" , "兒童語句"])

            for i in range(row):
                writer.writerow(data[i])


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.main_label.setText(_translate("Form", "CLSA 轉錄表"))
        self.label_adult_name.setText(_translate("Form", "成人編號 :"))
        self.label_adult_sentence.setText(_translate("Form", "成人語句 : "))
        self.label_child_sentence.setText(_translate("Form", "兒童語句 : "))
        self.label_tone.setText(_translate("Form", "語境 : "))
        self.pb_insert.setText(_translate("Form", "新增"))
        self.label_writer.setText(_translate("Form", "轉錄者 : "))
        self.label_num.setText(_translate("Form", "個案編號 : "))
        self.pb_done.setText(_translate("Form", "確定"))
        self.label_insert.setText(_translate("Form", "新增在第幾列 (預設為最底下) : "))
        self.label_delete.setText(_translate("Form", "要刪除第幾列 (預設為最底下) :"))
        self.pb_delete.setText(_translate("Form", "刪除"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "成人編號"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "成人語句"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "語境"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "兒童編號"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("Form", "兒童語句"))
        self.checkbox_sentence.setText(_translate("Form", "此句話不採計"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
