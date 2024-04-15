# -*- coding: utf-8 -*-
"""
Created on Thu May  4 20:01:53 2023

@author: USER
"""


fn = "file04.txt"



data = ['聯成','電腦','python']

with open(fn,'a',encoding='utf-8') as f:
    

    
    for line in data:
        f.write(line + '\n')