# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 20:01:06 2023

@author: USER
"""

score = {"Tom":95, "Bill":78, "John":47, "Edward":67, 
         "Eric":52, "Ivy":67, "David":35}

# 字典生成式 comprehension
print("及格有\n", {k:v for k,v in score.items() if v >= 60})
print("不及格有\n", {k:v for k,v in score.items() if v <60})

print()

# zip 上下合併(對應)為一組，合併後為元組
minScore = min(zip(score.values(), score.keys())) # 因為以值先做判斷(min),所以values寫前面
maxScore = max(zip(score.values(), score.keys()))

print("最高分：", maxScore)
print("最低分：", minScore)

d1 = [1,2,3]
d2 = [4,5,6]

mixD = zip(d1,d2)
print(list(mixD)) # --> [(1, 4), (2, 5), (3, 6)]