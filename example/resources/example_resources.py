from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QPushButton
import sys
import resources


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        btn = QPushButton("测试")
        btn.setIcon(QIcon(":about.png"))
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.vbox.addWidget(btn)
        self.vbox.addStretch()
        self.setWindowTitle("Styles")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
