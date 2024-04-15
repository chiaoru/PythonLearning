# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:05:20 2023

@author: USER
"""

def students(title,**personal):
    print(title,"依姓名排序")
    
    for key in sorted(personal):
        print("{0:8s}的分數：{1}".format(key,personal[key]))
        
    print('-'*30)    
    
    low60 = {k:v for k,v in personal.items() if v < 60}
    count = len(low60)
    
    print('不及格有：',count,'人')
    print(low60)
    
    
    
students('111學度期第一次評量',Bill=50,Mary=88,David=46,Sue=59,Tom=99)    
    