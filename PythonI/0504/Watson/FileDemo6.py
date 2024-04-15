# -*- coding: utf-8 -*-
"""
Created on Thu May  4 20:24:58 2023

@author: USER
"""

from datetime import datetime
import sys
import traceback


data = ['Python','Java','LCCNET']


def writeLog(errMsg):
    now = datetime.now()
    happen = now.strftime('%H:%M:%S')
    fileName = now.strftime('%Y%m%d') + ".log"
    with open(fileName,'a',encoding='utf-8') as fObj:
        fObj.write(happen +" "+errMsg + '\n')
    


try:
    print(data[0])
    print(data[5])
    
except Exception as ex:
    
    msg = ex.args[0]
    cl,exc,tb = sys.exc_info()
    

    
    
    
    lastCallStack = traceback.extract_tb(tb)[-1]
    
    fileName = lastCallStack[0]
    linenum =  lastCallStack[1]
    funName =  lastCallStack[2]
    

    
    error = 'File:{},line:{},Fun:{},detail:{}'.format(fileName,linenum,funName,msg)
    
    
    
    
    
    writeLog(error)



    