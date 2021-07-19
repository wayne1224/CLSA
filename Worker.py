from PyQt5 import QtCore

class Worker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(int)

    def __init__(self, fn):
        super(Worker, self).__init__()
        self.func = fn

    def run(self):
        self.func()
        self.finished.emit()