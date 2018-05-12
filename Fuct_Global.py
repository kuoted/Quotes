# -*- coding: utf-8 -*-

"""
包含一些开放中常用的函数
"""

import decimal
import json
import datetime

MAX_NUMBER = 10000000000000
MAX_DECIMAL = 2


# ----------------------------------------------------------------------
def safeUnicode(value):
    """检查接口数据潜在的错误，保证转化为的字符串正确"""
    # 检查是数字接近0时会出现的浮点数上限
    if type(value) is int or type(value) is float:
        if value > MAX_NUMBER:
            value = 0

    # 检查防止小数点位过多
    if type(value) is float:
        d = decimal.Decimal(str(value))
        if abs(d.as_tuple().exponent) > MAX_DECIMAL:
            value = round(value, ndigits=MAX_DECIMAL)
    return float(value)


# ----------------------------------------------------------------------
def loadSetting():
    """载入MongoDB数据库的配置"""
    try:
        f = file("VT_setting.json")
        setting = json.load(f)
        host = setting['mongoHost']
        port = setting['mongoPort']
        logging = setting['mongoLogging']
    except:
        host = 'localhost'
        port = 27017
        logging = False
    return host, port, logging

# ----------------------------------------------------------------------
def todayDate(model):
    """获取当前本机电脑时间的日期"""
    # time.strftime("%Y/%m/%d_%H:%M:%S_401408", time.localtime())
    return datetime.datetime.today().strftime(model)

def lastdayDateTime(model):
    # 获取前一天时间
    # "%Y-%m-%d %H:%M"
    d1 = datetime.datetime.today() + datetime.timedelta(days=-1)
    d1 = d1.strftime(model)
    return d1

def FistdayDateTime(trange):
    # 获取前trange天日期
    # "%Y-%m-%d %H:%M"
    d1 = datetime.datetime.today() + datetime.timedelta(days=-trange)
    d1 = d1.strftime("%Y-%m-%d")
    return d1

def CreatDateList(StartDate, EndDate):
    # 计算日期区间所有日期
    tTime = []
    d1 = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
    while True:
        tTime.append(d1.strftime("%Y-%m-%d"))
        d1 = d1 + datetime.timedelta(days=1)
        if d1.strftime("%Y-%m-%d") == EndDate:
            tTime.append(d1.strftime("%Y-%m-%d"))
            break
    return tTime
# print lastdayDateTime()