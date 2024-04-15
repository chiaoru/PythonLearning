# -*- coding: utf-8 -*-
"""
Created on Thu May  4 18:36:12 2023

@author: USER
"""

# break. continue 與 pass 的差別
for i in range(20):
    if i == 10:
        break # 適用於loop 迴圈，代表整迴圈停止
        print('break')
        
    if i % 4 == 0:
        continue # 適用於loop 迴圈，代表只跳過這一次迴圈
        print('test')
        
    if i == 3:
        pass # 都可以使用，代表當下略過
        print('Ya')
        
    print(i)
    
print('程式執行完畢')

for i in range(20):
    
    if i == 3:
        pass # 3不會被印出，代表略過，開發者必須再回來撰寫程式，目前先放著不處理
    
    else:
        print(i)
        
print('程式執行完畢')