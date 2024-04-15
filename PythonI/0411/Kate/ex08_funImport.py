# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:40:10 2023

@author: USER
"""

def hot():
    print("很熱!")
    
def cool(temp):
    print("現在溫度:", temp)
    
print(__name__) # ex08_funImport 印出主程式檔名

if __name__ == '__main__': # 當程式是主程式時才會印出 Ya
    print('Ya')

    