# -*- coding: utf-8 -*-
"""
Created on Thu May  4 20:16:01 2023

@author: USER
"""

from datetime import datetime

now = datetime.today()

print(now)

now = datetime.now()

print(now)

#%Y => yyyy   %y = > yy
#%m => 月  %d  => 日
# %H => 時  %M =>分   %S => 秒

formdate = now.strftime('%Y-%m-%d')

print(formdate)

date2 = now.strftime('%Y%m%d%H%M%S')

print(date2)
