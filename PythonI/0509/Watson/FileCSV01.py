# -*- coding: utf-8 -*-
"""
Created on Tue May  9 19:57:39 2023

@author: USER
"""

import csv

fileName = 'YouBike.csv'

with open(fileName,encoding='utf-8') as fO:
    csvReader = csv.reader(fO)
    
    bike = list(csvReader)
    
print(bike)    

for row in bike:
    print(row[1])