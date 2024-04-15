# -*- coding: utf-8 -*-
"""
Created on Tue May 16 21:10:54 2023

@author: USER
"""

import sqlite3

conn = sqlite3.connect('demo.db')

#sql = "select * from students"

#sql = "select * from students where sex='F'"

#sql = "select * from students where sex='F' and age <= 25"

sql = "select * from students where sex='F' and age >= 20 and age < 25"

cur = conn.cursor() # 資料集物件

cur.execute(sql)

res = cur.fetchall()

for row in res:
    print(row[0])
    print(row[1])
    print(row[2])
    print()






conn.commit()

conn.close()

