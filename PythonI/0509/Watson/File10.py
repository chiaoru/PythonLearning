# -*- coding: utf-8 -*-
"""
Created on Tue May  9 18:50:48 2023

@author: USER
"""
import os


print(os.getcwd()) # 抓取目前的工作目錄

print('檔案lcc.txt 是否存在？',os.path.exists('lcc.txt'))
print('資料夾good 是否存在？',os.path.exists('good'))


print('lcc.txt是檔案嗎？',os.path.isfile('lcc.txt'))
print('good是檔案嗎？',os.path.isfile('good'))

print('good是目錄嗎？',os.path.isdir('good'))

for item in os.listdir('c:\\lcc\\good'):
    print(item)
    
    
print(os.path.join('c:\\cc','good','lcc.txt')) 

files = ['file1.txt','image.jpg','hello.exe']   

for f in files:
    name = os.path.join('c:\\lcc',f)
    print(name)








