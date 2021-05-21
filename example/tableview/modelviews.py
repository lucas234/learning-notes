# @Time    : 2021/3/11 9:02
# @Author  : lucas
# @File    : modelviews.py
# @Project : pyqt
# @Software: PyCharm
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel
import signal
import operator

from PyQt5.QtWidgets import QHeaderView


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


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.table = QtWidgets.QTableView()
        self.table1 = QtWidgets.QTableWidget(0,5)
        self.table1.setHorizontalHeaderLabels(('Name1', 'Age2', 'work', 'Sex', 'company'))
        # self.table.verticalHeader().setVisible(False)
        # self.table.horizontalHeader().setStyleSheet(header_style)
        # self.table1.horizontalHeader().setStyleSheet(header_style)
        # self.table.setStyleSheet(table_data_style)
        self.data = [
          [4, 9, 2],
          [1, 0, 0],
          [3, 5, 0],
          [3, 3, 2],
          [7, 8, 9],
        ]
        self.result_layout = QtWidgets.QVBoxLayout()
        self.btn = QtWidgets.QPushButton("button")
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.result_layout)
        self.result_layout.addWidget(self.btn)
        self.result_layout.addWidget(self.table1)
        self.btn.clicked.connect(self.btn_click)
        # self.setCentralWidget(self.result_layout)
    def btn_click(self):
        self.result_layout.addWidget(self.table)
        self.result_layout.removeWidget(self.table1)
        self.model = TableModel(self.data, ('Name1', 'Age2', 'work', 'Sex', 'company'))
        self.table.setModel(self.model)
        # self.table.setColumnWidth(0, 160)

if __name__ == "__main__" :
    app=QtWidgets.QApplication(sys.argv)
    window=MainWindow()
    window.show()
    app.exec_()