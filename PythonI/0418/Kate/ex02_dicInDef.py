# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:00:17 2023

@author: USER
"""

def students(title, **personal):
    print(title, '依姓名來排序')
    for key in sorted(personal):
        print("{0:8s}的分數是{1}".format(key,personal[key]))

    print('-'*30)
    
    
    low60 = {k:v for k,v in personal.items() if v < 60}
    
    count = len(low60)
    print("不及格的人有:", count, "人!")
    print(low60)


students('111學年度第一次評量', Mary=61, Bill=63, David=31, Peter=49, Sue=51, Tom=92)
