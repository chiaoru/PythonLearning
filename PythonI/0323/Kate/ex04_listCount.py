# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 21:21:36 2023

@author: USER
"""

students = list()
scores = []

while True:
    name = input("搜尋學生姓名，q離開：")
    if name == "q":
        break
    if students.count(name) == 0: # 當找不到資料時，將新資料加入
        num = int(input("輸入分數："))
        students.append(name) # 將資料加入串列
        scores.append(num) # 因為同時放入，所以兩個索引值會相同
    else: # 當count > 0 代表找的到資料
        index = students.index(name) # 找到名字的位置 index
        sco = scores[index] # 以名字位置的索引值來搜尋分數
        print(name,"的分數是:",sco)
        