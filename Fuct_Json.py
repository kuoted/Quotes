# -*- coding: utf-8 -*-

import json

"""
Json处理
"""
# 将字典转换为json
def Encode(json_data):
    try:
        return json.dumps(json_data)
    except:
        return False

# 将json转换为字典
def Decode(data):
    try:
        return json.loads(data)
    except:
        return False

if __name__ == '__main__':
    print(Decode("{\"status\":\"2\"}"))