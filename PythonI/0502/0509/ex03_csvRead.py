# -*- coding: utf-8 -*-
"""
Created on Tue May  9 19:43:34 2023

@author: USER
"""

# 存取CSV(文字交換格式) 避免檔案格式不支援
# name,sex,tel,birthday
# 'Bill','M','09111111',2000-01-01
# 'Mary','F','09222222',2001-03-17

import csv

fileName = 'YouBike.csv'

with open(fileName, encoding='utf-8') as fO:
    csvReader = csv.reader(fO)
    bike = list(csvReader)
    
print(bike)

for row in bike:
    print("站點名稱:", row[1])
    print("地址:", row[8])
    print('可借:', row[2])
    print("可還:", row[3])
    print()