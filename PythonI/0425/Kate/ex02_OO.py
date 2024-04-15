# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 19:14:26 2023

@author: USER
"""

class Account:
    def __init__(self, number, acc): # __init__ 初始化
        self.number = number # 帳號
        self.account = acc # 戶名
        self.balance = 0 # 餘額
    
    def display(self):
        print("帳號:", self.number)
        print("戶名:", self.account)
        
    def deposit(self, money):
        if money > 0:
            self.balance += money
        else:
            raise RuntimeError('存錢必須大於零!')
            #print("存錢必須為正!")
    
    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money
        else:
            print("餘額不足!")
            
if __name__ == '__main__': # 如果是主程式才跑, __main__ 主要執行程式
    myAcc = Account('123-456-789', 'Bill')
    myAcc.display()
    print('餘額:', myAcc.balance)
    
    money = int(input('請輸入存款金額:'))
    if money <= 0:
        print('無法存錢!')
    else:
        myAcc.deposit(money)
    
    myAcc.deposit(10000)
    print('餘額:', myAcc.balance)
    
    
    money = int(input('請輸入體領金額:'))
    if money >= myAcc.balance:
        print('餘額不足!')
    else:
        myAcc.withdraw(money)
    
    myAcc.withdraw(1)
    print('餘額:', myAcc.balance)

        