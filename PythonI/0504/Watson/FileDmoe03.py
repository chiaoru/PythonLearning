# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:39:25 2023

@author: USER
"""

fn = "file02.txt"

with open(fn,encoding='utf-8') as fObj:
    
    datas = fObj.readlines()
    

for line in datas:
    print(line.strip()) # 去除前後空白
    
    
print(datas[2])    
    


   