# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 19:15:53 2023

@author: USER
"""

student = {"David":99, "Peter":88, "Mary":100}

print("David" in student) # 用key 搜尋
print("Bill" in student)

print()

while True:
    search = input("請輸入學生姓名，q離開：")
    search.lower()
    
    if search == 'q':
        break
    if search in student:
        print(search, "分數：",student[search])
    else:
        score = int(input("請輸入學生分數："))
        student[search] = score

print(student)

