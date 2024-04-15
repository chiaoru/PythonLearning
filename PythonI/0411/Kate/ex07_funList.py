# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:11:55 2023

@author: USER
"""

# 不定長度引數(參數不定)，會以 串列 來承接，可自行決定要輸入多少參數

def showStudents(*stud): # * 表示串列
    #print(stud)
    for item in stud:
        print('學生:', item)
    
showStudents()
showStudents('David','Peter', 'Mary')


def employee(name, pay, *work, area): # 參數area 需用關鍵字引數，否則error
    print('員工:', name)
    print('薪資:', pay)
    for item in work:
        print('工作內容:', item)
    print('工作地點:', area)
    
employee('Bill', 45000, '睡覺', '喝茶', '看Youtube', area='台中市')