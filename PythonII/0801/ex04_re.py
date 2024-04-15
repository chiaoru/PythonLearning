# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 21:20:25 2023

@author: USER
"""

# 正則表達式

import re

# [a-z] 任何小寫
# [A-Z] 任何大寫
# [A-Za-z0-9]
# [^0-9] 找出非數字外的字 

text = "https://www.lccnet.com.tw"
text2 = "python聯成電腦"

print(re.match("https", text))
print(re.match('https', text).span())
print(re.match('lccnet',text))
print(re.match('Python', text2))
print(re.match('Python', text2, flags=re.I))