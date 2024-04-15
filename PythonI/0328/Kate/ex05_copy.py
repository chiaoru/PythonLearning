# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:56:40 2023

@author: USER
"""

# 複製

a = 10
b = a
number = [10,20,30,40]
num = number

print(a)
print(b)
print(number)
print(num)
print()
print(id(a)) #印出記憶體位置
print(id(b)) # 記憶體位置相同，(因內容相同，所以暫存於同一個記憶體位置，以節省空間)
print(id(number))
print(id(num))

a = 100 # 值改變，記憶體位置也被改變
print(b)
print(id(a)) #印出記憶體位置
print(id(b))
print(id(number))
print(id(num))

number[0] = 100 # 串列中某一個值被改變
print(id(number)) # 記憶體位置依然相同，因為記憶體位址為同一位址
print(num) # 串列中的值也會被影響
print(id(num))

number = [1,2,3,4]
num = [1,2,3,4] # 因為分別宣告，所以記憶體位置也會不同

data = [1,2,3,4,5]
num = []

for i in data:
    num.append(i)
print(num)

data[0] = 100

print(num) # 因為與data是不同的記憶體位置，所以當data的內容被改變時，num不會被影響