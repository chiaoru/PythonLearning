# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 20:58:41 2023

@author: USER
"""

score = {"David":99, "Tom": 89}

score['Bill'] = 90

score.setdefault('Peter')

print("分數：", score)

score['Peter'] = 61

score.update({'Mary':91}) # update 更新
print(score)

# 排序
print("依姓名排序") # 預設為遞增排序

for key in sorted(score):
    print("%-10s %d" %(key, score[key]))
    
score.pop("Bill") # pop 移除

print("遞減排序")
for key in sorted(score, reverse=True):
    print("%-10s %d" %(key, score[key]))
    
print("字典清除:", score.clear(), score)

score.update(David=87, John=66)
print(score)