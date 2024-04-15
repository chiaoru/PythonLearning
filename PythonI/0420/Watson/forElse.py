# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 21:42:21 2023

@author: USER
"""


for i in range(2,101):
    for x in range(2,i):
        if i % x == 0:
            break
        
    else:
        print(i,'是質數')
