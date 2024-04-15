# -*- coding: utf-8 -*-
"""
Created on Tue May  9 18:50:48 2023

@author: USER
"""

import os # 與作業系統有關的函式庫

print(os.getcwd()) # 抓取目前的工作目錄

# 判斷檔案或資料夾是否存在
print('檔案 lcc.txt 是否存在:', os.path.exists('lcc.txt'))
print('資料夾 good 是存在:', os.path.exists('good'))

#判斷是否為檔案或資料夾
print('是檔案?', os.path.isfile('lcc.txt'))
print('good 是檔案?', os.path.isfile(('good')))
print('good 是資料夾?', os.path.isdir('good'))

# 將目錄中的東西抓出來
for item in os.listdir('C:\\lcc\\good'):
    print(item)
    
# 將字串組合成一個路徑，也可以用寫入的方式成立新檔案
print(os.path.join('c:\\lcc', 'good','lcc.txt')) # join 將裡面的值變成一個路徑

files = ['file1.txt', 'img1.jpg', 'hello.exe']
for f in files:
    name = os.path.join('C:\\lcc', f)
    print(name)
    
# 將圖片存檔 (byte 位元組)

