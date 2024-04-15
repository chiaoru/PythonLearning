# -*- coding: utf-8 -*-
"""
Created on Tue May  9 20:22:02 2023

@author: USER
"""

import csv

fileName = 'YouBike.csv'

with open(fileName,encoding='utf-8') as fO:
    
    csvdict = csv.DictReader(fO)
    
    for row in csvdict:
        print(row['sna'])
        print(row['ar])
        
   
