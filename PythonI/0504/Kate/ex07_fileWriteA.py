# -*- coding: utf-8 -*-
"""
Created on Thu May  4 20:06:39 2023

@author: USER
"""

from datetime import datetime


data = ['Python', 'Java', '聯成電腦']

def writeLog(errMsg):
    now = datetime.now()
    fileName = now.strftime('%y%m%d') +'.log' # strftime 時間格式化 ，'.log'記錄檔
    
    with open(fileName, 'a', encoding='utf-8') as fobj:
        fobj.write(errMsg +'\n')
        
        
try:
    print(data[0])
    print(data[3])

except Exception as ex:
    #writeLog(ex)
    writeLog(ex.args[0]) # args 中有很多的狀態 args[0] 錯誤狀態顯示
    
    
    
# 時間格式轉換

now = datetime.now()
today = datetime.today()

formdate = now.strftime('%Y-%m-%d') # 字串

# %Y => yyyy; %y => yy; %m => 月; %d => 日; %H => 時; %M => 分; %S => 秒

date2 = now.strftime('%Y%m%d')
date3 = now.strftime('%Y%m%d%H%M%S')
    
    
    

    

    