# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 21:24:46 2023

@author: USER
"""


def sayHello(name):
    print(name, '你好')


def square(x):
    return x ** 2

    
sayHello('Bill')
print(square(5))

print('-'*30)

# 匿名函式 lambda : 程式碼會更精簡，不用定義名稱、程式碼一行、執行完會回傳
(lambda name:print(name, '你好'))('John')
sq = lambda x:x ** 2
print(sq(5))

sq2 = lambda x, y : x*y
print(sq2(2,5))