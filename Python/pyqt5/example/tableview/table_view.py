# @Time    : 2021/3/1 14:44
# @Author  : lucas
# @File    : table_view.py
# @Project : pyqt
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("QTableWidget例子")
        self.resize(400,300)
        layout=QHBoxLayout()

        #实现的效果是一样的，四行三列，所以要灵活运用函数，这里只是示范一下如何单独设置行列
        TableWidget=QTableWidget(40,3)
        TableWidget.sortItems(2, Qt.DescendingOrder)

        # TableWidget = QTableWidget()
        # TableWidget.setRowCount(4)
        # TableWidget.setColumnCount(3)


        #设置水平方向的表头标签与垂直方向上的表头标签，注意必须在初始化行列之后进行，否则，没有效果
        TableWidget.setHorizontalHeaderLabels(['姓名','性别','体重（kg）'])
        # Todo 优化1 设置垂直方向的表头标签
        # TableWidget.setVerticalHeaderLabels(['行1', '行2', '行3', '行4'])

        # TODO 优化 2 设置水平方向表格为自适应的伸缩模式
        TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #TODO 优化3 将表格变为禁止编辑
        TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # TODO 优化 4 设置表格整行选中
        # TableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # TODO 优化 5 将行与列的高度设置为所显示的内容的宽度高度匹配
        # QTableWidget.resizeColumnsToContents(TableWidget)
        # QTableWidget.resizeRowsToContents(TableWidget)

        # TODO 优化 6 表格头的显示与隐藏resetVerticalScrollMode
        # TableWidget.verticalHeader().setVisible(False)
        # TableWidget.horizontalHeader().setVisible(False)

        # TOdo 优化7 在单元格内放置控件
        # comBox=QComboBox()
        # comBox.addItems(['男','女'])
        # comBox.addItem('未知')
        # comBox.setStyleSheet('QComboBox{margin:3px}')
        # TableWidget.setCellWidget(0,1,comBox)

        # searchBtn=QPushButton('修改')
        # searchBtn.setDown(True)
        # searchBtn.setStyleSheet('QPushButton{margin:3px}')
        # TableWidget.setCellWidget(0,2,searchBtn)


        # #添加数据
        # newItem=QTableWidgetItem('张三')
        # newItem.setForeground(QBrush(QColor(255, 0, 0)))
        # TableWidget.setItem(0,0,newItem)
        #
        # newItem=QTableWidgetItem('男')
        # # 设置对齐方式
        # newItem.setTextAlignment(Qt.AlignCenter)
        # # 设置字体类型，大小号，颜色
        # newItem.setFont(QFont('Times', 12, QFont.Black))
        # TableWidget.setItem(0,1,newItem)
        newItem=QTableWidgetItem('160')
        TableWidget.setItem(0,2,newItem)
        for i in range(50):
            newItem = QTableWidgetItem('张三')
            newItem.setForeground(QBrush(QColor(255, 0, 0)))
            TableWidget.setItem(i, 0, newItem)
            newItem = QTableWidgetItem('男')
            # 设置对齐方式
            newItem.setTextAlignment(Qt.AlignCenter)
            # 设置字体类型，大小号，颜色
            newItem.setFont(QFont('Times', 12, QFont.Black))
            TableWidget.setItem(i, 1, newItem)

            newItem = QTableWidgetItem(f'{160+i}')
            TableWidget.setItem(i, 2, newItem)

        # 按照体重排序
        # Qt.DescendingOrder降序
        # Qt.AscEndingOrder升序
        TableWidget.sortItems(2,Qt.DescendingOrder)

        # 合并单元格
        # TableWidget.setSpan(2,0,4,1)

        # 设置单元格的大小
        # 将第一列的单元宽度设置为150
        # tableWidget.setColumnWidth(0,150)
        # 将第一行的单元格高度的设置为120
        # tableWidget.setRowHeight(0,120)
        # 表格中不显示分割线
        # tableWidget.setShowGrid(False)
        # 允许右键产生菜单
        TableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        # 将右键菜单绑定到槽函数generateMenu
        def generateMenu(pos):
            # 计算有多少条数据，默认-1,
            # row_num = -1
            # for i in TableWidget.selectionModel().selection().indexes():
            #     row_num = i.row()
            row_num = TableWidget.currentRow()
            # 表格中只有两条有效数据，所以只在前两行支持右键弹出菜单
            if row_num:
                menu = QMenu()
                item1 = menu.addAction(u'选项一')
                item2 = menu.addAction(u'选项二')
                item3 = menu.addAction(u'选项三')
                action = menu.exec_(TableWidget.mapToGlobal(pos))
                # 显示选中行的数据文本
                if action == item1:
                    print('你选了选项一，当前行文字内容是：', TableWidget.item(row_num, 0).text(),
                          TableWidget.item(row_num, 1).text(),
                          TableWidget.item(row_num, 2).text())
                if action == item2:
                    print('你选了选项二，当前行文字内容是：', TableWidget.item(row_num, 0).text(),
                          TableWidget.item(row_num, 1).text(),
                          TableWidget.item(row_num, 2).text())
                if action == item3:
                    print('你选了选项三，当前行文字内容是：', TableWidget.item(row_num, 0).text(),
                          TableWidget.item(row_num, 1).text(),
                          TableWidget.item(row_num, 2).text())

        TableWidget.customContextMenuRequested.connect(generateMenu)

        layout.addWidget(TableWidget)
        self.setLayout(layout)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Table()
    win.show()
    sys.exit(app.exec_())
