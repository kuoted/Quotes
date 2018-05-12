# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtGui import *
# import Fuct_QThreadUI
from functools import partial
import urllib
import socket
import Fuct_Global

# 设置全局socket超时2秒
socket.setdefaulttimeout(4)

"""
其他窗口
"""
# 日线窗口
class DayLines(QWidget):
    def __init__(self,code, parent = None):
        super(DayLines,self).__init__(parent)
        self.setWindowTitle(u'日线')
        self.days = 30
        self.Status = True
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Imag/Imag/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowFlags(Qt.Qt.WindowStaysOnTopHint|Qt.Qt.WindowMinimizeButtonHint)
        self.mainlayout = QGridLayout(self)
        self.mainlayout.setContentsMargins(0,0,0,0)
        self.myLabelEx = myLabel()
        self.mainlayout.addWidget(self.myLabelEx)
        self.File = "./data/tmp/Quote.png"
        if code[0] == "6":
            self.code = "0" + code
        else:
            self.code = "1" + code
        self.setPng()
        self.connect(self.myLabelEx, QtCore.SIGNAL('setpng'), self.CalcDays)

    def setPng(self):
        # 获取并设置图片
        url = "http://img1.money.126.net/chart/hs/kline/day/%d/%s.png" %(self.days,self.code)
        for i in range(5):
            content = urllib.urlopen(url).read()
            if len(content) > 10000:
                with open(self.File,"wb") as F:
                        F.write(content)
                self.myLabelEx.setPixmap(QPixmap(self.File))#####设置标签图片
                self.tmpCode = self.code
                self.tmpDays = self.days
                break

    def CalcDays(self):
        # 计算天数
        if self.days == 30:
            self.days = 90
        elif self.days == 90:
            self.days = 180
        else:
            self.days = 30
        self.setPng()

    def closeEvent(self, QCloseEvent):
        self.Status = False

# 重写QLabel，加入点击事件，用来显示日线数据
class myLabel(QLabel):
    def __init__(self, parent=None):
        super(myLabel, self).__init__(parent)

    def mousePressEvent(self, e):
        # 重载点击信号
        self.emit(QtCore.SIGNAL("setpng"))

# 龙虎榜日期控件
class dateWindow(QWidget):
    def __init__(self, parent=None):
        super(dateWindow, self).__init__(parent)
        self.setWindowTitle(u'日期查询')
        self.resize(300, 350)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Imag/Imag/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowFlags(Qt.Qt.WindowStaysOnTopHint)
        self.cal = QtGui.QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.label = QtGui.QLabel(self)
        self.button = QtGui.QPushButton(self)
        self.button.setText(u"查   询")
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.cal)
        vbox.addWidget(self.button)
        self.setLayout(vbox)
        self.connect(self.cal, QtCore.SIGNAL('selectionChanged()'), self.showDate)
        self.button.clicked.connect(partial(self.button_clicked))

    def button_clicked(self):
        date = self.cal.selectedDate()
        date = str(date.toPyDate())
        self.emit(QtCore.SIGNAL("RankChice_dateWindow"), date)

    def showDate(self):
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))

# 涨停预测，自定义时间
class limitWindow(QWidget):
    def __init__(self, parent=None):
        super(limitWindow, self).__init__(parent)
        self.setWindowTitle(u'涨停预测')
        self.resize(300, 100)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Imag/Imag/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowFlags(Qt.Qt.WindowStaysOnTopHint)
        # 定义控件
        self.label1 = QtGui.QLabel(self)
        self.label2 = QtGui.QLabel(self)
        self.edit = QtGui.QLineEdit()
        self.button = QtGui.QPushButton(self)
        # 设置控件
        self.label1.setText(u"*时间格式：2017-06-28 15:00")
        self.label1.setStyleSheet("color:rgb(255, 0, 0);")
        self.label2.setText(u"开始时间：")
        self.edit.setText(Fuct_Global.lastdayDateTime("%Y-%m-%d"+" 15:00"))
        self.button.setText(u"开始检索")

        vbox1 = QtGui.QVBoxLayout()
        hbox1 = QtGui.QHBoxLayout()

        hbox1.addWidget(self.label2)
        hbox1.addWidget(self.edit)

        vbox1.addWidget(self.label1)
        vbox1.addLayout(hbox1)
        vbox1.addWidget(self.button)
        self.setLayout(vbox1)
        self.button.clicked.connect(partial(self.button_clicked))

    def button_clicked(self):
        date = self.edit.text()
        date = date.replace("：",":").replace("  "," ").strip()
        self.close()
        self.emit(QtCore.SIGNAL("limit_dateWindow"), date)


# 涨跌幅追踪，自定义时间
class fuctuationWindow(QWidget):
    def __init__(self, parent=None):
        super(fuctuationWindow, self).__init__(parent)
        self.setWindowTitle(u'涨跌幅追踪')
        # self.resize(300, 100)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Imag/Imag/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowFlags(Qt.Qt.WindowStaysOnTopHint)
        # 定义控件
        self.label1 = QtGui.QLabel(self)
        self.label2 = QtGui.QLabel(self)
        self.editStart = QtGui.QLineEdit()
        self.editEnd = QtGui.QLineEdit()
        self.QToolButtonStart = QtGui.QToolButton(self)
        self.QToolButtonEnd = QtGui.QToolButton(self)
        self.button = QtGui.QPushButton(self)
        # 定义控件
        day1 = QtGui.QPushButton(self)
        day1.setText(u"近一天")
        day2 = QtGui.QPushButton(self)
        day2.setText(u"近两天")
        day3 = QtGui.QPushButton(self)
        day3.setText(u"近三天")

        week1 = QtGui.QPushButton(self)
        week1.setText(u"近一周")
        week2 = QtGui.QPushButton(self)
        week2.setText(u"近两周")
        week3 = QtGui.QPushButton(self)
        week3.setText(u"近三周")

        month1 = QtGui.QPushButton(self)
        month1.setText(u"近一月")
        month2 = QtGui.QPushButton(self)
        month2.setText(u"近两月")
        month3 = QtGui.QPushButton(self)
        month3.setText(u"近三月")


        # 设置图标
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Imag/Imag/calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QToolButtonStart.setIcon(icon1)
        self.QToolButtonStart.setAutoRaise(True)
        self.QToolButtonEnd.setIcon(icon1)
        self.QToolButtonEnd.setAutoRaise(True)
        # 设置控件
        self.label1.setText(u"开始日期:")
        self.label2.setText(u"结束日期:")
        self.button.setText(u"开始检索")

        grid = QtGui.QGridLayout()
        grid.addWidget(day1, 0, 0)
        grid.addWidget(day2, 0, 1)
        grid.addWidget(day3, 0, 2)

        grid.addWidget(week1, 1, 0)
        grid.addWidget(week2, 1, 1)
        grid.addWidget(week3, 1, 2)

        grid.addWidget(month1, 2, 0)
        grid.addWidget(month2, 2, 1)
        grid.addWidget(month3, 2, 2)


        vbox1 = QtGui.QVBoxLayout()
        hbox1 = QtGui.QHBoxLayout()
        hbox2 = QtGui.QHBoxLayout()

        hbox1.addWidget(self.label1)
        hbox1.addWidget(self.editStart)
        hbox1.addWidget(self.QToolButtonStart)

        hbox2.addWidget(self.label2)
        hbox2.addWidget(self.editEnd)
        hbox2.addWidget(self.QToolButtonEnd)

        vbox1.addLayout(grid)
        vbox1.addLayout(hbox1)
        vbox1.addLayout(hbox2)
        vbox1.addWidget(self.button)
        self.setLayout(vbox1)
        self.button.clicked.connect(partial(self.button_clicked))

    def button_clicked(self):
        start = self.editStart.text()
        end = self.editEnd.text()
        self.emit(QtCore.SIGNAL("fuctuation_dateWindow"), start, end)

if __name__ == '__main__':
    pass