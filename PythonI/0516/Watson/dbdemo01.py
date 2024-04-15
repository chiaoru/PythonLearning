# -*- coding: utf-8 -*-
"""
Created on Tue May 16 19:13:14 2023

@author: USER
"""

import sqlite3

# 資料庫物件
conn = sqlite3.connect('demo.db')


sql = "create table if not exists students(id integer primary key autoincrement , name varhcar(30),age int,sex varchar(2),birthday varchar(10) ) "

# 執行
conn.execute(sql)

# 立即生效
conn.commit()

# 關閉資料庫
conn.close()