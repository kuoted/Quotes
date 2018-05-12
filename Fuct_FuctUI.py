# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from collections import OrderedDict
import csv
from Fuct_Global import *
"""

"""


class BasicMonitor(QtGui.QTableWidget):
    """
    基础表格属性
    """
    # signal = QtCore.pyqtSignal(type(Event()))

    # ----------------------------------------------------------------------
    def __init__(self, parent=None):
        """Constructor"""
        super(BasicMonitor, self).__init__(parent)

        # 保存表头标签用
        self.headerList = OrderedDict()  # 表格头
        self.dataList = []  # 表格数据

        # 初始化右键菜单
        self.initMenu()


    # ----------------------------------------------------------------------
    def initTable(self):
        """初始化表格"""
        # 设置表格的列数
        col = len(self.headerList)
        self.setColumnCount(col)
        # 设置列表头
        self.setHorizontalHeaderLabels(self.headerList)
        # 关闭左边的垂直表头
        self.verticalHeader().setVisible(False)
        # 设为不可编辑
        self.setEditTriggers(self.NoEditTriggers)
        # 设为行交替颜色
        self.setAlternatingRowColors(True)

    # ----------------------------------------------------------------------
    def updateEvent(self, event):
        """收到事件更新"""
        data = event.dict_['data']
        self.updateData(data)

    # ----------------------------------------------------------------------
    def updateData(self, Data_List):
        """将数据更新到表格中"""
        # 如果允许了排序功能，则插入数据前必须关闭，否则插入新的数据会变乱
        self.clearContents()
        for i in range(len(Data_List)):
            for j in range(len(Data_List[i])):
                Data = self.Data_List[i]
                Info = Data[j]
                if j in [4,5,10,11]:
                    Info = unicode(Info)+u"%"
                newItem = QTableWidgetItem(unicode(Info))
                # 添加提示气泡
                newItem.setToolTip(unicode(Info))
                if j == 4 and Data[4] > 0:
                    newItem.setTextColor(QColor(255, 0, 0))
                elif j == 4 and Data[4] < 0:
                    newItem.setTextColor(QColor(0, 255, 0))
                if j == 11 and Data[11] >= 30 and 11 > Data[4] > 9.9:
                    newItem.setTextColor(QColor(255, 0, 0))
                elif j == 11 and Data[11] < 30:
                    newItem.setTextColor(QColor(0, 255, 0))
                self.MyTable.setItem(i, j, newItem)

    def initMenu(self):
        """初始化右键菜单"""
        self.menu = QtGui.QMenu(self)

        detailAction = QtGui.QAction(u'详情', self)
        detailAction.triggered.connect(self.detail)

        copyAction = QtGui.QAction(u'复制代码', self)
        copyAction.triggered.connect(self.copy)

        copyAllAction = QtGui.QAction(u'复制全部', self)
        copyAllAction.triggered.connect(self.copyAll)

        saveAction = QtGui.QAction(u'保存内容', self)
        saveAction.triggered.connect(self.saveToCsv)

        self.menu.addAction(detailAction)
        self.menu.addAction(copyAction)
        self.menu.addAction(copyAllAction)
        self.menu.addAction(saveAction)

    def detail(self):
        """详情展示"""
        self.show_message(u"功能添加中")

    def copy(self):
        """详情展示"""
        self.show_message(u"功能添加中")

    def copyAll(self):
        """详情展示"""
        # 复制到剪切板
        data = [i[1] for i in self.Data_List]
        clipboard = QtGui.QApplication.clipboard()
        clipboard.setText(",".join(data))
        self.show_message(u"复制成功")

    def show_message(self, log):
        """消息提示框"""
        QtGui.QMessageBox.information(self, u"提示", log)

    def saveToCsv(self):
        """保存表格内容到CSV文件"""
        # 先隐藏右键菜单
        self.menu.close()

        # 获取想要保存的文件名
        path = QtGui.QFileDialog.getSaveFileName(self, u'保存数据', '', 'CSV(*.csv)')

        try:
            if not path.isEmpty():
                with open(unicode(path), 'wb') as f:
                    writer = csv.writer(f)
                    # 保存标签
                    headers = [header.encode('gbk') for header in self.headerList]
                    writer.writerow(headers)
                    # 保存每行内容
                    for row in range(self.MyTable.rowCount()):
                        rowdata = []
                        for column in range(self.MyTable.columnCount()):
                            item = self.MyTable.item(row, column)
                            if item is not None:
                                rowdata.append(
                                    unicode(item.text()).encode('gbk'))
                            else:
                                rowdata.append('')
                        writer.writerow(rowdata)
        except IOError:
            pass

    def contextMenuEvent(self, event):
        """右键点击事件"""
        self.menu.popup(QtGui.QCursor.pos())

    def resultSort(self, index):
        # 重写排序
        self.Data_List.sort(key=lambda x:x[index])
        self.addReportData(self.Data_List)



if __name__ == '__main__':
    pass