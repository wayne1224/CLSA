import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from Mytable import Mytable
from Tab2 import Tab2
from myform import Myform
class TabDemo(QtWidgets.QTabWidget):
    def __init__(self,parent=None):
        super(TabDemo, self).__init__(parent)

        self.resize(1393, 815)
    
        #创建3个选项卡小控件窗口
        self.tab1=Myform()
        self.tab2=Mytable()
        self.tab3=QtWidgets.QWidget()



        #将三个选项卡添加到顶层窗口中
        self.addTab(self.tab1, "CLSA 收錄表")
        self.addTab(self.tab2, "CLSA 轉錄表")
        self.addTab(self.tab3, "Tab 3")

        #每个选项卡自定义的内容
        self.setStyleSheet( "QTabBar::tab { height: 40px; width: 250px; }")

   
    #     self.tab3UI()

    # def tab3UI(self):
    #     #水平布局
    #     layout=QHBoxLayout()

    #     #添加控件到布局中
    #     layout.addWidget(QLabel('科目'))
    #     layout.addWidget(QCheckBox('物理'))
    #     layout.addWidget(QCheckBox('高数'))

    #     #设置小标题与布局方式
    #     self.setTabText(2,'教育程度')
    #     self.tab3.setLayout(layout)
if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    demo=TabDemo()
    demo.show()
    sys.exit(app.exec_())
