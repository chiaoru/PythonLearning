# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:30:35 2023

@author: USER
"""

from bank.Account import Account # bank.Account 當下資料夾中的bank資料夾的Account檔案

if __name__ == '__main__':
    ac = Account('123-456-789', 'Allen Chen', 1000)
    ac2 = Account('987-654-321', 'Jane Lin', 5000)
    
    print(ac)
    print(ac2)
    
    ac.deposit(2000) # 會印出餘額
    
    print(ac.bank)
    print(ac2.bank)
    
    Account.bank = "Handsome Bank" #更改類別(修改物件內的bank)
    # 物件內所有相關的同時被更改
    print(ac.bank) 
    print(ac2.bank)
    
    print('物件自動生成變數')
    # 依照自己的需求可自訂變數，只能自己使用(only for python)
    ac2.creditCard = '白帥帥無限卡'
    ac2.creditCardSecretary = '白金秘書'
    ac2.bank = 'OK Bank' # 與前面的類別變數不同，是為物件變數(賦予ac2的bank值)，先以自己的為主
    
    print(ac2.creditCard)
    print(ac2.creditCardSecretary)
    print(ac2.bank)
    print(ac.bank)