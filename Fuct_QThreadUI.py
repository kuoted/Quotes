# -*- coding: utf-8 -*-

from PyQt5.QtCore import *

import Fuct_LocalData
import Fuct_Limit

"""
UI功能函数
"""

##########################################################################
class QPushButton_cRankStocks_clicked(QThread):
    """
    龙虎榜数据
    """
    log_signal = pyqtSignal(str)
    cRankStocks_finished = pyqtSignal(str, str)
    def __init__(self, date, parent=None):
        super(QPushButton_cRankStocks_clicked, self).__init__(parent)
        self.date = date
        self.header = "RankList"

    def __del__(self):
        self.working = False

    def run(self):
        DataList = Fuct_LocalData.RankList_Data(self.date)
        #self.emit(QtCore.SIGNAL("SIGNAL_QPushButton_cRankStocks"), self.header, DataList)
        self.cRankStocks_finished.emit(self.header, str(DataList))

##########################################################################
class QPushButton_cLimit_clicked(QThread):
    """
    涨停预测数据
    """
    log_signal = pyqtSignal(str)
    climit_finished = pyqtSignal('QString', 'QString')
    def __init__(self, date, parent=None):
        super(QPushButton_cLimit_clicked, self).__init__(parent)
        self.date = date
        self.header = "Limit"

    def __del__(self):
        self.working = False

    def run(self):
        # self.date "2017-06-28  15:00"
        mySpider = Fuct_Limit.SDU_Spider(self.date)
        mySpider.FindPage()
        DataList = mySpider.Data_List
        #self.emit(QtCore.SIGNAL("SIGNAL_QPushButton_cLimit"), self.header, DataList)
        self.climit_finished.emit(self.header, DataList)
