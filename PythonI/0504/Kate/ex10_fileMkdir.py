# -*- coding: utf-8 -*-
"""
Created on Thu May  4 21:38:46 2023

@author: USER
"""

import  os

# 我的資料夾
myDir = 'lcc'
#myDir = 'C:\lcc' # 指定路徑

if os.path.exists(myDir):
    os.rmdir(myDir)
    print('已刪除')
    #print('已存在')
    
else:
    os.mkdir(myDir)