# -*- coding: utf-8 -*-

import requests
import Fuct_EnCode

"""
HTTP请求：POST
"""

sKey = 666
dkey = 888

# HTTP POST请求数据
def request_post(url, data):
    # data = Fuct_EnCode.encode_two(sKey, data)
    postdata = {"data": data}
    try:
        html = requests.post(url, postdata)
        result = html.text
        # result = Fuct_EnCode.decode_two(dkey, result)
    except:
        result = False

    return result

# HTTP GET请求数据
def request_get(url):
    try:
        html = requests.get(url)
        result = html.text
    except:
        result = False
    return result

if __name__ == '__main__':
    pass