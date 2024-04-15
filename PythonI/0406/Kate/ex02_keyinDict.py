# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 19:45:14 2023

@author: USER
"""

member = {"Mary":30000, "Bill":1000000, "David":0}

keys = member.keys() # keys() 抓出所有key值，成為一個元組
values = member.values()
print(keys)
print(values)

items = member.items() # 分別一組一組抓出來
print(items)

listkeys = list(keys) # 傳換成串列
listvalues = list(values)
listitems = list(items) # 二維串列

print(listitems[1][1])
print("最小值：", min(listvalues))
print("最大值：", max(listvalues))

for  it in listitems:
    print(it)
    print(it[0], it[1])
    
print()

for k,v in listitems: # 二維串列中，每一組裡面有兩個值
    print(k,v)