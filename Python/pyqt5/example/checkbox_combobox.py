# @Time    : 2021/5/21 13:09
# @Author  : lucas
# @File    : checkbox_combobox.py
# @Project : pyqt
# @Software: PyCharm

import sys
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QStandardItem, QFontMetrics, QPalette
from PyQt5.QtWidgets import qApp, QStyledItemDelegate, QComboBox, \
    QApplication, QWidget, QHBoxLayout, QPushButton, QMainWindow


class CheckableComboBox(QComboBox):
    # Subclass Delegate to increase item height
    class Delegate(QStyledItemDelegate):
        def sizeHint(self, option, index):
            size = super().sizeHint(option, index)
            size.setHeight(20)
            return size

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Make the combo editable to set a custom text, but readonly
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        # Make the lineedit the same color as QPushButton
        palette = qApp.palette()
        palette.setBrush(QPalette.Base, palette.button())
        self.lineEdit().setPalette(palette)

        # Use custom delegate
        self.setItemDelegate(CheckableComboBox.Delegate())

        # Update the text when an item is toggled
        self.model().dataChanged.connect(self.updateText)

        # Hide and show popup when clicking the line edit
        self.lineEdit().installEventFilter(self)
        self.closeOnLineEditClick = False

        # Prevent popup from closing when clicking on an item
        self.view().viewport().installEventFilter(self)

    def resizeEvent(self, event):
        # Recompute text to elide as needed
        self.updateText()
        super().resizeEvent(event)

    def eventFilter(self, object, event):

        if object == self.lineEdit():
            if event.type() == QEvent.MouseButtonRelease:
                if self.closeOnLineEditClick:
                    self.hidePopup()
                else:
                    self.showPopup()
                return True
            return False

        if object == self.view().viewport():
            if event.type() == QEvent.MouseButtonRelease:
                index = self.view().indexAt(event.pos())
                item = self.model().item(index.row())

                if item.checkState() == Qt.Checked:
                    item.setCheckState(Qt.Unchecked)
                else:
                    item.setCheckState(Qt.Checked)
                return True
        return False

    def showPopup(self):
        super().showPopup()
        # When the popup is displayed, a click on the lineedit should close it
        self.closeOnLineEditClick = True

    def hidePopup(self):
        super().hidePopup()
        # Used to prevent immediate reopening when clicking on the lineEdit
        self.startTimer(100)
        # Refresh the display text when closing
        self.updateText()

    def timerEvent(self, event):
        # After timeout, kill timer, and reenable click on line edit
        self.killTimer(event.timerId())
        self.closeOnLineEditClick = False

    def updateText(self):
        texts = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.Checked:
                texts.append(self.model().item(i).text())
        text = ", ".join(texts)

        # Compute elided text (with "...")
        metrics = QFontMetrics(self.lineEdit().font())
        elidedText = metrics.elidedText(text, Qt.ElideRight, self.lineEdit().width())
        self.lineEdit().setText(elidedText)

    def addItem(self, text, data=None):
        item = QStandardItem()
        item.setText(text)
        if data is None:
            item.setData(text)
        else:
            item.setData(data)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        item.setData(Qt.Unchecked, Qt.CheckStateRole)
        self.model().appendRow(item)

    def addItems(self, texts, datalist=None):
        for i, text in enumerate(texts):
            try:
                data = datalist[i]
            except (TypeError, IndexError):
                data = None
            self.addItem(text, data)

    def currentData(self):
        # Return the list of selected items data
        res = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.Checked:
                res.append(self.model().item(i).data())
        return res


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 300)
        layout = QHBoxLayout()
        comunes = ['Ameglia', 'Arcola', 'Bagnone', 'Bolano', 'Carrara', 'Casola', 'Castelnuovo Magra',
                   'Comano, località Crespiano', 'Fivizzano', 'Fivizzano località Pieve S. Paolo',
                   'Fivizzano località Pieve di Viano', 'Fivizzano località Soliera', 'Fosdinovo', 'Genova',
                   'La Spezia', 'Levanto', 'Licciana Nardi', 'Lucca', 'Lusuolo', 'Massa', 'Minucciano',
                   'Montignoso', 'Ortonovo', 'Piazza al sercho', 'Pietrasanta', 'Pignine', 'Pisa',
                   'Podenzana', 'Pontremoli', 'Portovenere', 'Santo Stefano di Magra', 'Sarzana',
                   'Serravezza', 'Sesta Godano', 'Varese Ligure', 'Vezzano Ligure', 'Zignago']
        combo = CheckableComboBox()
        combo.addItems(comunes)
        layout.addWidget(combo)
        btn = QPushButton()
        btn.setFixedSize(20,20)
        style = """QPushButton{
                                border-image:url(../assets/start.svg);
                                background-color: none;
                                border:none;
                                padding:1px 1px;
                            }
                            QPushButton:hover{
                                border-image:url(../assets/blue_start.svg);
                                border: 1px solid;
                                border-color:gray;
                                border-radius:4px
                            }
                                    """
        btn.setStyleSheet(style)
        layout.addWidget(btn)
        widget = QWidget(self)
        self.setCentralWidget(widget)
        widget.setLayout(layout)


a = QApplication(sys.argv)
w = Window()
w.show()
sys.exit(a.exec_())