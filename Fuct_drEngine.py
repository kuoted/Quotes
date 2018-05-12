# encoding: UTF-8

'''
数据记录引擎
'''

import sys
import Fuct_LocalData
import Fuct_Global
import socket

# 设置全局socket超时2秒
socket.setdefaulttimeout(4)

########################################################################
class DrEngine(object):
    """数据记录引擎"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass

    def Cache_RankList(self):
        """龙虎榜"""
        today = Fuct_Global.todayDate("%Y-%m-%d")
        StartDate = Fuct_Global.FistdayDateTime(180)
        print today,StartDate
        DateList = Fuct_Global.CreatDateList(StartDate, today)
        for date in DateList:
            print u"获取龙虎榜:", date
            Fuct_LocalData.RankList_Data(date)

if __name__=="__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')
    dr = DrEngine()
    dr.Cache_RankList()