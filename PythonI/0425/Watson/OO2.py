# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 19:14:18 2023

@author: USER
"""

class Account:
    #初始化
    def __init__(self,number,acc):
        self.number = number
        self.account = acc
        self.balance = 0
        
    def display(self):
        print('帳號：',self.number)
        print('戶名：',self.account)

    def deposit(self,money):
        if money > 0 :
            self.balance += money
        else:
            raise RuntimeError('存錢必須大於0')
            #print('存錢必須大於0')
            
    def withDraw(self,money):
        if self.balance >= money:
            self.balance -= money
            
            
           
if __name__ == '__main__':            
    myAcc = Account('123-456-789','陳大大')
    
    myAcc.display()
    print('餘額：',myAcc.balance)
    
    money = int(input('請輸入存錢的金額：'))
    if money <= 0 :
        print('無法存錢')
    else:
        myAcc.deposit(money)
        
    
        
    print('餘額：',myAcc.balance)
    myAcc.withDraw(1)
    print('餘額：',myAcc.balance)





            
            
        

        