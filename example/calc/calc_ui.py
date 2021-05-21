# @Time    : 2021/4/9 11:11
# @Author  : lucas
# @File    : calc_ui.py
# @Project : pyqt
# @Software: PyCharm
from PyQt5.QtCore import QRegExp, Qt, QFile, QTextStream
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QStyleFactory
from PyQt5 import uic
import sys
from functools import partial


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        # this will hide the title bar
        # self.setWindowFlag(Qt.FramelessWindowHint)
        # this is used for loading ui file
        uic.loadUi("calc.ui", self)
        # find our widgets
        self.display_result = ""
        self.buttons = self.findChildren(QPushButton, QRegExp('pushButton_.?'))
        self.display = self.findChild(QLineEdit, "result")
        self._connect_signals()

    def _connect_signals(self):
        """Connect signals and slots."""
        for btn in self.buttons:
            btn_text = btn.text()
            if btn_text == '=':
                btn.clicked.connect(self.calculate_result)
            elif btn_text == 'C':
                btn.clicked.connect(self.clear_display)
            else:
                btn.clicked.connect(partial(self.clicked, btn))

    def calculate_result(self):
        display = self.display.text().replace("×", "*").replace("÷", "/").replace("%", "/100")
        self.display_result = self.evaluate_expression(display)
        self.display.setText(self.display_result)

    def clear_display(self):
        self.display.setText("")
        self.display_result = ""

    def evaluate_expression(self, expression):
        try:
            result = str(eval(expression, {}, {}))
        except Exception:
            result = "ERROR"
        return result

    def clicked(self, button):
        if self.display.text() == "ERROR":
            self.clear_display()
        self.display_result += button.text()
        self.display.setText(self.display_result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyle('Fusion')
    # ['windowsvista', 'Windows', 'Fusion']

    # dark mode
    # from modes import QDarkPalette
    # QDarkPalette().set_app(app)

    window = UI()
    window.show()
    sys.exit(app.exec_())
