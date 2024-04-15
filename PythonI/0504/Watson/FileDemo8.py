# -*- coding: utf-8 -*-
"""
Created on Thu May  4 21:38:01 2023

@author: USER
"""

import os

myDir = 'c:\lcc'

if os.path.exists(myDir):
    os.rmdir(myDir)
    print('此資料夾已刪除')
else:
    os.mkdir(myDir)
    
    