# @Time    : 2021/3/4 13:56
# @Author  : lucas
# @File    : test.py
# @Project : pyqt
# @Software: PyCharm
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget, QLabel, QGridLayout
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
import webbrowser, sys


class Ui_MainWindow(QWidget):
    item_name = "PyQt打开外部链接"

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tips_1 = QLabel("网站：www.1024shen.com");
        self.tips_1.setOpenExternalLinks(True)

        self.btn_webbrowser = QPushButton('webbrowser效果', self)
        self.btn_test = QPushButton('test效果', self)
        browser = QWebEngineView()
        self.label = QLabel()
        self.hyperlink()
        browser.load(QUrl("https://blog.csdn.net/s_daqing"))
        self.btn_webbrowser.clicked.connect(self.btn_webbrowser_Clicked)
        self.btn_test.clicked.connect(self.test)
        # self.label.clicked.connect(self.hyperlink)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.btn_webbrowser, 1, 0)
        grid.addWidget(self.btn_test, 2, 0)
        grid.addWidget(self.tips_1, 3, 0)
        grid.addWidget(self.label, 4, 0)
        grid.addWidget(browser, 5, 0)

        self.setLayout(grid)

        self.resize(250, 150)
        # self.setMinimumSize(266, 304)
        # self.setMaximumSize(266, 304)
        # self.center()
        self.setWindowTitle(self.item_name)
        self.show()

    def btn_webbrowser_Clicked(self):
        url = 'https://www.1024shen.com/'
        webbrowser.open(url, new=0, autoraise=True)
        # webbrowser.open_new(url)
        # webbrowser.open_new_tab(url)

    def test(self):
        QDesktopServices.openUrl(QUrl("https://www.1024shen.com/"))

    def hyperlink(self):
        self.label.setText('超链接标签<a href="https://blog.csdn.net/s_daqing">点击打开查看</a>')
        self.label.setGeometry(20, 30, 100, 25)
        self.label.setOpenExternalLinks(True)  # 使其成为超链接
        self.label.setTextInteractionFlags(Qt.TextBrowserInteraction)  # 双击可选中文本

    # def center(self):
    #     qr = self.frameGeometry()
    #     cp = QDesktopWidget().availableGeometry().center()
    #     qr.moveCenter(cp)
    #     self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = Ui_MainWindow()
    sys.exit(app.exec_())