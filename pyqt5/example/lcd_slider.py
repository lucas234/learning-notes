# @Time    : 2021/3/3 17:11
# @Author  : lucas
# @File    : test.py
# @Project : Endtest
# @Software: PyCharm

a = [1, 3, 2, 4, 2, 4, 4]

# print(Counter(a))
print({i: a.count(i) for i in a})

def triangles():
    N=[1]
    while True:
        yield N
        S=N[:]
        S.append(0) #将list添加0，作为最后一个元素，长度增加1
        N=[S[i-1]+S[i] for i in range(len(S))]

a = [1]
r = [1]
n = 2
triangle = [[1]]
while n<10:
    r = [1]
    for i in range(len(a)-1):
        r.append(a[i]+a[i+1])
    r.append(1)
    n += 1
    a = r
    triangle.append(a)
print(triangle)





import sys
from PyQt5.QtWidgets import QWidget, \
  QPushButton, \
  QToolTip, \
  QMessageBox, \
  QApplication, \
  QDesktopWidget, \
  QMainWindow, \
  QAction, \
  qApp, \
  QLCDNumber, \
  QSlider, \
  QVBoxLayout, \
  QHBoxLayout
from PyQt5.QtCore import Qt, \
  QObject, \
  pyqtSignal
from PyQt5.QtGui import QFont, \
  QIcon


class Communicate(QObject):
  closeApp = pyqtSignal()


# QMainWindow是QWidget的派生类
class CMainWindow(QMainWindow):

  def __init__(self):
    super().__init__()

    # ToolTip设置
    QToolTip.setFont(QFont('华文楷体', 10))

    # statusBar设置
    self.statusBar().showMessage('准备就绪')

    # 退出Action设置
    exitAction = QAction(QIcon('1.png'), '&Exit', self)
    exitAction.setShortcut('ctrl+Q')
    exitAction.setStatusTip('退出应用程序')
    exitAction.triggered.connect(qApp.quit)  # qApp就相当于QCoreApplication.instance()

    # menuBar设置
    menubar = self.menuBar()
    fileMenu = menubar.addMenu('&File')
    fileMenu.addAction(exitAction)

    # toolBar设置
    self.toolbar = self.addToolBar('Exit')
    self.toolbar.addAction(exitAction)

    # 确认PushButton设置
    btnOK = QPushButton("OK")
    btnOK.setToolTip("点击此按钮将确认改变！")
    # btnOK.setStatusTip("点击此按钮将确认改变！")
    btnOK.clicked.connect(self.buttonClicked)
    btnOK.resize(btnOK.sizeHint())

    # 取消PushButton设置
    btnCancel = QPushButton("Cancel")
    btnCancel.setToolTip("点击此按钮将放弃改变！")
    # btnCancel.setStatusTip("点击此按钮将放弃改变！")
    btnCancel.clicked.connect(self.buttonClicked)
    btnCancel.resize(btnCancel.sizeHint())

    # 退出PushButton设置
    btnQuit = QPushButton('退出')
    btnQuit.setToolTip("点击此按钮将退出应用程序！")
    btnQuit.setStatusTip("点击此按钮将退出应用程序！")
    btnQuit.clicked.connect(qApp.quit)
    btnQuit.resize(btnQuit.sizeHint())

    # PushButton布局
    hBox = QHBoxLayout()
    hBox.addStretch(1)
    hBox.addWidget(btnOK)
    hBox.addWidget(btnCancel)
    hBox.addWidget(btnQuit)

    # LCDNumber和Slider设置
    lcd = QLCDNumber(self)
    sld = QSlider(Qt.Horizontal, self)
    sld.valueChanged.connect(lcd.display)

    # 布局
    vBox = QVBoxLayout()
    vBox.addWidget(lcd)
    vBox.addWidget(sld)
    vBox.addLayout(hBox)
    widget = QWidget()
    self.setCentralWidget(widget)  # 建立的widget在窗体的中间位置
    widget.setLayout(vBox)

    self.c = Communicate()
    self.c.closeApp.connect(self.close)

    # Window设置
    self.resize(500, 300)
    self.center()
    self.setFont(QFont('华文楷体', 10))
    self.setWindowTitle('PyQt5应用教程（snmplink编著）')
    self.setWindowIcon(QIcon('10.png'))
    self.show()

  def center(self):
    # 得到主窗体的框架信息
    qr = self.frameGeometry()
    # 得到桌面的中心
    cp = QDesktopWidget().availableGeometry().center()
    # 框架的中心与桌面中心对齐
    qr.moveCenter(cp)
    # 自身窗体的左上角与框架的左上角对齐
    self.move(qr.topLeft())

  def mousePressEvent(self, event):
    self.c.closeApp.emit()

  def buttonClicked(self):
    sender = self.sender()
    self.statusBar().showMessage(sender.text() + '按下')

  def keyPressEvent(self, e):
    if e.key() == Qt.Key_Escape:
      self.close()

  def closeEvent(self, QCloseEvent):
    reply = QMessageBox.question(self,
                                 'PyQt5应用教程（snmplink编著）',
                                 "是否要退出应用程序？",
                                 QMessageBox.Yes | QMessageBox.No,
                                 QMessageBox.No)
    if reply == QMessageBox.Yes:
      QCloseEvent.accept()
    else:
      QCloseEvent.ignore()


if __name__ == '__main__':
  app = QApplication(sys.argv)
  MainWindow = CMainWindow()
  sys.exit(app.exec_())
