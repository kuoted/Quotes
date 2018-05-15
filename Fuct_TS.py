# -*- coding: utf-8 -*-

"""
tuShare API
"""
import os
import datetime
import pandas as pd
import tushare as ts
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

# ----------------------------------------------------------------------
def TradeingDatGET():
    """获取最近一个交易日"""
    # 优先从本地文件获取
    year = datetime.datetime.today().strftime("%Y")
    toDay = datetime.datetime.today().strftime("%Y-%m-%d")
    filename = r'.\data\QTTradingDay\QTTradingDay%s.csv' %year
    # 如果本地不存在则获取后创建
    if not os.path.exists(filename):
        ts.trade_cal()[-365:].to_csv(filename)
    result = pd.read_csv(filename)
    for i in range(100):
        if int(result[u'isOpen'][result[u'calendarDate']==toDay.replace("-", "/")]) == 1:
            return toDay

def get_stock_basics():
    # 证券基本信息
    data = pd.read_csv("./data/tmp/stock_basics.csv")
    return data

if __name__ == '__main__':
    stock_basics = get_stock_basics()
    secShortName = "平安银行"
    # print stock_basics['secShortName'][0].decode("gbk")
    print( stock_basics["secID"][stock_basics['secShortName'] == secShortName.encode("gbk")].tolist()[0] )