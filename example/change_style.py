# @Time    : 2021/4/14 10:25
# @Author  : lucas
# @File    : change_style.py
# @Project : pyqt
# @Software: PyCharm
from PyQt5.QtWidgets import (QDialog, QApplication,
                             QStyleFactory, QComboBox,
                             QLabel, QVBoxLayout)


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        styleComboBox = QComboBox()
        # 获取本机支持的主题，并添加到QComboBox中
        styleComboBox.addItems(QStyleFactory.keys())

        styleLabel = QLabel("Style:")

        # 绑定槽函数，
        styleComboBox.activated[str].connect(self.changeStyle)

        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.vbox.addWidget(styleLabel)
        self.vbox.addWidget(styleComboBox)
        self.vbox.addStretch()

        self.setWindowTitle("Styles")  # 设置标题
        self.changeStyle('Fusion')  # 启动时使用Fusion风格

    # 槽函数
    def changeStyle(self, styleName):
        # 改变Style
        QApplication.setStyle(QStyleFactory.create(styleName))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
