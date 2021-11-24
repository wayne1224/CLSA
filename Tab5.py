import database.DatabaseApi as db
from PyQt5 import QtWidgets
from components.norm import NormModifyTab
from components.setting import SettingTab

class GeneralTab(QtWidgets.QTabWidget):
    def __init__(self):
        super(GeneralTab, self).__init__()
        self.tab0 = NormModifyTab()
        self.tab1 = SettingTab()

        self.addTab(self.tab0, "常模設定頁面")
        self.addTab(self.tab1, "其他設定頁面")

        self.setStyleSheet(open("QSS/Tab5.qss", "r").read())

