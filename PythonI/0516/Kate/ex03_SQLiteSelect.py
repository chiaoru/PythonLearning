# -*- coding: utf-8 -*-
"""
Created on Tue May 16 20:45:47 2023

@author: USER
"""

# 查詢資料

import sqlite3

connect = sqlite3.connect('demo.db')

# 查詢所有欄位，當資料量大時，顯示所有欄位效能會很差
sql = "select * from students"

# 執行結果，資料庫抓出的資料是元祖(不可更改)
result = connect.execute(sql)

# 將結果轉換成串列並印出
#print(list(result))

# 將結果用迴圈印出
for row in result:
    print("姓名:", row[1])
    print("性別:", row[3])
    print("生日:", row[4])
    print()

# 當更改速度或不更改資料時，可不做commit(),但如資料持續更新時，建議寫，雖然較慢，但確保資料同步
connect.commit()
connect.close()
