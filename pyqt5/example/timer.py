# # @Time    : 2021/3/22 10:52
# # @Author  : lucas
# # @File    : timer.py
# # @Project : pyqt
# # @Software: PyCharm
# import sys
# from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel
# from PyQt5.QtCore import QTimer,QDateTime
#
# class WinForm(QWidget):
#     def __init__(self,parent=None):
#         super(WinForm, self).__init__(parent)
#         self.setWindowTitle('QTimer example')
#
#         self.listFile=QListWidget()
#         self.label=QLabel('Label')
#         self.startBtn=QPushButton('Start')
#         self.endBtn=QPushButton('Stop')
#
#         layout=QGridLayout()
#
#         self.timer=QTimer()
#         self.timer.timeout.connect(self.showTime)
#
#         layout.addWidget(self.label,0,0,1,2)
#         layout.addWidget(self.startBtn,1,0)
#         layout.addWidget(self.endBtn,1,1)
#
#         self.startBtn.clicked.connect(self.startTimer)
#         self.endBtn.clicked.connect(self.endTimer)
#
#         self.setLayout(layout)
#
#     def showTime(self):
#         time=QDateTime.currentDateTime()
#         timeDisplay=time.toString('yyyy-MM-dd hh:mm:ss dddd')
#         self.label.setText(timeDisplay)
#
#     def startTimer(self):
#         self.timer.start(1000)
#         self.startBtn.setEnabled(False)
#         self.endBtn.setEnabled(True)
#
#     def endTimer(self):
#         self.timer.stop()
#         self.startBtn.setEnabled(True)
#         self.endBtn.setEnabled(False)
#
# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     form=WinForm()
#     form.show()
#     sys.exit(app.exec_())





import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# Define class to create the stop watch
class StopWatchWindow(QMainWindow):

    def __init__(self):
        # Call the parent constructor
        super().__init__()

        # Set the title of the window
        self.setWindowTitle("Stop Watch using QTimer")
        # Set the geometry for the window
        self.setGeometry(100, 100, 300, 200)

        # Set the necessary variables
        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.count = '00'
        self.startWatch = False

        # Create label to display the watch
        self.label = QLabel(self)
        # Set geometry for the label
        self.label.setGeometry(100, 40, 150, 70)


        # Create start button
        self.start = QPushButton("Start", self)
        # Set geometry to the start button
        self.start.setGeometry(50, 120, 100, 40)
        # Call start() method when the start button is clicked
        self.start.pressed.connect(self.Start)

        # Create reset button
        resetWatch = QPushButton("Reset", self)
        # Set geometry to the stop button
        resetWatch.setGeometry(160, 120, 100, 40)
        # Call reset() method when the reset button is clicked
        resetWatch.pressed.connect(self.Reset)


        # Create timer object
        timer = QTimer(self)
        # Add a method with the timer
        timer.timeout.connect(self.showCounter)
        # Call start() method to modify the timer value
        timer.start(100)

        # Move the position of the window
        self.move(900, 400)
        # Display the window
        self.show()

    # Define a method to modify the values of minutes and seconds based on the timer value
    def showCounter(self):
        # Check the value of startWatch  variable to start or stop the Stop Watch
        if self.startWatch:
            # Increment counter by 1
            self.counter += 1

            # Count and set the time counter value
            cnt = int((self.counter/10 - int(self.counter/10))*10)
            self.count = '0' + str(cnt)

            # Set the second value
            if int(self.counter/10) < 10 :
                self.second = '0' + str(int(self.counter / 10))
            else:
                self.second = str(int(self.counter / 10))
                # Set the minute value
                if self.counter / 10 == 60.0 :
                    self.second == '00'
                    self.counter = 0
                    min = int(self.minute) + 1
                    if min < 10 :
                        self.minute = '0' + str(min)
                    else:
                        self.minute = str(min)


        # Merge the mintue, second and count values
        text = self.minute + ':' + self.second + ':' + self.count
        # Display the stop watch values in the label
        self.label.setText('<h1 style="color:blue">' + text + '</h1>')

    # Define method to handle the start button
    def Start(self):
        # Set the caption of the start button based on previous caption
        if self.start.text() == 'Stop':
            self.start.setText('Resume')
            self.startWatch = False
        else:
            # making startWatch to true
            self.startWatch = True
            self.start.setText('Stop')

    # Define method to handle the reset button
    def Reset(self):
        self.startWatch = False
        # Reset all counter variables
        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.count = '00'
        # Set the initial values for the stop watch
        self.label.setText(str(self.counter))

# Create app object and run the app
app = QApplication(sys.argv)
stopWt = StopWatchWindow()
app.exec()


# def start_timer(slot, count=1, interval=1000):
#     counter = 0
#
#     def handler():
#         nonlocal counter
#         counter += 1
#         slot(counter)
#         if counter >= count:
#             timer.stop()
#             timer.deleteLater()
#     timer = QtCore.QTimer()
#     timer.timeout.connect(handler)
#     timer.start(interval)
#
#
# def timer_func(count):
#     print('Timer:', count)
#     if count >= 5:
#         pass
# start_timer(timer_func, 10000)