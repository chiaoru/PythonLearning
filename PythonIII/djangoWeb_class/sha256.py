# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 19:11:16 2023

@author: USER
"""

# 加密演算法 SHA-256

import hashlib

pwd = '123456'

pwd_sha = hashlib.sha256(pwd.encode('utf-8')).hexdigest()

print('加密後的文字：', pwd_sha)