# -*- coding: utf-8 -*-
"""
Created on Thu May 18 18:47:32 2023

@author: USER
"""

import sqlite3

connect = sqlite3.connect("demo.db")

try:
    while True:
        name = input("請輸入姓名，q離開：")
        if name == 'q':
            break
        sql = "select * from students where name ='{}'".format(name)
        
        cursor = connect.cursor()
        cursor.execute(sql)
        
        data = cursor.fetchone()
        
        if data == None:
            print("找不到!")
            
        else:
            print("姓名：", data[1])
            print("年齡：", data[2])
            print("生日：", data[4])

finally:
    connect.close()