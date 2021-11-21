from PyQt5 import QtCore
import sys

class Worker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(int)

    def __init__(self, fn):
        super(Worker, self).__init__()
        self.func = fn

    def run(self):
        self.func()
        self.finished.emit()

class Worker_DB(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(int)

    def __init__(self, fn):
        super(Worker_DB, self).__init__()
        self.func = fn

    def run(self):
        if self.func() == True:
            self.finished.emit()
        else:
            print("Database Failed")
            quit()
        