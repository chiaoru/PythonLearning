# -*- coding: utf-8 -*-
"""
Created on Tue May  9 21:20:17 2023

@author: USER
"""

import csv

fileName = 'mycsv.csv'

with open(fileName, 'w', encoding='utf-8', newline='') as fO: # newline='' 預設斷行 \n
    csvWritter = csv.writer(fO)
    
    csvWritter.writerow(['name', 'age', 'sex'])
    csvWritter.writerow(['Bill', 18, 'M'])
    csvWritter.writerow(['Mary', 25, 'F'])
    