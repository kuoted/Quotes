# -*- coding: utf-8 -*-

import os
import sys
import Fuct_DataAPI
import datetime
"""
获取数据接口。
读取本地数据：
    数据存在：读取本地数据后返回
    数据不存在：通过API接口获取数据后写文件，并将数据返回
"""

def RankList_Data(date):
    # 龙虎榜数据
    # 缓存最近数据
    # 查询最新一天数据
    # toDay = Fuct_Global.todayDate()
    filename = r'.\data\MktRankListStocks\RankListStocks%s.txt' %date
    # 如果本地不存在则获取后创建
    if os.path.exists(filename):
        with open(filename) as f:
            try:
                rankLists = Fuct_DataAPI.rankList_Parser(f.read())
            except:
                rankLists = ""
            return rankLists
    else:
        data = Fuct_DataAPI.rankList_Get(date)
        try:
            rankLists = Fuct_DataAPI.rankList_Parser(data)
        except:
            rankLists = ""
        # 将数据保存到本地
        if len(rankLists) > 0:
            with open(filename,"w") as f:
                f.write(data)
            return rankLists
        # 如果没有数据，日期递减100天并递归函数，直到获取到数据为止
        for i in range(100):
            i = 1
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            date = date + datetime.timedelta(-1)
            date = str(date)
            rankLists = RankList_Data(date)
            if rankLists > 0:
                return rankLists

# def

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    print RankList_Data("2017-06-12")