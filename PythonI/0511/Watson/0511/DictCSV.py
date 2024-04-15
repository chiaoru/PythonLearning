# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv

fileName = "dictcsv.csv"

with open(fileName,'w',encoding='utf-8' , newline='') as f:
    fields = ['name','sex','age']
    
    # 建立Writer 的物件
    dictWriter = csv.DictWriter(f, fieldnames=fields)
    
    # 寫入標題
    
    dictWriter.writeheader()

    dictWriter.writerow({'name':'陳美麗','sex':'女','age':'31'})
    dictWriter.writerow({'name':'陳聰明','sex':'男','age':'21'})    