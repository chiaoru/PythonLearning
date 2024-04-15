# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:44:22 2023

@author: USER
"""

# csv 以字典方式寫入
import csv

fileName = 'dictcsv.csv'

with open(fileName, 'w', encoding='utf-8' ,newline='') as f:
    # 欄位名稱定義
    fields = ['name', 'sex', 'age']
    
    # 建立 Writer 的物件
    dictWriter = csv.DictWriter(f, fieldnames=fields)
    
    # 寫入標題
    dictWriter.writeheader()
    
    # 依行用字典方式寫入資料
    dictWriter.writerow({'name':'陳美麗', 'sex':'女', 'age':'30'})
    dictWriter.writerow({'name':'陳聰明', 'sex':'男', 'age':'21'})
    