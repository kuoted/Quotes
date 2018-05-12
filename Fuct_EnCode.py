# -*- coding: utf-8 -*-
import base64
import re
# import hashlib
# import time

"""
对称加解密
"""

def encode_two(key,s):
    s1 = base64.encodestring(s) #64外层加密
    list = re.findall(r'.{1}',s1) #拆分分列表
    data = ''
    for s2 in list:
        D1 = encrypt(key, s2) #内层加密
        data = data+D1
    return data
    
def decode_two(key,s):
    list = re.findall(r'.{2}',s)
    data = ''
    for s2 in list: 
        D1 = decrypt(key, s2) #内层解密
        data = data+D1
    s2 = base64.decodestring(data) #64外层解密
    return s2
    
def encrypt(key, s):
    b = bytearray(str(s))
    n = len(b) # 求出 b 的字节数
    c = bytearray(n*2)
    j = 0
    for i in range(0, n):
        b1 = b[i]
        b2 = b1 ^ key # b1 = b2^ key
        c1 = b2 % 16
        c2 = b2 // 16 # b2 = c2*16 + c1
        c1 = c1 + 65
        c2 = c2 + 65 # c1,c2都是0~15之间的数,加上65就变成了A-P 的字符的编码
        c[j] = c1
        c[j+1] = c2
        j = j+2
    return c

def decrypt(key, s):
    c = bytearray(str(s))
    n = len(c) # 计算 b 的字节数
    if n % 2 != 0 :
        return ""
    n = n // 2
    b = bytearray(n)
    j = 0
    for i in range(0, n):
        c1 = c[j]
        c2 = c[j+1]
        j = j+2
        c1 = c1 - 65
        c2 = c2 - 65
        b2 = c2*16 + c1
        b1 = b2^ key
        b[i]= b1
    try:
        return b
    except:
        return "failed"

# def suanmd5():
#     # 计算MD5
#     src = 'Qtrader'+time.strftime('%Y%m%d',time.localtime(time.time()))
#     m2 = hashlib.md5()
#     m2.update(src)
#     # return m2.hexdigest()

if __name__ == "__main__":
    # key = 999
    # data = "abasdasdfasdfa~!@#$%^&*(sdffasd"
    # data1 = encode_two(key, data)
    # data2 = decode_two(key, data1)
    # print suanmd5()
    pass