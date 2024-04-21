# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 18:51:27 2023

@author: USER
"""

# 加密演算法 hashlib
import hashlib # 雜湊

def MD5(word):
    md = hashlib.md5()
    md.update(word.encode(encoding='utf-8')) # 對字元進行編碼,如果沒有編碼，會出現 TypeError
    return md.hexdigest()

if __name__ == '__main__':
    msg = '123456abc'
    MD5_str = MD5(msg)
    print('加密後：', MD5_str)
    