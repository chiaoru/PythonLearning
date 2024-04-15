# -*- coding: utf-8 -*-
"""
Created on Thu May 18 19:55:24 2023

@author: USER
"""

# update 修改
# update 資料表名稱 set 欄位名稱1=欲修改值, 欄位名稱2=修改值 where 條件
# 必須有條件式，否則會全部被更改

import sqlite3

connect = sqlite3.connect("demo.db")

try:
    while True:
        name = input("請輸入欲搜尋姓名的關鍵字，q離開:")
        if name == 'q':
            break
        sql = "select * from students where name like '%{}%'".format(name)
        
        cursor = connect.cursor()
        cursor.execute(sql)
        
        data = cursor.fetchall()
        
        #if data == None:
        if len(data) == 0:
            print("找不到!")
            
        else:
            for row in data:
                print("ID:", row[0])
                print("姓名：", row[1])
                print("年齡：", row[2])
                print("生日：", row[4])
                print()
                
            #q = input("請問是否要修改資料?(y/n)")
            q = input("修改資料=>1 刪除資料=>2 不做任何異動=>n :")
            
            if q == '1':
            
                num = int(input('請輸入欲修改的ID:'))
                age = int(input("請輸入欲修正的年齡:"))
                
                sql = "update students set age={} where id={}".format(age, num)
                
                connect.execute(sql)
                connect.commit()

# delete 刪除
# delete from 資料表 where 條件
# 用過的ID (流水編號、身份證字號、主鍵) 如被刪除後不會再回復，會從新ID編號

            elif q == '2':
                num = input("請輸入欲刪除的ID:")
                sql = "delete from students where id={}".format(num)
                cursor.execute(sql)
                connect.commit()
                
            
finally:
    connect.close()