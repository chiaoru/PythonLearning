# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 19:46:37 2023

@author: USER
"""

class Account:
    #初始化
    def __init__(self,number,acc):
        
        # 物件變數私有化  ，只能在這個類別裡面存取
        self.__number = number
        self.__account = acc
        self.__balance = 0
        
    def display(self):
        print('帳號：',self.__number)
        print('戶名：',self.__account)

    def deposit(self,money):
        if money > 0 :
            self.__balance += money
            if money >= 100000:
                self.__interest()
        else:
            raise RuntimeError('存錢必須大於0')
            #print('存錢必須大於0')
            
    def withDraw(self,money):
        if self.__balance >= money:
            self.__balance -= money
            
    def  getBalance(self):
        return self.__balance
    
    
    #私有化方法
    def __interest(self):
        interest = self.__balance * 0.002
        self.__balance += interest
        
        
            
if __name__ == '__main__':
    myAcc = Account('123-456-789','陳聰明')  
    myAcc.__balance = 1  # 動態建立變數，與內部的私有化不同
    
    print(myAcc.getBalance())
    
    myAcc.deposit(1100)
    print(myAcc.getBalance())
    myAcc.deposit(100000)
    print(myAcc.getBalance())
    
 

            
            