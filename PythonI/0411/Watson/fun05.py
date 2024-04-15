# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 20:26:30 2023

@author: USER
"""

#預設值引數

#函式中若有預設值引數時，你的位置引數必須在預設值引數之前，不可以在後


def student(name,sex,school='聯成',age=19):
    print('姓名：',name)
    print('性別：',sex)
    print('學校：',school)
    print(age)
    
    
    
student('Bill','男')    

student('Mary','女','台中女中')

student('Mary','女','台中女中',16)

student('Peter','男',age=14)

