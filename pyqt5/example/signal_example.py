# @Time    : 2021/5/18 13:45
# @Author  : lucas
# @File    : signal_example.py
# @Project : pyqt
# @Software: PyCharm
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
import time


class Communicate(QObject):
    closeApp = pyqtSignal()


class Example(QMainWindow):
    closeApp = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.showMsg)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.lable = QLabel("hello", self)
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()

    def showMsg(self):
        print("ok")
        self.lable.setText("hahah")
        QApplication.processEvents()
        time.sleep(1)
        self.lable.setText("wait")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())