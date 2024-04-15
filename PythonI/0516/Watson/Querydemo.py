# -*- coding: utf-8 -*-
"""
Created on Tue May 16 20:30:54 2023

@author: USER
"""

import sqlite3

conn = sqlite3.connect('demo.db')

sql = "select * from students"

result = conn.execute(sql)


for row in result:
    print(row[1])
    print(row[4])
    print()



conn.commit()

conn.close()

