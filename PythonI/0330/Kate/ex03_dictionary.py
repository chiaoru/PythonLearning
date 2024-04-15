# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:44:47 2023

@author: USER
"""

# 字典 key: value

#直接定義方式
students = {"Tom":98,"David":70,"May":100}

print(type(students))
print(students["David"]) # 用key找值，有key才能被找到，否則error
#print(students["Bill"]) 

#第二種定義方式
fruit = dict(a="Apple", b="Banana")
print(fruit["b"])

number = dict() # 給予空字典
number = {} #兩種方式都可以
number[1] = "台中一中"
number[10] = "台中女中"
print(number)
print(number[10])

number[10] = "中興高中" # 修改值，因為key本來存在，如果沒有key值，則視為新增
print(number[10])

print(students.get("Bill"))
print(students.get("Bill",'沒有key'))