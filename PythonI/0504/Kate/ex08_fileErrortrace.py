# -*- coding: utf-8 -*-
"""
Created on Thu May  4 20:54:38 2023

@author: USER
"""

from datetime import datetime
import sys
import traceback


data = ['Python', 'Java', '聯成電腦']

def writeLog(errMsg):
    now = datetime.now()
    happenTime = now.strftime('%H:%M:%S')
    fileName = now.strftime('%Y%m%d') +'.log' # strftime 時間格式化 ，'.log'記錄檔
    
    with open(fileName, 'a', encoding='utf-8') as fobj:
        fobj.write(happenTime + ' ' + errMsg +'\n')
        
        
try:
    print(data[0])
    print(data[3])

except Exception as ex:
    msg = ex.args[0]
    cl, exc, tb = sys.exc_info() 
    # 紀錄最新一筆的錯誤訊息
    lastCallStack = traceback.extract_tb(tb)[-1] # -1 最新的一筆
    
    fileName = lastCallStack[0] # 取得發生的檔案名稱
    lineNumber = lastCallStack[1] # 哪一行出問題
    functionName = lastCallStack[2] # 哪一個方法出問題
    error = 'File:{}, Line:{}, Function:{}, Detail:{}'.format(fileName, lineNumber, functionName, msg)
    #print(error)
    
    writeLog(error)