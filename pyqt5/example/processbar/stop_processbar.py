# @Time    : 2021/5/20 10:04
# @Author  : lucas
# @File    : stop_processbar.py
# @Project : pyqt
# @Software: PyCharm

from PyQt5.QtWidgets import (
    QWidget, QApplication, QProgressBar, QMainWindow,
    QHBoxLayout, QPushButton
)
from PyQt5.QtCore import (
    Qt, QObject, pyqtSignal, pyqtSlot, QRunnable, QThreadPool
)
import time


class WorkerSignals(QObject):
    progress = pyqtSignal(int)


class JobRunner(QRunnable):
    signals = WorkerSignals()

    def __init__(self):
        super().__init__()

        self.is_paused = False
        self.is_killed = False

    @pyqtSlot()
    def run(self):
        for n in range(100):
            self.signals.progress.emit(n + 1)
            time.sleep(0.1)

            while self.is_paused:
                time.sleep(0)

            if self.is_killed:
                break

    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False

    def kill(self):
        self.is_killed = True


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Some buttons
        w = QWidget()
        l = QHBoxLayout()
        w.setLayout(l)

        btn_stop = QPushButton("Stop")
        btn_pause = QPushButton("Pause")
        btn_resume = QPushButton("Resume")

        l.addWidget(btn_stop)
        l.addWidget(btn_pause)
        l.addWidget(btn_resume)

        self.setCentralWidget(w)

        # Create a statusbar.
        self.status = self.statusBar()
        self.progress = QProgressBar()
        self.status.addPermanentWidget(self.progress)

        # Thread runner
        self.threadpool = QThreadPool()

        # Create a runner
        self.runner = JobRunner()
        self.runner.signals.progress.connect(self.update_progress)
        self.threadpool.start(self.runner)

        btn_stop.pressed.connect(self.runner.kill)
        btn_pause.pressed.connect(self.runner.pause)
        btn_resume.pressed.connect(self.runner.resume)

        self.show()

    def update_progress(self, n):
        self.progress.setValue(n)


app = QApplication([])
w = MainWindow()
app.exec_()



# import threading, requests
# import tkinter as tk
#
#
# def switch_thread_states(widget):
#     # or whatever pause / resume text you wish for the widget / button
#     if widget['text'] == 'Pause':
#         widget['text'] = 'Resume'
#     else:
#         widget['text'] = 'Pause'
#     for thread in threading.enumerate():
#         if not isinstance(thread, threading._MainThread):
#             if thread.paused:
#                 thread.resume()
#             else:
#                 thread.pause()
#
#
# class PauseableThread(threading.Thread):
#
#     def __init__(self, urls):
#
#         threading.Thread.__init__(self)
#         self.urls = urls
#         self.paused = False
#         self.pause_cond = threading.Condition(threading.Lock())
#
#     def run(self):
#
#         for url in self.urls:
#
#             with self.pause_cond:
#                 while self.paused:
#                     self.pause_cond.wait()
#             # make requests here or whatever you're doing
#             requests.get(url, headers={'User-Agent': 'Mozilla/5.0 .....'})
#
#     def pause(self):
#
#         self.paused = True
#         self.pause_cond.acquire()
#
#     def resume(self):
#
#         self.paused = False
#         self.pause_cond.notify()
#         self.pause_cond.release()
