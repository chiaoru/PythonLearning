# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 21:17:58 2023

@author: USER
"""

class myBirth:
    def __init__(self, name, y, m, d):
        self.name = name
        self.year = y
        self.month = m
        self.day = d
    
    # 重新定義方法(給使用者看的): 本來就有，但為了使用者需求而重新改寫
    def __str__(self):
        print(self.name, 'Hello!')
        # 定義輸出格式，字串只能加字串
        return '生日:' + str(self.year) + '年' + str(self.month) + '月' + str(self.day) + '日'
    
    # 給開發者看的,在console 中系統可做反饋，如 打入變數 birth 時，會出現 1999年9月21日
    def __repr__(self):
        return '{}年{}月{}日'.format(self.year, self.month, self.day)
    
birth = myBirth('Bill', 1999,9,21)
print(birth)

print(repr(birth))