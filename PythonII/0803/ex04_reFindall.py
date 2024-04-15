# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:38:32 2023

@author: USER
"""

import re

text = "find abbbbc, bc, skip c, bbbbcc"

pattern = "a*b+c" 
# * 前一字元或括弧內出現零次或多次
    # aaaaab  aaab  ab 皆符合
# + 前一字元至少要出現一次或多次
    # bbb b
    
result = re.findall(pattern, text)
print(result)

text2 = "good 123 Ya 456 lccnet 789"
result = re.findall('([a-z]+)', text2) # 至少要有一次英文字a-z
print(result)

text3 = "year 2023 Month 08 day 03"
pattern = "[0-9]+"
result = re.findall(pattern, text3)  # 至少要有一次數字0-9
print(result)

pattern = "[A-Za-z]"
result = re.findall(pattern, text3) # 只要有英文字就被抓入 (單個)
print(result)

pattern = "[A-Za-z]+"
result = re.findall(pattern, text3)  # 只要至少有一個英文字就被抓入 (單字)
print(result)

pattern = "a*b*c" 
result = re.findall(pattern, text)
print(result)



