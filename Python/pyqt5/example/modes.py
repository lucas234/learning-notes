# @Time    : 2021/4/14 9:28
# @Author  : lucas
# @File    : dark_style.py
# @Project : pyqt
# @Software: PyCharm
from PyQt5.QtGui import QPalette, QColor

# dark mode
WHITE = QColor(255, 255, 255)
BLACK = QColor(0, 0, 0)
RED = QColor(255, 0, 0)
PRIMARY = QColor(53, 53, 53)
SECONDARY = QColor(35, 35, 35)
TERTIARY = QColor(42, 130, 218)

# light mode
LIGHT_BLACK = QColor(0, 0, 0)
LIGHT_WHITE = QColor(255, 255, 255)
LIGHT_RED = QColor(255, 0, 0)
LIGHT_PRIMARY = QColor(245, 245, 245)
LIGHT_SECONDARY = QColor(255, 252, 255)
LIGHT_TERTIARY = QColor(42, 130, 218)


def css_rgb(color, a=False):
    """Get a CSS `rgb` or `rgba` string from a `QtGui.QColor`."""
    return ("rgba({}, {}, {}, {})" if a else "rgb({}, {}, {})").format(*color.getRgb())


class QLightPalette(QPalette):
    """Dark palette for a Qt application meant to be used with the Fusion theme."""
    def __init__(self, *__args):
        super().__init__(*__args)

        # Set all the colors based on the constants in globals
        self.setColor(QPalette.Window, LIGHT_PRIMARY)
        self.setColor(QPalette.WindowText, LIGHT_BLACK)
        self.setColor(QPalette.Base, LIGHT_SECONDARY)
        self.setColor(QPalette.AlternateBase, LIGHT_PRIMARY)
        self.setColor(QPalette.ToolTipBase, LIGHT_BLACK)
        self.setColor(QPalette.ToolTipText, LIGHT_BLACK)
        self.setColor(QPalette.Text, LIGHT_BLACK)
        self.setColor(QPalette.Button, LIGHT_PRIMARY)
        self.setColor(QPalette.ButtonText, LIGHT_BLACK)
        self.setColor(QPalette.BrightText, LIGHT_RED)
        self.setColor(QPalette.Link, LIGHT_TERTIARY)
        self.setColor(QPalette.Highlight, LIGHT_TERTIARY)
        self.setColor(QPalette.HighlightedText, LIGHT_BLACK)

    @staticmethod
    def set_stylesheet(app):
        """Static method to set the tooltip stylesheet to a `QtWidgets.QApplication`."""
        app.setStyleSheet("QToolTip {{"
                          "color: {white};"
                          "background-color: {tertiary};"
                          "border: 1px solid {white};"
                          "}}".format(white=css_rgb(LIGHT_BLACK), tertiary=css_rgb(LIGHT_TERTIARY)))

    def set_app(self, app):
        """Set the Fusion theme and this palette to a `QtWidgets.QApplication`."""
        app.setStyle("Fusion")
        app.setPalette(self)
        self.set_stylesheet(app)


class QDarkPalette(QPalette):
    def __init__(self, *__args):
        super().__init__(*__args)

        # Set all the colors based on the constants in globals
        self.setColor(QPalette.Window, PRIMARY)
        self.setColor(QPalette.WindowText, WHITE)
        self.setColor(QPalette.Base, SECONDARY)
        self.setColor(QPalette.AlternateBase, PRIMARY)
        self.setColor(QPalette.ToolTipBase, WHITE)
        self.setColor(QPalette.ToolTipText, WHITE)
        self.setColor(QPalette.Text, WHITE)
        self.setColor(QPalette.Button, PRIMARY)
        self.setColor(QPalette.ButtonText, WHITE)
        self.setColor(QPalette.BrightText, RED)
        self.setColor(QPalette.Link, TERTIARY)
        self.setColor(QPalette.Highlight, TERTIARY)
        self.setColor(QPalette.HighlightedText, BLACK)

    @staticmethod
    def set_stylesheet(app):
        """Static method to set the tooltip stylesheet to a `QtWidgets.QApplication`."""
        app.setStyleSheet("QToolTip {{"
                          "color: {white};"
                          "background-color: {tertiary};"
                          "border: 1px solid {white};"
                          "}}".format(white=css_rgb(WHITE), tertiary=css_rgb(TERTIARY)))

    def set_app(self, app):
        """Set the Fusion theme and this palette to a `QtWidgets.QApplication`."""
        app.setStyle("Fusion")
        app.setPalette(self)
        self.set_stylesheet(app)



from PyQt5.QtWidgets import QApplication, QVBoxLayout, \
    QPushButton, QMainWindow, QWidget
import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        btn = QPushButton("测试")
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(btn)
        w = QWidget()
        self.setCentralWidget(w)
        w.setLayout(self.vbox)
        self.setWindowTitle("暗黑模式")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    # 用法
    QDarkPalette().set_app(app)
    win.show()
    sys.exit(app.exec_())