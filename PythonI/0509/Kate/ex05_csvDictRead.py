# -*- coding: utf-8 -*-
"""
Created on Tue May  9 20:15:04 2023

@author: USER
"""

import csv

fileName = 'YouBike.csv'

with open(fileName, encoding='utf-8') as fO:
    csvdict = csv.DictReader(fO) # 建立字典的閱讀器
    for row in csvdict:
        #print(row)
        
        print('站名:', row['sna'])
        print('地址:', row['ar'])
        print()
    