# -*- coding: utf-8 -*-
"""
Created on Tue May  9 20:07:24 2023

@author: USER
"""

import csv

fileName = 'YouBike.csv'

with open(fileName,encoding='utf-8') as fO:
    csvReader = csv.reader(fO)
    
    for row in csvReader:
        print('Row %s = ' % csvReader.line_num,row)