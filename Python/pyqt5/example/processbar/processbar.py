# @Time    : 2021/4/13 11:16
# @Author  : lucas
# @File    : processbar.py
# @Project : pyqt
# @Software: PyCharm
# import sys
# from PyQt5.QtCore import QTimer
# from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar
# from PyQt5.QtCore import Qt
#
#
# class Example(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.pbar = QProgressBar(self)
#         self.pbar.setGeometry(30, 40, 200, 25)
#         self.pbar.setValue(50)
#
#         self.setWindowTitle("QT Progressbar Example")
#         self.setGeometry(32, 32, 320, 200)
#         self.show()
#
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.handleTimer)
#         self.timer.start(1000)
#
#     def handleTimer(self):
#         value = self.pbar.value()
#         if value < 100:
#             value = value + 1
#             self.pbar.setValue(value)
#         else:
#             self.timer.stop()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# import sys
# import time
# from PyQt5.QtWidgets import (QApplication, QDialog,
#                              QProgressBar, QPushButton)
#
# TIME_LIMIT = 100
#
#
# class Actions(QDialog):
#     """
#     Simple dialog that consists of a Progress Bar and a Button.
#     Clicking on the button results in the start of a timer and
#     updates the progress bar.
#     """
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('Progress Bar')
#         self.progress = QProgressBar(self)
#         self.progress.setGeometry(0, 0, 300, 25)
#         self.progress.setMaximum(100)
#         self.button = QPushButton('Start', self)
#         self.button.move(0, 30)
#         self.show()
#
#         self.button.clicked.connect(self.onButtonClick)
#
#     def onButtonClick(self):
#         count = 0
#         while count < TIME_LIMIT:
#             count += 2
#             time.sleep(1)
#             self.progress.setValue(count)
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Actions()
#     sys.exit(app.exec_())


import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QDialog,
                             QProgressBar, QPushButton)

TIME_LIMIT = 100


class External(QThread):
    """
    Runs a counter thread.
    """
    countChanged = pyqtSignal(int)

    # def __init__(self):
    #     super(External, self).__init__()
    #
    # def __del__(self):
    #     self.wait()

    def run(self):
        count = 0
        while count < TIME_LIMIT:
            count += 1
            time.sleep(1)
            self.countChanged.emit(count)


class Actions(QDialog):
    """
    Simple dialog that consists of a Progress Bar and a Button.
    Clicking on the button results in the start of a timer and
    updates the progress bar.
    """

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Progress Bar')
        self.progress = QProgressBar(self)
        self.progress.setGeometry(0, 0, 300, 25)
        self.progress.setMaximum(100*100)
        self.button = QPushButton('Start', self)
        self.button.move(0, 30)
        self.show()

        self.button.clicked.connect(self.onButtonClick)

    def onButtonClick(self):
        self.calc = External()
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()

    def onCountChanged(self, value):
        new = (value +0.3)*100
        self.progress.setValue(new)
        self.progress.setFormat("%.02f%%" % (value+0.3))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Actions()
    sys.exit(app.exec_())