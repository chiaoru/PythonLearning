# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:43:48 2023

@author: USER
"""

students = ['Bill', 'Mary', 'David', 'Peter']

# remove 移除
students.remove('David')
print(students) # 串列中有一樣的元件才能被移除

#students.remove('Tom') # error: x not in list，可用count防呆
if students.count('Tom') > 0:
    students.remove('Tom')
    
    
print()    
    
# pop 取出不放回
number = [1,2,3,4,5,6,7,8]
n = number.pop() # 由後往前抓
print(n)
print(number)

n = number.pop(5) # 抓索引值內的值
print(n)
print(number)



 
