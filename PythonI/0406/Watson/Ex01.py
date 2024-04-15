# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 19:14:13 2023

@author: USER
"""

student = {"David":99,"Peter":88,"Mary":100}

print("Bill" in student)

print("Mary" in student)

print()

while True:
    search = input("請輸入學生q(exit)：")
    
    if search == 'q':
        break
    
    if search in student:
        print(search,"分數：",student[search])
        
    else:
        
        score = int(input("請輸入分數："))
        student[search] = score
        
        
print(student)        