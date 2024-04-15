# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:20:19 2023

@author: USER
"""

import db

print('UBike查詢')

while True:
    num = input('站名 => 1，地區查詢 => 2，地址查詢 => 3，離開 => q:')
    
    if num == 'q':
        break
    
    if num == '1':
        station = input('請輸入欲查詢的站名:')
        sql = "select * from ntpbike where station like '%{}%'".format(station)
        
    elif num == '2':
        sql = "select distinct area from ntpbike" # distinct SQL語法 略過重複項
        db.cursor.execute(sql)
        data = db.cursor.fetchall()
        for row in data:
            print(row[0], end=',') # 因為只抓了 area
        print()
        
        area=input('請輸入欲搜尋的地區:')
        sql = "select * from ntpbike where area='{}'".format(area)
        
        
    elif num == '3':
        address = input('請輸入欲查詢的地址:')
        
    db.cursor.execute(sql)
    data = db.cursor.fetchall()
    
    for row in data:
        print(row[1], row[3],row[4]) # station, rent,space

db.connect.close()
    