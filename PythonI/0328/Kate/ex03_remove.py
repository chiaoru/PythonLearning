# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:09:43 2023

@author: USER
"""

fruits = ['Banana', 'Apple', 'Melon', 'Watermelon']

while True:
    print('Currently, there are:', fruits)
    
    f = input('Please input the kind of fruits that you want to delete, Enter to quit:')
    if f == "":
        break
    if fruits.count(f) > 0:
        fruits.remove(f)
    else:
        print("No this kind of fruit!")
        