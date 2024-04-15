# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 20:02:18 2023

@author: USER
"""

class Account:
    def __init__(self, number, acc): # __init__ 初始化
        # 物件變數私有化，只能在這個類別中存取
        self.__number = number # 帳號
        self.__account = acc # 戶名
        self.__balance = 0 # 餘額
    
    def display(self):
        print("帳號:", self.__number)
        print("戶名:", self.__account)
        
    def deposit(self, money):
        if money > 0:
            self.__balance += money
            
            if money >= 100000:
                self.__interest()
        else:
            raise RuntimeError('存錢必須大於零!')
            #print("存錢必須為正!")
    
    def withdraw(self, money):
        if self.__balance >= money:
            self.__balance -= money
        else:
            print("餘額不足!")
            
    def getBalance(self):
        return self.__balance
    
    def __interest(self): # 變數私有化為在變數名稱前加上兩個底線 __Name
        interest = self.__balance * 0.002
        self.__balance += interest
    
    
if __name__ == '__main__':
    myAcc = Account('123-456-789', 'Smart Chen')
    myAcc.__balance = 1 # 動態建立變數，與內部的私有化不同
    # Python 可動態定義變數(動態宣告)
    
    print(myAcc.__balance) # 非class內的 self.__balance, 而是新宣告的 myAcc.__balance
    print(myAcc.getBalance())
    
    myAcc.deposit(1100)
    print(myAcc.getBalance())
    
    myAcc.deposit(100000)
    print(myAcc.getBalance())
    
    
    
    
