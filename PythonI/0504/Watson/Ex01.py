# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

for i in range(20):
    if i == 10:
        break  # 立即離開
        print("break")
    
    if i % 4 == 0:
        continue  # 放棄一次。下面皆不執行
        print("test")
    
    if i == 3 :
        pass
        print("Ya")
    
    print(i)
    
print('程式執行完畢')    