# -*- coding: utf-8 -*-
"""
Created on Tue May 16 21:11:18 2023

@author: USER
"""

# 查詢資料，方式二(推薦)

import sqlite3

connect = sqlite3.connect('demo.db')

# 查詢所有欄位，當資料量大時，顯示所有欄位效能會很差
#sql = "select * from students"

# 條件式查詢 where
#sql = "select * from students where sex='F'"
#sql = "select * from students where sex='F' and age <= 25"
#sql = "select * from students where sex='F' and age >=20 and age < 25"
sql = "select * from students where sex='F' and age between 20 and 25" # between 介於 (大於等於與小於等於) 用於日期或整數 => 25 >= age >= 20

# 產生一個查詢物件
cursor = connect.cursor()
cursor.execute(sql)

# 抓取查詢結果
result = cursor.fetchall() # 二維
#result = cursor.fetchone() # 一維，當資料只有一筆時，例帳號密碼

for row in result:
    print("姓名:", row[1])
    print("年齡:", row[2])
    print("生日:", row[4])
    print()

#print(list(result))

connect.commit()
connect.close()