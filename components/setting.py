import database.DatabaseApi as db
import configparser
import requests
import json
import os
from PyQt5 import QtCore, QtGui, QtWidgets

class SettingTab(QtWidgets.QWidget):
    def __init__(self):
        super(SettingTab, self).__init__()
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.setLayout(self.verticalLayout)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_azure = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_azure.sizePolicy().hasHeightForWidth())
        self.label_azure.setSizePolicy(sizePolicy)
        self.label_azure.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_azure.setFont(font)
        self.label_azure.setObjectName("label")
        
        # Azure Title HBOX
        self.title_azure_hbox = QtWidgets.QHBoxLayout()
        self.title_azure_hbox.addItem(spacerItem)
        self.title_azure_hbox.addWidget(self.label_azure)
        self.title_azure_hbox.addItem(spacerItem)
        self.title_azure_hbox.addItem(spacerItem)

        self.verticalLayout_2.addLayout(self.title_azure_hbox)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(450, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.horizontalLayout.addWidget(self.lineEdit)

        # Azure Buttons
        self.updateBtn = QtWidgets.QPushButton()
        self.updateBtn.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.updateBtn.setFont(font)
        self.updateBtn.setObjectName("updateBtn")
        self.horizontalLayout.addWidget(self.updateBtn)

        self.deleteBtn = QtWidgets.QPushButton()
        self.deleteBtn.setMaximumSize(QtCore.QSize(16777215, 100))
        self.deleteBtn.setFont(font)
        self.deleteBtn.setObjectName("deleteBtn")
        self.horizontalLayout.addWidget(self.deleteBtn)
       
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_db = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_db.setFont(font)
        self.label_db.setObjectName("label_3")

        #DB Title HBOX
        self.title_db_hbox = QtWidgets.QHBoxLayout()
        self.title_db_hbox.addItem(spacerItem)
        self.title_db_hbox.addWidget(self.label_db)
        self.title_db_hbox.addItem(spacerItem)
        self.title_db_hbox.addItem(spacerItem)

        self.verticalLayout_3.addLayout(self.title_db_hbox)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.upload_db_btn = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.upload_db_btn.setFont(font)
        self.upload_db_btn.setObjectName("upload_db_btn")
        self.horizontalLayout_4.addWidget(self.upload_db_btn)
        self.download_db_btn = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.download_db_btn.setFont(font)
        self.download_db_btn.setObjectName("download_db_btn")
        self.horizontalLayout_4.addWidget(self.download_db_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        # self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # self.label_4 = QtWidgets.QLabel()
        # font = QtGui.QFont()
        # font.setFamily("微軟正黑體")
        # font.setPointSize(14)
        # self.label_4.setFont(font)
        # self.label_4.setObjectName("label_4")
        # self.horizontalLayout_3.addWidget(self.label_4)
        # self.pushButton_3 = QtWidgets.QPushButton()
        # font = QtGui.QFont()
        # font.setFamily("微軟正黑體")
        # font.setPointSize(14)
        # self.pushButton_3.setFont(font)
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.horizontalLayout_3.addWidget(self.pushButton_3)
        # self.pushButton_2 = QtWidgets.QPushButton()
        # font = QtGui.QFont()
        # font.setFamily("微軟正黑體")
        # font.setPointSize(14)
        # self.pushButton_2.setFont(font)
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.horizontalLayout_3.addWidget(self.pushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_3.addItem(spacerItem3)
        # self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)

        #Signal deleteBtn
        self.updateBtn.clicked.connect(self.update_STT_key)
        self.deleteBtn.clicked.connect(self.delete_STT_key)
        self.upload_db_btn.clicked.connect(self.upload_db)
        self.download_db_btn.clicked.connect(self.download_db)

        self.retranslateUi()
        self.setStyleSheet(open("./QSS/setting.qss", "r").read())

    def get_STT_key(self):
        cf = configparser.ConfigParser()
        cf.read("config.ini") 
        key = cf.get("STT", "key")
        self.lineEdit.setText(key)
       
    def update_STT_key(self):
        key = self.lineEdit.text()

        url = "https://eastus.api.cognitive.microsoft.com/sts/v1.0/issueToken"
        headers = {'Ocp-Apim-Subscription-Key': key, 'Content-type': 'application/x-www-form-urlencoded', 'Content-Length': '0'}
        r = requests.post(url, headers=headers)
        if r.status_code != 200:
            QtWidgets.QMessageBox.warning(self, '警告',"<p style='font-size:12pt;'>金鑰無效<br\>請重新輸入</p>", QtWidgets.QMessageBox.Ok)
            self.get_STT_key()
            return

        cf = configparser.ConfigParser()
        cf.read("config.ini") 
        cf.set("STT", "key", key)
        fh = open("config.ini", 'w')
        cf.write(fh)  # 把要修改的節點的內容寫到檔案中
        fh.close()

        QtWidgets.QMessageBox.information(self, '通知',"<p style='font-size:12pt;'>更新成功</p>", QtWidgets.QMessageBox.Ok)

    def delete_STT_key(self):
        close = QtWidgets.QMessageBox.question(self,
                        "金鑰",
                        '<p style="font-size:12pt; color: #3778bf;">確定要刪除嗎?</p>\n',
                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if close == QtWidgets.QMessageBox.Yes :
            cf = configparser.ConfigParser()
            cf.read("config.ini") 
            cf.set("STT", "key", "")
            fh = open("config.ini", 'w')
            cf.write(fh)  # 把要修改的節點的內容寫到檔案中
            fh.close()

            QtWidgets.QMessageBox.information(self, '通知',"<p style='font-size:12pt;'>刪除成功</p>", QtWidgets.QMessageBox.Ok)
            self.get_STT_key()
    
    def upload_db(self):
        try:
            filePath, _ = QtWidgets.QFileDialog.getOpenFileName(None,
                                            "開啟檔案",
                                            "",
                                            "json files(*.json)")
        except:
            pass

        try:
            with open(filePath, 'r', encoding='utf8') as json_file:
                data = json.load(json_file)

            #匯入資料庫                    
            result = db.importCLSA(data['childData'], data['document'], data['norm'])

            if result:
                QtWidgets.QMessageBox.information(self, '通知',"<p style='font-size:12pt;'>上傳成功</p>", QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.warning(self, '通知',"<p style='font-size:12pt;'>上傳失敗<br/>格式錯誤，請重新選擇檔案</p>", QtWidgets.QMessageBox.Ok)
        except:
            pass
    
    def download_db(self):
        # 選存檔位置
        try:
            filePath, _ = QtWidgets.QFileDialog.getSaveFileName(None,
                                            "開啟檔案",
                                            "db.json",
                                            "json files(*.json)")
        except:
            pass

        output = db.exportCLSA()

        try:
            with open(f'{filePath}', 'w', encoding='utf8') as json_file:
                json.dump(output, json_file, ensure_ascii=False, indent=2)
            QtWidgets.QMessageBox.information(self, '通知',"<p style='font-size:12pt;'>下載成功</p>", QtWidgets.QMessageBox.Ok)
        except:
            QtWidgets.QMessageBox.warning(self, '通知',"<p style='font-size:12pt;'>下載失敗<br/>請再試一次</p>", QtWidgets.QMessageBox.Ok)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.label_azure.setText(_translate("", "語音轉文字服務"))
        self.label_2.setText(_translate("", "  金鑰: "))
        self.updateBtn.setText(_translate("", "    更改    "))
        self.deleteBtn.setText(_translate("", "    刪除    "))
        self.label_db.setText(_translate("", "資料管理"))
        self.label_5.setText(_translate("", "  本系統資料: "))
        self.upload_db_btn.setText(_translate("", "    上傳    "))
        self.download_db_btn.setText(_translate("", "    下載    "))
        #self.label_4.setText(_translate("", "孩童資料: "))
        # self.pushButton_3.setText(_translate("", "    上傳    "))
        # self.pushButton_2.setText(_translate("", "    下載    "))