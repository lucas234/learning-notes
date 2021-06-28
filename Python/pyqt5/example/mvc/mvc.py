# @Time    : 2021/3/17 15:43
# @Author  : lucas
# @File    : mvc.py
# @Project : pyqt
# @Software: PyCharm
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMenu


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(433, 322)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 218))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableView = QtWidgets.QTableView(self.layoutWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.tableView_2 = QtWidgets.QTableView(self.layoutWidget)
        self.tableView_2.setObjectName("tableView_2")
        self.verticalLayout_2.addWidget(self.tableView_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(80, 240, 195, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 433, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        TableWidget = self.tableView
        TableWidget.setContextMenuPolicy(Qt.CustomContextMenu)

        # 将右键菜单绑定到槽函数generateMenu
        def generateMenu(pos):
            print(123)
            # 计算有多少条数据，默认-1,
            # row_num = -1
            # for i in TableWidget.selectionModel().selection().indexes():
            #     row_num = i.row()
            # row_num = TableWidget.currentRow()
            row_num = TableWidget.currentIndex().row()
            # 表格中只有两条有效数据，所以只在前两行支持右键弹出菜单
            if row_num>=0:
                menu = QMenu()
                item1 = menu.addAction(u'选项一')
                item2 = menu.addAction(u'选项二')
                item3 = menu.addAction(u'选项三')
                action = menu.exec_(TableWidget.mapToGlobal(pos))
                # 显示选中行的数据文本
                if action == item1:
                    print(f'你选了选项一，当前{row_num}行文字内容是：', TableWidget.model().table_data[2][2])
                if action == item2:
                    print('你选了选项二，当前行文字内容是：', TableWidget.item(row_num, 0).text(),
                          TableWidget.item(row_num, 1).text(),
                          TableWidget.item(row_num, 2).text())
                if action == item3:
                    print('你选了选项三，当前行文字内容是：', TableWidget.item(row_num, 0).text())

        TableWidget.customContextMenuRequested.connect(generateMenu)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "remove"))


class TableMode(QtCore.QAbstractTableModel):
    """
    创建list model
    """
    HEAD_DATA = ('Name', 'Age', 'work', 'Sex', 'company')

    def __init__(self, parent=None):
        super(TableMode, self).__init__(parent)
        self.table_data = [["A", 'B', 'C', 'D'],
                           ["A1", 'B1', 'C1', 'D1'],
                           ["A2", 'B2', 'C2', 'D2'],
                           ["A3", 'B3', 'C3', 'D3']]

    def columnCount(self, parent=QtCore.QModelIndex()):
        """
        :param parent:
        :return:
        """
        return 4

    def rowCount(self, parent=QtCore.QModelIndex()):
        """
        :param self:
        :param parent:
        :param args:
        :param kwargs:
        :return:
        """
        return len(self.table_data)

    def headerData(self, sec, orientation=QtCore.Qt.Horizontal, role=QtCore.Qt.DisplayRole):
        """
        :param sec:
        :param orientation:
        :param role:
        :return:
        """
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.HEAD_DATA[sec]

        if orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            return sec + 1

    def data(self, index=QtCore.QModelIndex(), role=QtCore.Qt.DisplayRole):
        """
        :param QModelIndex:
        :param role:
        :return:
        """
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            return self.table_data[index.row()][index.column()]

        # 设置前景色
        if role == QtCore.Qt.ForegroundRole:
            return QtGui.QColor(255, 0, 0)

        # 设置背景色
        if role == QtCore.Qt.BackgroundColorRole:
            return QtGui.QColor(0, 255, 0)

        # if role == QtCore.Qt.DecorationRole:
        #     return QtGui.QPixmap("D:/school/TdClass/Prictice/1.jpg")

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

    def insertRow(self, row, value=None, idnex=QtCore.QModelIndex()):
        """
        :param row:
        :param value: [v1, v2, v3, v4]
        :param idnex:
        :return:
        """
        if value != None:
            self.beginInsertRows(idnex, row, row)
            self.table_data.insert(row, value)
            self.endInsertRows()

    def removeRow(self, row, idnex=QtCore.QModelIndex()):
        """
        :param row:
        :param value: [v1, v2, v3, v4]
        :param idnex:
        :return:
        """
        self.beginRemoveRows(idnex, row, row)
        self.table_data.pop(row)
        self.endRemoveRows()

    def clear(self):
        """
        :return:
        """
        for i in reversed(range(self.rowCount())):
            self.removeRow(i)


class DemonWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    """
    创建list model
    """

    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.table_model = TableMode(self.tableView)
        self.tableView.setModel(self.table_model)
        self.tableView_2.setModel(self.table_model)

    @QtCore.pyqtSlot()
    def on_pushButton_clicked(self):
        """
        # 点击按钮添加元素
        :return:
        """
        self.table_model.insertRow(self.table_model.rowCount(), ['S', 'S', 'S', 'S'])

    @QtCore.pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        # 点击按钮删除元素
        :return:
        """
        # self.table_model.clear() #清空整个表格
        # self.table_model.removeRow(self.table_model.rowCount() - 1) #删除最后一行
        # 删除选定行
        row = self.tableView.currentIndex().row()
        print(row)
        self.table_model.removeRow(row)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # sys.argv是一组命令行参数的列表，该程序会被cou进行轮询
    ex = DemonWindow()
    ex.show()
    app.exec_()