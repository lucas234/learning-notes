import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QPushButton, QAction, QFormLayout, \
    QHBoxLayout, QRadioButton, QLabel, QLineEdit, QTableView
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

class TableModel(QtCore.QAbstractTableModel):

    HORIZONTAL_HEAD_DATA = ('Name', 'Age', 'work', 'Sex', 'company')
    VERTICAL_HEAD_DATA = (11, 22, 33, 44, 55)

    def __init__(self, data, header=HORIZONTAL_HEAD_DATA):
        super(TableModel, self).__init__()
        self._data = data
        self.header = header

    def data(self, index=QtCore.QModelIndex(), role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            if self._data:
                return self._data[index.row()][index.column()]
        # # 设置前景色
        # if role == QtCore.Qt.ForegroundRole:
        #     return QtGui.QColor("#4d7d57")

        # # 设置背景色
        # if role == QtCore.Qt.BackgroundColorRole:
        #     return QtGui.QColor(0, 255, 0)

        # 对齐方式
        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignCenter

        # # 设置字体
        # if role == QtCore.Qt.FontRole:
        #     font = QtGui.QFont()
        #     font.setPixelSize(12)
        #     font.setFamily("verdana")
        #     return QtCore.QVariant(font)

        # if role == QtCore.Qt.DecorationRole:
        #     return QtGui.QPixmap("C:\\1.jpg")

    def rowCount(self, parent=QtCore.QModelIndex()):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, parent=QtCore.QModelIndex()):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        if self._data:
            return len(self._data[0])
        else:
            return 0

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.header[section])
            if orientation == Qt.Vertical:
                # len(VERTICAL_HEAD_DATA) 一定要>=rowCount
                return str(self.VERTICAL_HEAD_DATA[section])
        # if role != QtCore.Qt.DisplayRole:
        #     return QtCore.QVariant()
        # if orientation == QtCore.Qt.Horizontal:
        #     return QtCore.QVariant(self.HEAD_DATA[section])
        # return QtCore.QVariant(int(section + 1))

    def flags(self, index=QtCore.QModelIndex()):
        """
        :param index:
        :return:
        """
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

    def setData(self, index=QtCore.QModelIndex(), value=None, role=QtCore.Qt.EditRole):
        """
        :param QModelIndex:
        :param value:
        :param role:
        :return:
        """
        if value != None:
            self.table_data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True


    def insertRow(self, row, value=None, index=QtCore.QModelIndex()):
        """
        :param row:
        :param value: [v1, v2, v3, v4]
        :param idnex:
        :return:
        """
        if value != None:
            self.beginInsertRows(index, row, row)
            self.table_data.insert(row, value)
            self.endInsertRows()

    def removeRow(self, row, index=QtCore.QModelIndex()):
        """
        :param row:
        :param value: [v1, v2, v3, v4]
        :param idnex:
        :return:
        """
        self.beginRemoveRows(index, row, row)
        self.table_data.pop(row)
        self.endRemoveRows()

    def clear(self):
        """
        :return:
        """
        for i in reversed(range(self.rowCount())):
            self.removeRow(i)

    def sort(self, column, order=Qt.AscendingOrder):
        """Sort table by given column number.
        """
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.arraydata = sorted(self.arraydata, key=operator.itemgetter(column))
        if order == Qt.DescendingOrder:
            self.arraydata.reverse()
        self.emit(SIGNAL("layoutChanged()"))


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Test'
        self.left = 100
        self.top = 100
        self.width = 340
        self.height = 280
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.layout = QVBoxLayout(self)
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setStyleSheet(#"QTabWidget::tab-bar{alignment:center;}"
                                     "QTabWidget::pane {border: 1px solid black;background: white;}"
                                     "QTabBar::tab:selected {background-color: blue;margin-top: 2px;}"
                                     # "QTabBar::tab:!selected {background-color: blue;}"
                                     "QTabBar::tab{height:30px; width:108px; color:red;font: 11pt}"
                                 )
        self.page1 = QWidget()
        self.page2 = QTableView()
        self.tabWidget.addTab(self.page1, "Page 1")
        self.tabWidget.addTab(self.page2, "Page 2")
        # self.tabWidget.setTabPosition(QTabWidget.North)
        # self.button1 = QPushButton("Button 1", self)
        # self.button1.clicked.connect(lambda: self.tabWidget.setCurrentIndex(0))
        # self.button2 = QPushButton("Button 2", self)
        self.page1UI()
        self.page2UI()
        # self.button2.clicked.connect(self.button2_clicked)
        self.layout.addWidget(self.tabWidget)
        # self.layout.addWidget(self.button1)
        # self.layout.addWidget(self.button2)
        self.setLayout(self.layout)
        self.show()

    def page1UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("男"))
        sex.addWidget(QRadioButton("女"))
        layout.addRow(QLabel("性别"), sex)
        layout.addRow("生日", QLineEdit())
        # self.setTabText(1, "个人详细信息")
        self.page1.setLayout(layout)

    def page2UI(self):
        self.data = [
            [4, 9, 2],
            [1, 0, 0],
            [3, 5, 0],
            [3, 3, 2],
            [7, 8, 9],
        ]
        self.model = TableModel(self.data, ('Name1', 'Age2', 'work', 'Sex', 'company'))
        self.page2.setModel(self.model)

    # def button2_clicked(self):
    #     self.tabWidget.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())



# from PyQt5 import QtGui
# from PyQt5.QtWidgets import QApplication, QDialog,QTabWidget, QComboBox, QCheckBox ,QGroupBox ,QVBoxLayout, QWidget, QLabel, QLineEdit, QDialogButtonBox
# import sys
# from PyQt5.QtGui import QIcon
#
#
#
# class DownloadListTab(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PyQt5 TabWidget Example")
#         self.setWindowIcon(QIcon("icon.png"))
#         #self.setStyleSheet('background-color:grey')
#         vbox = QVBoxLayout()
#         tabWidget = QTabWidget()
#         # buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
#         # buttonbox.accepted.connect(self.accept)
#         # buttonbox.rejected.connect(self.reject)
#         tabWidget.setFont(QtGui.QFont("Sanserif", 12))
#         tabWidget.addTab(TabContact(), "Contact Details")
#         tabWidget.addTab(TabPeronsalDetails(), "Personal Details")
#         vbox.addWidget(tabWidget)
#         # vbox.addWidget(buttonbox)
#         self.setLayout(vbox)
#
#
# class TabContact(QWidget):
#     def __init__(self):
#         super().__init__()
#         nameLabel = QLabel("Name: ")
#         nameEdit = QLineEdit()
#         phone = QLabel("Phone:")
#         phoneedit = QLineEdit()
#         addr = QLabel("Address:")
#         addredit = QLineEdit()
#         email = QLabel("Email:")
#         emailedit = QLineEdit()
#         vbox = QVBoxLayout()
#         vbox.addWidget(nameLabel)
#         vbox.addWidget(nameEdit)
#         vbox.addWidget(phone)
#         vbox.addWidget(phoneedit)
#         vbox.addWidget(addr)
#         vbox.addWidget(addredit)
#         vbox.addWidget(email)
#         vbox.addWidget(emailedit)
#         self.setLayout(vbox)
#
#
# class TabPeronsalDetails(QWidget):
#     def __init__(self):
#         super().__init__()
#         groupBox = QGroupBox("Select Your Gender")
#         list = ["Male", "Female"]
#         combo = QComboBox()
#         combo.addItems(list)
#         vbox = QVBoxLayout()
#         vbox.addWidget(combo)
#         groupBox.setLayout(vbox)
#         groupBox2 = QGroupBox("Select Your Favorite Programming Language")
#         python =QCheckBox("Python")
#         cpp = QCheckBox("C++")
#         java = QCheckBox("Java")
#         csharp = QCheckBox("C#")
#         vboxp = QVBoxLayout()
#         vboxp.addWidget(python)
#         vboxp.addWidget(cpp)
#         vboxp.addWidget(java)
#         vboxp.addWidget(csharp)
#         groupBox2.setLayout(vboxp)
#         mainLayout = QVBoxLayout()
#         mainLayout.addWidget(groupBox)
#         mainLayout.addWidget(groupBox2)
#         self.setLayout(mainLayout)
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     tabdialog = DownloadListTab()
#     tabdialog.show()
#     app.exec()