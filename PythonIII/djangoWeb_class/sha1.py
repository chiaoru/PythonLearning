# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 19:21:32 2023

@author: USER
"""

# 加密演算法 sha1 
import hashlib

pwd = 'abc電腦123'

sha1 = hashlib.sha1()
sha1.update(pwd.encode('utf-8'))

result = sha1.hexdigest()

print("加密後的文字：", result)

sha = hashlib.sha1()
sha.update(bytes(pwd, encoding='utf-8'))
res = sha.hexdigest()
print("用位元組編碼加密後的文字：", res)