# -*- coding: utf-8 -*-
"""
Created on Thu May 18 19:29:32 2023

@author: USER
"""

# 相似 like SQL語法

import sqlite3

connect = sqlite3.connect("demo.db")

try:
    while True:
        name = input("請輸入欲搜尋姓名的關鍵字，q離開：")
        if name == 'q':
            break
        sql = "select * from students where name like '%{}%'".format(name) # 只要有 君 都出現
        
        #sql = "select * from students where name like '%{}'".format(name) # 當 君 在最後一次時，都出現
        #sql = "select * from students where name like '{}%'".format(name) # 當 君 在第一字時，都出現
        #sql = "select * from students where name like '{}'".format(name) # 等於 name == '君君'
        
        cursor = connect.cursor()
        cursor.execute(sql)
        
        data = cursor.fetchall()
        
        if data == None:
            print("找不到!")
            
        else:
            for row in data:
                print("姓名：", row[1])
                print("年齡：", row[2])
                print("生日：", row[4])
                print()

finally:
    connect.close()