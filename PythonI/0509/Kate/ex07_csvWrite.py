# -*- coding: utf-8 -*-
"""
Created on Tue May  9 21:41:56 2023

@author: USER
"""

import csv

fileName = 'mycsv2.csv'

allData = [['name', 'age', 'sex'], ['陳比爾', 18, 'M'], ['王美麗', 21, 'F']]

with open(fileName, 'w', encoding='utf-8', newline='') as fO: # newline='' 預設斷行 \n
    csvWriter = csv.writer(fO)
    
    for row in allData:
        csvWriter.writerow(row)
    