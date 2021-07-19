import sys
import database.DatabaseApi as db
import time
import numpy as np
import random
from PyQt5 import QtCore, QtGui, QtWidgets
import DistilTag  
from statistics import mean
from datetime import datetime
from sympy import solve, symbols, sqrt, sympify
from functools import partial
from Worker import Worker

class AnalysisTab(QtWidgets.QWidget):
    procMain = QtCore.pyqtSignal(int)
    def __init__(self):
        super(AnalysisTab, self).__init__()
        # self.setObjectName("Form")
        # self.resize(1080, 868)
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        #add Header 
        self.headerLayout = QtWidgets.QHBoxLayout()
        # self.horizontalLayout = QtWidgets.QHBoxLayout()
        # self.horizontalLayout.setObjectName("horizontalLayout")
        # self.label_2 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        # self.label_2.setFont(font)
        # self.label_2.setObjectName("label_2")
        # self.horizontalLayout.addWidget(self.label_2)
        # self.transcriber_label = QtWidgets.QLabel()
        # font = QtGui.QFont()
        # font.setPointSize(14)
        # self.transcriber_label.setFont(font)
        # self.transcriber_label.setText("")
        # self.transcriber_label.setObjectName("transcriber_label")
        # self.horizontalLayout.addWidget(self.transcriber_label)
        # #self.headerLayout.addLayout(self.horizontalLayout)
        # spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        # self.headerLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.caseID_label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        self.caseID_label.setFont(font)
        self.caseID_label.setText("")
        self.caseID_label.setObjectName("caseID_label")
        self.horizontalLayout_2.addWidget(self.caseID_label)
        self.headerLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.headerLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.date_label = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_label.sizePolicy().hasHeightForWidth())
        self.date_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.date_label.setFont(font)
        self.date_label.setText("")
        self.date_label.setObjectName("date_label")
        self.horizontalLayout_3.addWidget(self.date_label)
        self.headerLayout.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.headerLayout.addItem(spacerItem)
        layout.addLayout(self.headerLayout)

        #add Space
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        layout.addItem(spacerItem)

        #initial Bold font
        font = QtGui.QFont()
        font.setBold(True)
        self.tableWidget = QtWidgets.QTableWidget(self)
        #self.tableWidget.setGeometry(QtCore.QRect(270, 30, 481, 761))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(24)
        layout.addWidget(self.tableWidget)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter) #字置中
        item.setFont(font) #Bold
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item.setTextAlignment(QtCore.Qt.AlignCenter) #字置中
        item.setFont(font) #Bold
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter) #字置中置頂
        item.setFont(font) #Bold
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter) #字置中置頂
        item.setFont(font) #Bold
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter) #字置中置頂
        item.setFont(font) #Bold
        self.tableWidget.setItem(13, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter) #字置中置頂
        item.setFont(font) #Bold
        self.tableWidget.setItem(13, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(16, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(17, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(18, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(18, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(19, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(20, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(20, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(21, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(22, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(22, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(23, 2, item)
        
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.retranslateUi()
        #setSpan
        self.tableWidget.setSpan(0,0,1,3)
        self.tableWidget.setSpan(1,0,2,2)
        self.tableWidget.setSpan(3,0,2,2)
        self.tableWidget.setSpan(5,0,8,1)
        self.tableWidget.setSpan(5,1,8,1)
        self.tableWidget.setSpan(13,0,5,1)
        self.tableWidget.setSpan(13,1,5,1)
        self.tableWidget.setSpan(18,0,2,2)
        self.tableWidget.setSpan(20,0,2,2)
        self.tableWidget.setSpan(22,0,2,2)
        self.tableWidget.setSpan(3,2,2,2)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        #self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        #self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        #QtCore.QMetaObject.connectSlotsByName(Form)
        # 設字置中
        for i in range(1,24):
            if i == 3 or i == 4:
                continue
            else:
                self.tableWidget.item(i,2).setTextAlignment(QtCore.Qt.AlignCenter)
                #補上面的沒init的cell
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(i, 3, item)
        
        #Class內變數宣告
        self.caseID = ''
        self.date = None
        self.isEdit = False

    @QtCore.pyqtSlot()
    def setEdit(self):
        self.isEdit = True
    
    def getEdit(self):
        return self.isEdit

    @QtCore.pyqtSlot(dict)
    def getDoc(self, key):
        if key != None:
            if '_id' in key: #若傳入整個document
                self.clearContent()
                if key['transcription']['analysis']:
                    self.setContent(key['transcription']['analysis'])
            else:
                self.caseID = key['caseID']
                self.date = key['date']
                self.caseID_label.setText(str(self.caseID))
                date_time = self.date.strftime("%Y-%m-%d %H:%M")
                self.date_label.setText(date_time)

                #呼叫過去的Analysis
                analysis = db.findAnalysis(self.caseID,self.date)
                if analysis:
                    self.clearContent()
                    self.setContent(analysis)
                else:
                    self.clearContent()
                    print("No data")
            

    @QtCore.pyqtSlot(list)
    def getChildUtterance(self, utterance):
        #Create a QThread object
        self.thread = QtCore.QThread()
        #Create a worker object
        self.worker = Worker(partial(self.analyze_and_setContent,utterance))
        #Move worker to the thread
        self.worker.moveToThread(self.thread)
        #Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        #self.worker.progress.connect(self.reportProgress)
        #Start the thread
        self.thread.start()

    def analyze_and_setContent(self,utterance):
        self.isEdit = False
        if not utterance:
            #傳signal給MainWindow
            self.procMain.emit(4)
            return 
        #try:
        print(utterance)
        utterance = list(sorted(utterance, key = len, reverse = True))
        wordArray = [] #有效詞
        charArray = [] #有效字
        utterStr = ""
        Analysis = {
            'charCount':0,
            'wordCount':0,
            'Content':{
                'N':0,
                'V':0,
                'VH':0,
                'Neu':0,
                'Nf':0,
                'Nh':0,
                'D':0,
                'percentage':0.0,
                'sum':0
            },
            'Function':{
                'P':0,
                'C':0,
                'T':0,
                'I':0,
                'percentage':0.0,
                'sum':0
            },
            'VOCD-w':0.0,
            'VOCD-c':0.0,
            'MLU-w':0,
            'MLU-c':0,
            'MLU5-w':0,
            'MLU5-c':0
        }

        #將句子合併
        for i in utterance: 
            utterStr += i
            utterStr += '。'
            
        #開始進行斷詞
        tagger = DistilTag.DistilTag()
        tagged = tagger.tag(utterStr)
        print(tagged)
        wordCount = [0]*len(tagged) #統計每句詞數
        charCount = [len(i) + 1 for i in tagged]
        i = 0 #每句話的index
        for sent in tagged:
            print(i)
            #charArray.extend(utterance[i])
            for pair in sent:
                wordCount[i] += 1 #統計每句詞數
                wordArray.append(pair[0]) #收集詞
                charArray.append(len(pair[0]))
                #統計實詞
                if pair[1] == 'Neu':
                    Analysis['Content']['Neu'] += 1
                elif pair[1] == 'Nf' or pair[1] == 'Nequ':
                    Analysis['Content']['Nf'] += 1
                elif pair[1] == 'Nh' or pair[1] == 'Nep':
                    Analysis['Content']['Nh'] += 1
                elif pair[1].startswith('N'):
                    Analysis['Content']['N'] += 1
                elif pair[1] == 'VH' or pair[1] == 'A':
                    Analysis['Content']['VH'] += 1
                elif pair[1].startswith('V') or pair[1] == 'SHI':
                    Analysis['Content']['V'] += 1
                elif pair[1].startswith('D') and pair[1] != 'DASHCATEGORY':
                    Analysis['Content']['D'] += 1
                #統計虛詞
                elif pair[1] == 'P':
                    Analysis['Function']['P'] += 1
                elif pair[1].startswith('Ca') or pair[1].startswith('Cb'):
                    Analysis['Function']['C'] += 1
                elif pair[1].startswith('T'):
                    Analysis['Function']['T'] += 1
                elif pair[1] == 'I':
                    Analysis['Function']['I'] += 1
                else:
                    wordCount[i] -= 1
                    charCount[i] -= 1
                    # if ord(charArray[-1]) + 65248 == ord(wordArray.pop()):  #去除無效詞
                    #     charArray.pop() #去除無效字
            i += 1
                    
        #設Dict值
        Analysis['charCount'] = sum(charCount) #總字數
        Analysis['wordCount'] = sum(wordCount) #總詞數
        Analysis['Content']['percentage'] = round(sum(Analysis['Content'].values())/sum(wordCount),2) #實詞比例
        Analysis['Function']['percentage'] = round(sum(Analysis['Function'].values())/sum(wordCount),2) #虛詞比例
        Analysis['Content']['sum'] = int(sum(Analysis['Content'].values())) #總實詞
        Analysis['Function']['sum'] = int(sum(Analysis['Function'].values())) #總虛詞
        Analysis['MLU-w'] = round(mean(wordCount),2)
        Analysis['MLU-c'] = round(mean(charCount),2)
        Analysis['MLU5-w'] = round(mean(wordCount[:5]),2)
        Analysis['MLU5-c'] = round(mean(charCount[:5]),2)
        try:
            Analysis['VOCD-w'] = round(self.getVOCD(wordArray),2)
        except:
            Analysis['VOCD-w'] = self.getVOCD(wordArray)
        try:
            Analysis['VOCD-c'] = round(self.getVOCD(charArray),2)
        except:
            Analysis['VOCD-c'] = self.getVOCD(charArray)

        print(wordArray)
        print(charArray)

        #呼叫資料庫
        print('caseID:',self.caseID)
        print('Date:',type(self.date))
        db.updateAnalysis(self.caseID, self.date, Analysis)

        #通知彙整完整
        #informBox = QtWidgets.QMessageBox.information(self, '通知','資料彙整並儲存成功', QtWidgets.QMessageBox.Ok)

        #顯示在Table
        self.setContent(Analysis)

        #傳signal給MainWindow
        self.procMain.emit(3)

        # except Exception as e:
        #     #傳signal給MainWindow
        #     self.procMain.emit(4)
        #     print(e)

    def getTTR(self,a):
        return len(set(a)) / len(a)

    def getD(self,TTR,N):
        D = symbols('x')
        return solve(D/N * (sqrt(1 + 2*N/D) - 1) - TTR , D)[0]

    def getVOCD(self,token):
        if len(token) < 50:
            return "樣本數不足"

        TTR = np.zeros(100)
        avgTTR = np.zeros(16)
        D = np.zeros(16)
        avgD = np.zeros(3)

        for i in range(3): #重複三次
            for N in range(35,51): #取Token數
                for j in range(100): #重複100次
                    TTR[j] = self.getTTR(random.sample(token,N)) #select subsample of N tokens at random and calculate TTR
                avgTTR[N - 35] = np.mean(TTR)
                D[N - 35] = self.getD(avgTTR[N - 35],N)
            avgD[i] = np.mean(D.flatten())
        return np.mean(avgD)

    @QtCore.pyqtSlot()
    def clearContent(self):
        self.caseID_label.setText('')
        self.date_label.setText('')
        
        self.tableWidget.item(1,3).setText('') 
        self.tableWidget.item(2,3).setText('') 
        self.tableWidget.item(5,1).setText('')
        self.tableWidget.item(13,1).setText('')
        self.tableWidget.item(5,3).setText('')
        self.tableWidget.item(6,3).setText('')
        self.tableWidget.item(7,3).setText('')
        self.tableWidget.item(8,3).setText('')
        self.tableWidget.item(9,3).setText('')
        self.tableWidget.item(10,3).setText('')
        self.tableWidget.item(11,3).setText('')
        self.tableWidget.item(12,3).setText('')
        self.tableWidget.item(13,3).setText('')
        self.tableWidget.item(14,3).setText('')
        self.tableWidget.item(15,3).setText('')
        self.tableWidget.item(16,3).setText('')
        self.tableWidget.item(17,3).setText('')
        self.tableWidget.item(18,3).setText('')
        self.tableWidget.item(19,3).setText('')
        self.tableWidget.item(20,3).setText('')
        self.tableWidget.item(21,3).setText('')
        self.tableWidget.item(22,3).setText('')
        self.tableWidget.item(23,3).setText('')

    def setContent(self,Analysis):
        self.tableWidget.item(1,3).setText(str(Analysis['charCount'])) #總字數
        self.tableWidget.item(2,3).setText(str(Analysis['wordCount'])) #總詞數
        self.tableWidget.item(5,1).setText(str(Analysis['Content']['sum'])) #總實詞
        self.tableWidget.item(13,1).setText(str(Analysis['Function']['sum'])) #總虛詞
        self.tableWidget.item(5,3).setText(str(Analysis['Content']['N']))
        self.tableWidget.item(6,3).setText(str(Analysis['Content']['V']))
        self.tableWidget.item(7,3).setText(str(Analysis['Content']['VH']))
        self.tableWidget.item(8,3).setText(str(Analysis['Content']['Neu']))
        self.tableWidget.item(9,3).setText(str(Analysis['Content']['Nf']))
        self.tableWidget.item(10,3).setText(str(Analysis['Content']['Nh']))
        self.tableWidget.item(11,3).setText(str(Analysis['Content']['D']))
        self.tableWidget.item(12,3).setText('{:.1%}'.format(Analysis['Content']['percentage']))
        self.tableWidget.item(13,3).setText(str(Analysis['Function']['P']))
        self.tableWidget.item(14,3).setText(str(Analysis['Function']['C']))
        self.tableWidget.item(15,3).setText(str(Analysis['Function']['T']))
        self.tableWidget.item(16,3).setText(str(Analysis['Function']['I']))
        self.tableWidget.item(17,3).setText('{:.1%}'.format(Analysis['Function']['percentage']))
        self.tableWidget.item(18,3).setText(str(Analysis['VOCD-w']))
        self.tableWidget.item(19,3).setText(str(Analysis['VOCD-c']))
        self.tableWidget.item(20,3).setText(str(Analysis['MLU-w']))
        self.tableWidget.item(21,3).setText(str(Analysis['MLU-c']))
        self.tableWidget.item(22,3).setText(str(Analysis['MLU5-w']))
        self.tableWidget.item(23,3).setText(str(Analysis['MLU5-c']))
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        #Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "兒童語言樣本各指標"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Form", "分析結果"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Form", "1.計算總字數及詞數"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("Form", "總字數"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("Form", "總詞數"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("Form", "3.計算實詞和虛詞"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("Form", "2.計算各類詞類數"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("Form", "實詞"))
        item = self.tableWidget.item(5, 2)
        item.setText(_translate("Form", "名詞（N）"))
        item = self.tableWidget.item(6, 2)
        item.setText(_translate("Form", "動詞（V）"))
        item = self.tableWidget.item(7, 2)
        item.setText(_translate("Form", "形容詞（A）"))
        item = self.tableWidget.item(8, 2)
        item.setText(_translate("Form", "數詞（Neu）"))
        item = self.tableWidget.item(9, 2)
        item.setText(_translate("Form", "量詞（Nf）"))
        item = self.tableWidget.item(10, 2)
        item.setText(_translate("Form", "代詞（Nh）"))
        item = self.tableWidget.item(11, 2)
        item.setText(_translate("Form", "副詞（D）"))
        item = self.tableWidget.item(12, 2)
        item.setText(_translate("Form", "實詞之總百分比"))
        item = self.tableWidget.item(13, 0)
        item.setText(_translate("Form", "虛詞"))
        item = self.tableWidget.item(13, 2)
        item.setText(_translate("Form", "介詞（P）"))
        item = self.tableWidget.item(14, 2)
        item.setText(_translate("Form", "連詞（C）"))
        item = self.tableWidget.item(15, 2)
        item.setText(_translate("Form", "助詞（T）"))
        item = self.tableWidget.item(16, 2)
        item.setText(_translate("Form", "嘆詞（I）"))
        item = self.tableWidget.item(17, 2)
        item.setText(_translate("Form", "虛詞之總百分比"))
        item = self.tableWidget.item(18, 0)
        item.setText(_translate("Form", "4.計算詞彙多樣性/字的多樣性"))
        item = self.tableWidget.item(18, 2)
        item.setText(_translate("Form", "VOCD-w"))
        item = self.tableWidget.item(19, 2)
        item.setText(_translate("Form", "VOCD-c"))
        item = self.tableWidget.item(20, 0)
        item.setText(_translate("Form", "5.計算平均語句長度（MLU）"))
        item = self.tableWidget.item(20, 2)
        item.setText(_translate("Form", "MLU-w"))
        item = self.tableWidget.item(21, 2)
        item.setText(_translate("Form", "MLU-c"))
        item = self.tableWidget.item(22, 0)
        item.setText(_translate("Form", "6.計算最長五個語句之平均語句長度（MLU5）"))
        item = self.tableWidget.item(22, 2)
        item.setText(_translate("Form", "MLU5-w"))
        item = self.tableWidget.item(23, 2)
        item.setText(_translate("Form", "MLU5-c"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        #self.label_2.setText(_translate("Form", "轉錄者："))
        self.label_3.setText(_translate("Form", "個案編號："))
        self.label_5.setText(_translate("Form", "收錄日期："))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen = AnalysisTab()
    screen.show()
    sys.exit(app.exec_())
