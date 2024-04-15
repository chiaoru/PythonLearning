# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 20:52:28 2023

@author: USER
"""

# 新增串列資料

# 方式一 append 加入 從最後面加入

scores = list() # 產生空白串列

while True: # 無窮迴圈，重複無限次，需用break 跳脫迴圈
    number = int(input("輸入分數，-1離開："))
    if number == -1:
        break
    scores.append(number) #將資料依序加進空白串列中

print(scores)

# 方式二 insert 插入 從想要的位置插入
number = [10,20,30,40,50]

number.insert(2,99) # 從第二位置 插入 99
print(number)

# 找出索引值位置 index ，使用index時，一定要有尋找的值，否則error
n = number.index(40) # 找出40的位置
print(n)

# count 找尋想搜尋的值有幾個，可協助找index個數，當count = 0 不可用index，會出現錯誤

count = number.count(200)
print("數量：", count)
