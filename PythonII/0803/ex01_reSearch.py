# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 18:45:30 2023

@author: USER
"""

import re
text = "https://www.lccnet.com.tw"
text2 = "python聯成電腦python"

print(re.search('https', text).span())

print(re.search('lccnet',text).span())

print(re.search('python', text2).span())

# re.match 從頭開始找，如值在後方就找不到
# re.search 是只要值有符合就可以找到，但只找到第一個就結束


print(re.search('Python',text2))

# flags=re.I 忽略大小寫
print(re.search('Python',text2, flags=re.I).span())

# 要尋找的關鍵字有兩個以上可用 group()
print(re.search('python',text2).group())