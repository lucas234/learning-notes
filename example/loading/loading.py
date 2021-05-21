# @Time    : 2021/3/22 13:05
# @Author  : lucas
# @File    : loading.py
# @Project : pyqt
# @Software: PyCharm
from PyQt5.Qt import *
from PyQt5.QtWidgets import QDesktopWidget


class LoadingMask(QMainWindow):
    signal = pyqtSignal()

    def __init__(self, parent, gif=None, tip=None):
        self.gif = gif
        self.tip = tip
        super(LoadingMask, self).__init__(parent)
        # parent.installEventFilter(self)
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        if self.tip:
            self.label.setText(self.tip)
            font = QFont('Microsoft YaHei', 10, QFont.Normal)
            font_metrics = QFontMetrics(font)
            self.label.setFont(font)
            self.label.setFixedSize(font_metrics.width(self.tip, len(self.tip))+10, font_metrics.height()+5)
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setStyleSheet(
                'QLabel{border-radius: 4px; color: red; padding: 5px;}')

        if self.gif:
            self.movie = QMovie(self.gif)
            self.movie.setSpeed(30)
            self.label.setMovie(self.movie)
            self.label.setFixedSize(QSize(100, 100))
            self.label.setScaledContents(True)
            self.movie.start()

        layout = QHBoxLayout()
        widget = QWidget()
        width, height = parent.width(),parent.height()
        widget.setFixedSize(width, height)
        widget.setLayout(layout)
        layout.addWidget(self.label)
        self.setCentralWidget(widget)
        self.setWindowOpacity(0.9)
        # print(widget.palette().color(QPalette.Background).name())
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.ToolTip)
        # self.center()
        self.hide()
        self.move(parent.pos().x() + 1, parent.pos().y() + 30)

    def eventFilter(self, widget, event):
        if widget == self.parent() and type(event) == QMoveEvent:
            self.move_with_parent()
            return True
        return super(LoadingMask, self).eventFilter(widget, event)

    def move_with_parent(self):
        if self.isVisible():
            self.move(self.parent().geometry().x(), self.parent().geometry().y())
            self.setFixedSize(QSize(self.parent().geometry().width(), self.parent().geometry().height()))

    # def center(self):
    #     qr = self.frameGeometry()
    #     cp = QDesktopWidget().availableGeometry().center()
    #     qr.moveCenter(cp)
    #     self.move(qr.topLeft())

    def show_loading(self, window, duration=5000):
        self.show()
        window.installEventFilter(self)
        QTimer().singleShot(duration, lambda :self.deleteLater())

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    widget = QWidget()
    widget.setFixedSize(500, 500)
    loading_gif = LoadingMask(widget, 'loading.gif')
    loading_gif.show_loading(widget)
    # loading_tip = LoadingMask(widget, tip="loading...")
    # loading_tip.show_loading(widget)
    widget.show()
    sys.exit(app.exec_())
