# -*- coding: utf-8 -*-
"""
Created on Tue May 16 20:04:35 2023

@author: USER
"""

import sqlite3

connect = sqlite3.connect('demo.db')

name = input('請輸入姓名:')
age = int(input('請輸入年齡:'))
sex = input('請輸入性別(F/M):')
birthday = input('請輸入生日(yyyy-mm-dd):')

#                           可不照順序(資料表欄位名稱)，只要後面的 values 有對應即可   
sql = "insert into students(sex, birthday, age, name) values('{}','{}','{}','{}')".format(sex, birthday,age,name)

connect.execute(sql)
connect.commit()
connect.close()



