from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer, Qt, QSize
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QStyledItemDelegate, QApplication, QStyle, \
    QStyleOptionProgressBar, QHBoxLayout, QPushButton, QWidget, QToolTip, QAbstractItemView

data = [["第一集", 100, 2], ["第2集", 0, 1],
        ["第4集", 20, 1], ["第3集", 0, 1],
        ["山海情", 0, 0]]


class ButtonDelegate(QStyledItemDelegate):

    def __init__(self, parent=None):
        super(ButtonDelegate, self).__init__(parent)

    def paint(self, painter, option, index):
        QToolTip.setFont(QFont('Arial', 11))

        def clicked_start_pause():
            # global image
            row = index.row()
            if index.data()==1:
                data[row][2] = 0
                print("开始任务")
                image = QIcon("pause.svg")
                btn_start_pause.setToolTip("暂停")
            elif index.data()==0:
                print("暂停任务")
                data[row][2] = 1
                image = QIcon("start.svg")
                btn_start_pause.setToolTip("开始")
            else:
                image = QIcon("checkmark.svg")
                btn_start_pause.setToolTip("下载完成")

            btn_start_pause.setIcon(image)
            # print(index.row())
            print(index.data())
            # print(index.model().index(index.row(),0).data())

        if index.data()==1:
            image = QIcon("start.svg")
        elif index.data()==0:
            image = QIcon("pause.svg")
        else:
            image = QIcon("checkmark.svg")

        if not self.parent().indexWidget(index):
            btn_start_pause = QPushButton(self.parent())
            btn_start_pause.setIconSize(QSize(20, 20))
            btn_start_pause.setIcon(image)
            btn_start_pause.index = [index.row(), index.column()]
            btn_start_pause.clicked.connect(clicked_start_pause)
            if index.data() == 1:
                btn_start_pause.setToolTip("开始")
            elif index.data() == 0:
                btn_start_pause.setToolTip("暂停")
            else:
                btn_start_pause.setToolTip("下载完成")
                btn_start_pause.setDisabled(True)

            style = """QPushButton{
                                background-color: none;
                                border:none;
                                padding:1px 1px;
                            }
                            QPushButton:hover{
                                padding:1px 1px;
                                border: 1px solid;
                                border-color:#49b675;
                                border-radius:4px
                            }
                            """
            btn_start_pause.setStyleSheet(style)
            btn_folder = QPushButton(self.parent())
            btn_folder.setIconSize(QSize(20, 20))
            btn_folder.setIcon(QIcon("folder.svg"))
            btn_folder.index = [index.row(), index.column()]
            btn_folder.clicked.connect(clicked_start_pause)
            btn_folder.setToolTip("打开所在文件夹")
            # 显示图片
            # btn_folder.setToolTip('<img src="../assets/close.svg">')
            btn_folder.setStyleSheet(style)
            btn_delete = QPushButton(self.parent())
            btn_delete.setIconSize(QSize(20, 20))
            btn_delete.setIcon(QIcon("close.svg"))
            btn_delete.index = [index.row(), index.column()]
            btn_delete.clicked.connect(clicked_start_pause)
            btn_delete.setToolTip("删除")
            btn_delete.setStyleSheet(style)
            h_box_layout = QHBoxLayout()
            h_box_layout.addWidget(btn_start_pause)
            h_box_layout.addWidget(btn_delete)
            h_box_layout.addWidget(btn_folder)
            h_box_layout.setContentsMargins(0, 0, 0, 0)
            h_box_layout.setAlignment(Qt.AlignCenter)
            widget = QWidget()
            widget.setFixedWidth(150)
            widget.setLayout(h_box_layout)
            self.parent().setIndexWidget(index, widget)


class ProgressBarDelegate(QStyledItemDelegate):
    def __init__(self, parent):
        QStyledItemDelegate.__init__(self, parent=parent)

    def paint(self, painter, option, index):
        # QStyledItemDelegate.paint(self, painter, option, index)
        progress = index.data()
        bar_option = QStyleOptionProgressBar()
        bar_option.rect = option.rect
        # bar_option.rect.setWidth(120)
        bar_option.rect.setHeight(option.rect.height() - 5)
        bar_option.rect.setTop(option.rect.top() + 5)
        bar_option.minimum = 0
        bar_option.maximum = 100
        bar_option.progress = progress
        bar_option.text = f"{progress}%" if progress < 100 else "完成"
        bar_option.textVisible = True
        bar_option.textAlignment = QtCore.Qt.AlignCenter
        QApplication.style().drawControl(QStyle.CE_ProgressBar, bar_option, painter)


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

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QTableView()
    w.setColumnWidth(1, 250)
    w.setColumnWidth(2, 250)
    w.setFixedSize(500, 400)
    delegate = ProgressBarDelegate(w)
    w.setItemDelegateForColumn(1, delegate)
    button_delegate = ButtonDelegate(w)
    w.setItemDelegateForColumn(2, button_delegate)
    model = TableModel(data, ("ID", "Name", "Progress"))
    w.setModel(model)
    w.verticalHeader().setVisible(False)
    w.setShowGrid(False)
    w.setSelectionMode(QAbstractItemView.NoSelection)
    # w.setFrameShape(QFrame.Box)
    w.horizontalHeader().setVisible(False)
    w.show()

    def handle_timer():
        import random
        data[0][1] = random.randint(40, 100)
        data[1][1] = random.randint(50, 100)
        data[2][1] = random.randint(60, 100)
        data[3][1] = random.randint(90, 100)
        data[4][1] = random.randint(1, 100)
        # model = TableModel(data, ("ID", "Name", "Progress"))
        # w.setModel(model)
        # model._data = data
        w.viewport().repaint()
        # w.viewport().update()

    timer = QTimer()
    timer.timeout.connect(handle_timer)
    timer.start(1000)
    sys.exit(app.exec_())


