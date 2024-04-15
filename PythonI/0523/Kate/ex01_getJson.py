# -*- coding: utf-8 -*-
"""
Created on Tue May 23 18:33:52 2023

@author: USER
"""

import db
import json
import requests

url = "https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?size=1000"

data = requests.get(url).text

bike = json.loads(data)

#print(bike) --> 串列

for item in bike:
    # 找是否有存在於資料表中，有就修改，沒有就新增
    station = item['sna']
    sql = "select * from ntpbike where station = '{}'".format(station)
    
    db.cursor.execute(sql)
    
    row = db.cursor.fetchone()

    
    if row == None: # 表示找不到
        sql = "insert into ntpbike(station, tot, rent, space, area, address, lat, lng) values('{}', '{}', '{}', '{}', '{}', '{}', '{}','{}')".format(item['sna'],item['tot'],item['sbi'],item['bemp'],item['sarea'],item['ar'],item['lat'],item['lng'])
        db.cursor.execute(sql)
        db.connect.commit()

    else:
        #sql = "update ntpbike set rent={}, space={} where id={}".format(item['sbi'],item['bemp'],row[0])
        sql = "update ntpbike set rent='{}', space='{}' where station='{}'".format(item['sbi'],item['bemp'],item['sna'])
        
        db.cursor.execute(sql)
        db.connect.commit()
        
db.connect.close()