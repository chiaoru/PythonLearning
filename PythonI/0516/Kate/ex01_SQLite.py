# -*- coding: utf-8 -*-
"""
Created on Tue May 16 18:56:42 2023

@author: USER
"""

import sqlite3

# 資料庫物件
connect = sqlite3.connect('demo.db') # db database

#       建立   資料表 資料表名稱 欄位   整數      主鍵      自動增值      欄位   文字(大小)  欄位 整數 欄位 文字(大小)  欄位       文字(大小)  
#sql = "create table students(id integer primary key autoincrement, name varchar(30), age int, sex varchar(2), birthday varchar(10))"

# 如不存在就建立 if not exists
sql = "create table if not exists students(id integer primary key autoincrement, name varchar(30), age int, sex varchar(2), birthday varchar(10))"

# 執行
connect.execute(sql)
#立即生效(跟資料庫說同步執行)，否則只會再暫存區
connect.commit()
# 關閉
connect.close()
