# -*- coding: utf-8 -*-

import Fuct_Http
import Fuct_Json

"""
账户相关
"""

# 链接
host = "http://127.0.0.1/"
host = "http://qtrader.duapp.com/"
login_url = host+"login/"
checkLogin_url = host+"checkLogin/"
register_url = host+"register/"

get_test = host+"get/"

# 登录
def Login(event):
    event = Fuct_Json.Encode(event)
    return Fuct_Http.request_post(login_url, event)

# 登出
def Logout(event):
    return Fuct_Http.request_post(register_url, event)

# 账户注册
def Register(event):
    event = Fuct_Json.Encode(event)
    return Fuct_Http.request_post(register_url, event)

# 检查单点登录
def CheckLogin(event):
    return Fuct_Http.request_post(register_url, event)

# 测试
def get(event):
    return Fuct_Http.request_post(get_test, event)

if __name__ == '__main__':
    print( "Register：", Register({"userName":"KingMagic2","passWord":"Huawei@123","phone":"17358536853","qq":"542601619"}))