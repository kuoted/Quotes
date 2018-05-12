# -*- coding: utf-8 -*-
import Fuct_Json
import Fuct_Http
import Fuct_Global

"""
获取证券数据：
1、行情数据
2、其他接口数据
"""
# rankListUrl：龙虎榜
rankListUrl = "http://datainterface3.eastmoney.com//EM_DataCenter_V3/api/" \
              "LHBGGDRTJ/GetLHBGGDRTJ?tkn=eastmoney&mkt=0&dateNum=&startDateTime=%s&" \
              "endDateTime=%s&sortRule=1&sortColumn=&pageNum=1&pageSize=200&cfg=lhbggdrtj"

def rankList_Get(date):
    # 获取龙虎榜数据
    # date 日期
    url = rankListUrl % (date, date)
    result = Fuct_Http.request_get(url)
    if not result:
        result = ""
    return result

def rankList_Parser(result):
    # 解析龙虎榜数据
    # rankLists：龙虎榜数据列表
    # [u'日期', u'证券代码 ', u'证券简称', u'收盘价', u'涨跌幅', u'换手', u'龙虎榜\n买入额', u'龙虎榜\n卖出额', u'龙虎榜\n净买额(万)',
    #  u'市场总\n成交额(万)', u'净买额\n占成交比', u'买入额\n占总成交比', u'上榜原因', u'净买说明', ]
    s = Fuct_Json.Decode(result)
    if not s:
        return []
    rankLists = []
    for i in s["Data"][0]["Data"]:
        rankList = i.split("|")
        tem_rankList = []
        for index in [13,0,1,2,3,4,11,10,5,6,14,15,8,-1]:
            tem_rankList.append(rankList[index])
        # 数据格式化，校验小数位数
        # print tem_rankList[7], type(tem_rankList[7])
        for index, item in enumerate(tem_rankList):
            if item == "":
                tem_rankList[index] = 0
        tem_rankList[3] = Fuct_Global.safeUnicode(float(tem_rankList[3]))  # 收盘价
        tem_rankList[4] = Fuct_Global.safeUnicode(float(tem_rankList[4]))  # 涨跌幅
        tem_rankList[5] = Fuct_Global.safeUnicode(float(tem_rankList[5]))  # 换手
        tem_rankList[6] = Fuct_Global.safeUnicode(float(tem_rankList[6])/10000)  # 龙虎榜买入额
        tem_rankList[7] = Fuct_Global.safeUnicode(float(tem_rankList[7])/10000)  # 龙虎榜卖出额
        tem_rankList[8] = Fuct_Global.safeUnicode(float(tem_rankList[8])/10000)  # 龙虎榜净买额
        tem_rankList[9] = Fuct_Global.safeUnicode(float(tem_rankList[9])/10000)  # 总成交额(万)
        tem_rankList[10] = Fuct_Global.safeUnicode(float(tem_rankList[10]))  # 净买占比
        tem_rankList[11] = Fuct_Global.safeUnicode(float(tem_rankList[6])/float(tem_rankList[9])*100)  # 买入占比
        rankLists.append(tem_rankList)
    return rankLists

if __name__ == '__main__':
    rankList_Parser("2017-06-13")