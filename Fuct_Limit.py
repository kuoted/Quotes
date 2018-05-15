# -*- coding: utf-8 -*-
import importlib

import re, time
import requests

import numpy as np
from pandas import DataFrame
import sys
importlib.reload(sys)

#sys.setdefaultencoding('utf8')
import Fuct_TS
'''
获取涨停预报
'''

class SDU_Spider():

    def __init__(self, StartTime):
        self.page = 100             # 网页page数量
        self.SuccessNumLimit = 20   # 成功数限制
        self.SuccessRateLimit = 20  # 成功率限制
        self.StartTime = StartTime    # 开始时间"2017-06-28  15:00"
        self.stock_basics = Fuct_TS.get_stock_basics()

    def FindPage(self):
        Data_List = []
        for i in range(1, self.page+1):
            time.sleep(1)
            url = 'http://www.178448.com/fjzt-1.html?page=' + str(i)
            try:
                print( "===================%s========================="%str(i) )
                r = requests.get(url, timeout=5)
                print( url )
                opage_list,Status = self.Web_Parser(r.text)
                if Status:
                    Data_List = Data_List + opage_list
                else:
                    print( "Status:", Status )
                    break
            except Exception as e:
                print( "===================ERROR=========================" )
                print( Exception,e )
                print( url )
        self.HeBin(Data_List)

    def Web_Parser(self,string):
        string = re.findall("<tbody>(.*?)</tbody>",string, re.S)[0]
        fjzt_list = re.findall("<tr>(.*?)</tr>",string, re.S)
        opage_list = []
        Status = True
        for fjzt in fjzt_list:
            sfjzt = re.findall("<td>(.*?)</td>",fjzt, re.S)
            user = re.findall("<a href=.*?\">(.*?)</a>",fjzt, re.S)[0]  # 伏击用户
            SuccessNum = re.findall("<td class=\"bzt\">(.*?)</td>",fjzt, re.S)[0]  # 伏击成功数
            SuccessRate = sfjzt[1]  # 伏击成功率
            secShortName = sfjzt[2]  # 股票简称
            AmbushSeason = sfjzt[3]  # 伏击原因
            AmbushTime = str(sfjzt[4].replace("  "," "))  # 伏击日期
            Ambush_Price = sfjzt[5]  # 伏击价格
            if float(SuccessNum)>self.SuccessNumLimit and float(SuccessRate[:-1]) > self.SuccessRateLimit:
                for s in ["QQ","买点","咨询","http"]:
                    if s in AmbushSeason:
                        continue
                f_list = [AmbushTime,SuccessRate,user,secShortName,AmbushSeason,Ambush_Price,SuccessNum]
                if AmbushTime > self.StartTime:
                    opage_list.append(f_list)
                    Status = True
                    print( AmbushTime,SuccessRate,user,secShortName,AmbushSeason,Ambush_Price,SuccessNum )
                else:
                    # print AmbushTime, self.StartTime
                    # print type(AmbushTime), type(self.StartTime)
                    Status = False
        return opage_list,Status

    def HeBin(self,Data_List):
        """数据合并后写文件"""
        columns_list = [u"伏击日期",u"成功率",u"伏击人",u"证券简称",u"伏击理由",u"伏击价格",u"成功数"]
        rdata = DataFrame(np.array(Data_List),columns = columns_list)
        secShortNameList = set(rdata[u'证券简称'].tolist())
        Data_List = []
        for secShortName in secShortNameList:
            AmbushTime = ",".join(set(rdata[u'伏击日期'][rdata[u'证券简称'] == secShortName].tolist()))
            SuccessRate = rdata[u'成功率'][rdata[u'证券简称'] == secShortName].tolist()
            for i,v in enumerate(SuccessRate):
                SuccessRate[i] = float(v.replace("%","").strip())
            SuccessRate = sum(SuccessRate) // len(SuccessRate)
            user = rdata[u'伏击人'][rdata[u'证券简称'] == secShortName].tolist()
            AmbushSeason = rdata[u'伏击理由'][rdata[u'证券简称'] == secShortName].tolist()
            for i in range(len(AmbushSeason)):
                try:
                    AmbushSeason[i] = str(AmbushSeason[i])
                except:
                    pass
            AmbushSeason = ",".join(AmbushSeason)
            PriceList = rdata[u'伏击价格'][rdata[u'证券简称'] == secShortName].tolist()
            for i in range(len(PriceList)):
                PriceList[i] = float(PriceList[i].strip())
            Ambush_Price = sum(PriceList)//len(PriceList)
            SuccessNumList = rdata[u'成功数'][rdata[u'证券简称'] == secShortName].tolist()
            for i in range(len(SuccessNumList)):
                SuccessNumList[i] = float(SuccessNumList[i].strip())
            SuccessNum = sum(SuccessNumList) // len(SuccessNumList)
            UserCount = len(user)
            AmbushTime = self.CheckStrLen(AmbushTime)
            AmbushSeason = self.CheckStrLen(AmbushSeason)
            try:
                code = self.stock_basics["secID"][self.stock_basics['secShortName'] == secShortName.encode("gbk")].tolist()[0]
                code = code.replace(".XSHE","").replace(".XSHG","")
                Data_List.append([AmbushTime,code,secShortName,Ambush_Price,UserCount,SuccessNum,SuccessRate,AmbushSeason])
            except:
                pass
        self.Data_List = Data_List

    def CheckStrLen(self,string):
        # 检查字符串长度
        width = 50
        try:
            string = string.decode('utf-8')
            return unicode("\n".join([unicode(string[x:x + width]) for x in range(0, len(string), width)]))
        except:
            return string
if __name__=='__main__':
    mySpider = SDU_Spider("2017-06-28  15:00")
    mySpider.FindPage()
    Data_List = mySpider.Data_List
    print( Data_List )