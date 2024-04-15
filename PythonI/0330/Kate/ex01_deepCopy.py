# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 19:53:23 2023

@author: USER
"""

number = [[10,20,30],[1,2],[2,3,4,5,6]]

print(number[1][0])

for item in number: # item 是串列
    for i in item:
        print(i, end=",")
    print()
    
"""
可變形別(型態)：記憶體位置相同，但內容可改變，如串列、字典。
不可變形別(型態)：整數、字串、元組。

淺複製：對於不變型別的改變不受影響，對可變形別的修改會受影響，用於一維串列。
深複製:對於可變形別與不變型別的修改都不受影響，用於二為串列。

"""  

import copy

# 淺複製
list1 = [1,2,3,4,5]
list2 = [1, [2,3]]

newlist1 = copy.copy(list1)
newlist2 = copy.copy(list2)

list1[0] = 100
print(list1)
print(newlist1)

list2[1][0] = 100
print(list2)
print(newlist2)

# 深複製 deep copy
newlist3 = copy.deepcopy(list1)
newlist4 = copy.deepcopy(list2)

list2[1][1] = 99
print(list2)
print(newlist4)








