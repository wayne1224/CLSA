import sys
import database.DBapi
from PyQt5 import QtCore, QtGui, QtWidgets
from DistilTag import DistilTag  
from statistics import mean
from datetime import datetime

class AnalysisTab(QtWidgets.QWidget):
    def __init__(self):
        super(AnalysisTab, self).__init__()
        # self.setObjectName("Form")
        # self.resize(1080, 868)
        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)
        #initial Bold font
        font = QtGui.QFont()
        font.setBold(True)
        self.tableWidget = QtWidgets.QTableWidget(self)
        #self.tableWidget.setGeometry(QtCore.QRect(270, 30, 481, 761))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(24)
        layout.addWidget(self.tableWidget, 0, 0)
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
        self.caseID = ''
        self.date = None

    @QtCore.pyqtSlot(dict)
    def getKey(self, key):
        print(key)
        if key != None: 
            self.caseID = key['caseID']
            self.date = key['date']

    @QtCore.pyqtSlot(list)
    def getChildUtterance(self, utterance):
        if utterance == None:
            return 
        utterance = list(sorted(utterance, key = len, reverse = True))
        wordCount = [0]*len(utterance) #統計每句詞數
        charCount = [len(i) for i in utterance]
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

        #開始進行斷詞
        tagger = DistilTag()
        tagged = tagger.tag(utterStr)
        print(tagged)
        i = 0 #每句話的index
        for sent in tagged:
            for pair in sent:
                wordCount[i] += 1 #統計每句詞數
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

        #呼叫資料庫
        print('caseID:',self.caseID)
        print('Date:',self.date)
        database.DBapi.updateAnaylsis(self.caseID, self.date, Analysis)

        #顯示在Table
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
        self.tableWidget.item(12,3).setText(str(Analysis['Content']['percentage']*100)+'%')
        self.tableWidget.item(13,3).setText(str(Analysis['Function']['P']))
        self.tableWidget.item(14,3).setText(str(Analysis['Function']['C']))
        self.tableWidget.item(15,3).setText(str(Analysis['Function']['T']))
        self.tableWidget.item(16,3).setText(str(Analysis['Function']['I']))
        self.tableWidget.item(17,3).setText(str(Analysis['Function']['percentage']*100)+'%')
        #VOCD-w
        #VOCD-c
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen = AnalysisTab()
    screen.show()
    sys.exit(app.exec_())
