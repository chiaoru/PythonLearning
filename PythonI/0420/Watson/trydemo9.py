# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 20:50:50 2023

@author: USER
"""



def showList(datalist , num):
    try:
        print(datalist[num])
    except IndexError as e:
        print('超出範圍')
        raise IndexError("請處理索引值超出")
        
data = [10,20,30]


showList(data,1)
showList(data,5)        
print('程式執行完畢')