# -*- coding: utf-8 -*-
"""
Created on Thu May 18 21:41:52 2023

@author: USER
"""

import db
# 適用於sqlite 中的所有檔案，只要將 cursor, connect 做更改即可(連接來源不同)


try:
    while True:
        name = input("請輸入姓名，q離開：")
        if name == 'q':
            break
        sql = "select * from students where name ='{}'".format(name)
        
        db.cursor.execute(sql)
        
        data = db.cursor.fetchone()
        
        if data == None:
            print("找不到!")
            
        else:
            print("姓名：", data[1])
            print("年齡：", data[2])
            print("生日：", data[4])

finally:
    db.connect.close()