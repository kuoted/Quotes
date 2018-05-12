# -*- coding: utf-8 -*-

"""
主界面逻辑处理
"""

# 系统模块
import sip
import copy
import os
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from functools import partial
import csv

# 自定义模块
import Fuct_QThreadUI
import Fuct_TableHeader
import Fuct_Global
from UI_Main import Ui_MainWindow
import Login_Start
import UI_Global

class MainWindow(QtGui.QMainWindow):
    """主界面"""
    signalStatusBar = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 初始化登录窗口
        self.LoginUI = Login_Start.MainWindow()
        self.LoginUI.show()
        self.connect(self.LoginUI, QtCore.SIGNAL("transfer_login"), self.setLoginStatus)
        # 设置界面样式
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.showMaximized()
        # 设置窗口拉动按钮
        sizeGrip = QSizeGrip(self)
        sizeGrip.setStyleSheet("image: url(:/Imag/Imag/sizegrip.png);")
        self.ui.sizeGrip_layout.addWidget(sizeGrip)
        self.ui.sizeGrip_layout.setAlignment(sizeGrip, Qt.AlignRight)
        # 允许关闭tab
        self.ui.tabWidget.setTabsClosable(True)  # 显示关闭按钮
        self.connect(self.ui.tabWidget, SIGNAL("tabCloseRequested(int)"), self.closeTab)
        # 设置次级菜单
        self.Menu_Setting()
        # 设置主菜单与副菜单映射关系
        self.Menu_Link()
        self.UpdateMenu(self.ui.QToolButton_mRankList.text())
        # 设置按钮点击后保持按下状态
        self.KeepButtonStatus()
        # 初始化表格
        self.initToolBox()
        self.tmp_dataList = []
        # 按下按钮
        self.ui.QToolButton_mRankList.click()
        # tem数据定义
        self.tmp_daylines = ""
        # 启动数据引擎

        # 绑定主菜单证券功能按钮
        self.ui.QToolButton_mRankList.clicked.connect(partial(self.UpdateMenu_clicked, "龙虎榜"))
        self.ui.QToolButton_mLimit.clicked.connect(partial(self.UpdateMenu_clicked, "涨停预测"))
        self.ui.QToolButton_mFuctuation.clicked.connect(partial(self.UpdateMenu_clicked, "涨跌幅追踪"))
        self.ui.QToolButton_mNews.clicked.connect(partial(self.UpdateMenu_clicked, "资讯"))
        self.ui.QToolButton_mSecType.clicked.connect(partial(self.UpdateMenu_clicked, "板块追踪"))

        # 绑定主菜单系统功能按钮
        self.ui.QToolButton_Login.clicked.connect(partial(self.QToolButton_Login_clicked))
        self.ui.QToolButton_Setting.clicked.connect(partial(self.QToolButton_Setting_clicked))

    # 主菜单按钮-------------------------------------------------------------
    def UpdateMenu_clicked(self, event):
        # 刷新菜单
        self.UpdateMenu(event)

    def QToolButton_Login_clicked(self):
        # 登录
        self.LoginUI.show()

    def QToolButton_Setting_clicked(self):
        # 设置
        self.show_message(u"功能添加中：\n"
                          u"1、新股开板\n"
                          u"2、复牌公告\n"
                          u"3、公告\n"
                          u"4、个股新闻\n")

    # 副菜单按钮-------------------------------------------------------------
    def QPushButton_cRankStocks_clicked(self,date):
        # import time
        # time.sleep(10)
        # 龙虎榜_查询近一天
        self.thread = Fuct_QThreadUI.QPushButton_cRankStocks_clicked(date)
        self.connect(self.thread, QtCore.SIGNAL("SIGNAL_QPushButton_cRankStocks"), self.QThread_RankStocks)
        self.thread.start()
        self.MyTable.hide()

    def QPushButton_cRankChice_clicked(self):
        # 龙虎榜_查询自定义时间
        self.slavewindow = UI_Global.dateWindow()
        self.connect(self.slavewindow, QtCore.SIGNAL("RankChice_dateWindow"), self.QPushButton_cRankStocks_clicked)
        self.slavewindow.show()
        self.MyTable.hide()

    def QPushButton_cLimit_clicked(self,date):
        # 涨停预测_查询近一天
        if len(date) < 16:
            self.show_message(u"时间不正确，请检查后重试！")
        else:
            self.thread = Fuct_QThreadUI.QPushButton_cLimit_clicked(date)
            self.connect(self.thread, QtCore.SIGNAL("SIGNAL_QPushButton_cLimit"), self.QPushButton_cLimit)
            self.thread.start()
            self.MyTable.hide()
            self.show_message(u"数据引擎预计耗时2分钟，请耐心等待！")

    def QPushButton_cLimitChice_clicked(self):
        # 涨停预测_查询自定义时间
        self.slavewindow = UI_Global.limitWindow()
        self.connect(self.slavewindow, QtCore.SIGNAL("limit_dateWindow"), self.QPushButton_cLimit_clicked)
        self.slavewindow.show()
        self.MyTable.hide()

    def QPushButton_cFuctuationChice_clicked(self):
        # 涨跌幅_查询自定义时间
        self.slavewindow = UI_Global.fuctuationWindow()
        self.connect(self.slavewindow, QtCore.SIGNAL("fuctuation_dateWindow"), self.QPushButton_cLimit_clicked)
        self.slavewindow.show()
        self.MyTable.hide()

    # 副菜单线程-------------------------------------------------------------
    def QThread_RankStocks(self, tType, dataList):
        # 显示龙虎榜数据
        self.tableType = tType
        self.dataList = dataList
        self.headerList = Fuct_TableHeader.header[tType]
        self.addReportData()

    def QPushButton_cLimit(self, tType, dataList):
        # 显示涨停预测数据
        self.tableType = tType
        self.dataList = dataList
        self.headerList = Fuct_TableHeader.header[tType]
        self.addReportData()

    # 系统函数----------------------------------------------------------------------
    def show_message(self, log):
        """消息提示框"""
        QtGui.QMessageBox.information(self, u"提示", log)

    def Menu_Link(self):
        # 设置主菜单与副菜单映射关系
        self.MenuLink = [
                            {
                                "MainTitle": "龙虎榜",
                                "CMenu":[self.ui.QPushButton_cRankStocks,self.ui.QPushButton_cRankChice,]
                            },

                            {
                                "MainTitle": "涨停预测",
                                "CMenu": [self.ui.QPushButton_cLimit,self.ui.QPushButton_cLimitChice,]
                            },
                            {
                                "MainTitle": "涨跌幅追踪",
                                "CMenu": [self.ui.QPushButton_cFuctuation]
                            },
                        ]

    def Menu_Setting(self):
        # 设置菜单
        buttonList = []
        widget = QWidget()

        # 创建副菜单按钮
        # 龙虎榜
        self.ui.QPushButton_cRankStocks = QPushButton(u"龙近一天_龙虎榜", widget)
        self.ui.QPushButton_cRankChice = QPushButton(u"历史数据_龙虎榜", widget)
        # 涨停预测
        self.ui.QPushButton_cLimit = QPushButton(u"近一天_预测", widget)
        self.ui.QPushButton_cLimitChice = QPushButton(u"自定义查询_预测", widget)
        # 涨跌幅追踪
        self.ui.QPushButton_cFuctuation = QPushButton(u"自定义查询_涨跌幅", widget)
        # 添加到按钮列表
        buttonList.append(self.ui.QPushButton_cRankStocks)
        buttonList.append(self.ui.QPushButton_cRankChice)
        buttonList.append(self.ui.QPushButton_cLimit)
        buttonList.append(self.ui.QPushButton_cLimitChice)
        buttonList.append(self.ui.QPushButton_cFuctuation)

        # 绑定副菜单按钮
        self.ui.QPushButton_cRankStocks.clicked.connect(partial(self.QPushButton_cRankStocks_clicked, Fuct_Global.todayDate("%Y-%m-%d")))
        self.ui.QPushButton_cRankChice.clicked.connect(partial(self.QPushButton_cRankChice_clicked))
        self.ui.QPushButton_cLimit.clicked.connect(partial(self.QPushButton_cLimit_clicked, Fuct_Global.lastdayDateTime("%Y-%m-%d %H:%M")))
        self.ui.QPushButton_cLimitChice.clicked.connect(partial(self.QPushButton_cLimitChice_clicked))
        self.ui.QPushButton_cFuctuation.clicked.connect(partial(self.QPushButton_cFuctuationChice_clicked))

        # 添加按钮到界面
        for button in buttonList:
            self.ui.horizontalLayout_6.addWidget(button)

    def UpdateMenu(self,mButtonName):
        # 刷新二级菜单
        mButtonName = str(mButtonName)

        for data in self.MenuLink:
            if data["MainTitle"] == mButtonName:
                for button in data["CMenu"]:
                    button.show()
            else:
                for button in data["CMenu"]:
                    button.hide()

    def KeepButtonStatus(self):
        # 保持按钮高亮
        Button_List = [self.ui.QToolButton_mRankList,self.ui.QToolButton_mNews,self.ui.QToolButton_mSecType,
                       self.ui.QPushButton_cFuctuation,self.ui.QToolButton_mLimit]
        for toolButton in Button_List:
            toolButton.setCheckable(True)
            toolButton.setAutoExclusive(True)

    def mousePressEvent(self,event):
        """鼠标点击事件"""
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self,event):
        """鼠标移动事件"""
        if event.buttons() ==QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    # 登陆状态----------------------------------------------------------------
    def setLoginStatus(self, status):
        # 0成功
        self.LoginStatus = status
        self.ui.QToolButton_Login.setText(u"已登录")

    # 表格函数-----------------------------------------------------------------
    def initMyToolBox(self):
        """设置二维表格"""
        self.MyTable.setRowCount(len(self.dataList)+5)
        self.MyTable.setColumnCount(len(self.headerList))
        for i in Fuct_TableHeader.headerWidth[self.tableType]:
            self.MyTable.setColumnWidth(i,300)  # 设置宽度
        self.MyTable.setHorizontalHeaderLabels(self.headerList)

    def initToolBox(self):
        """设置二维表格"""
        self.layout = QVBoxLayout()
        self.MyTable = QTableWidget()
        self.layout.addWidget(self.MyTable)
        self.ui.tab1.setLayout(self.layout)
        # 设为行交替颜色
        self.MyTable.setAlternatingRowColors(True)
        # 初始化右键菜单
        self.initMenu()
        # 隐藏表头
        self.MyTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.MyTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置表头信号槽
        self.MyTable.horizontalHeader().sectionClicked.connect(self.resultSort)

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

    def DoubleClicked(self, Item=None):
        """双击展示日线"""
        if self.tmp_dataList != self.dataList[Item.row()][1]:
            self.slavewindow = UI_Global.DayLines(self.dataList[Item.row()][1])
            self.slavewindow.show()
            self.tmp_dataList = self.dataList[Item.row()][1]
        elif self.slavewindow.Status is False:
            self.slavewindow = UI_Global.DayLines(self.dataList[Item.row()][1])
            self.slavewindow.show()
            self.tmp_dataList = self.dataList[Item.row()][1]

    def detail(self):
        """详情展示"""
        self.show_message(u"功能添加中")

    def copy(self):
        """复制选中证券代码"""
        data = [self.MyTable.item(i.row(), 1).text() for i in self.MyTable.selectedIndexes()]
        data = set(data)
        clipboard = QtGui.QApplication.clipboard()
        clipboard.setText(",".join(data))
        self.show_message(u"复制选中证券代码成功")

    def copyAll(self):
        """复制全部证券代码"""
        data = [i[1] for i in self.dataList]
        clipboard = QtGui.QApplication.clipboard()
        clipboard.setText(",".join(data))
        self.show_message(u"复制全部证券代码成功")

    def saveToCsv(self):
        """保存表格内容到CSV文件"""
        # 先关闭右键菜单
        self.menu.close()

        # 获取想要保存的文件名
        path = QtGui.QFileDialog.getSaveFileName(self, u'保存数据', '', 'CSV(*.csv)')

        try:
            if not os.path.exists(path):
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

        self.dataList.sort(key=lambda x: x[index])
        if len(self.tmp_dataList) > 0:
            if self.tmp_dataList == self.dataList:
                self.dataList = self.dataList[::-1]
        # 数据深拷贝
        self.tmp_dataList = copy.deepcopy(self.dataList)
        self.addReportData()

    def addReportData(self):
        """向表格中填写数据"""

        self.MyTable.clear()  # 清空表头及表数据
        self.initMyToolBox()  # 二维表格初始化行列、设置表头
        for i in range(len(self.dataList)):
            for j in range(len(self.dataList[i])):
                Data = self.dataList[i]
                Info = Data[j]
                # 为保证排序正确，self.dataList数据中不包含%
                # 如果表格头中包含%，在设置数据时将%加上
                if "%" in self.headerList[j]:
                    Info = unicode(Info)+u"%"
                Info = unicode(Info)
                newItem = QTableWidgetItem(Info)
                # 添加提示气泡
                newItem.setToolTip(Info)
                if j == 4 and Data[4] > 0:
                    newItem.setTextColor(QColor(255, 0, 0))
                elif j == 4 and Data[4] < 0:
                    newItem.setTextColor(QColor(0, 255, 0))
                if j == 11 and Data[11] >= 30 and 11 > Data[4] > 9.9:
                    newItem.setTextColor(QColor(255, 0, 0))
                elif j == 11 and Data[11] < 30:
                    newItem.setTextColor(QColor(0, 255, 0))
                self.MyTable.setItem(i, j, newItem)
                newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # 绑定双击事件
        self.connect(self.MyTable, SIGNAL("itemDoubleClicked (QTableWidgetItem*)"), self.DoubleClicked)
        self.MyTable.show()

    def closeTab(self, index):
        # 关闭Tab页面
        self.ui.tabWidget.removeTab(index)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    import qdarkstyle
    app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())