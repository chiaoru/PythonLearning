# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:50:49 2023

@author: USER
"""

class Account(object):
    bank = 'My Bank'
    
    def __init__(self, number, name, money): # __init__ 初始化
        self.number = number
        self.name = name
        self.__balance = money # 私有化，餘額不能隨意更改
        self.people = 'Bill' # 理專角色
        
    def deposit(self, money):
        self.__balance += money
        self.__showBalance()
        
    def withdraw(self, money):
        if self.__balance >= money: # 當餘額大於提取金額才能進入
            self.__balance -= money
        self.__showBalance() # 呼叫內部方法
        
    def __showBalance(self): # 方法私有化(內部方法，內部呼叫)
        print(self.__balance)
        
    def __str__(self): # 如未寫會印出記憶體位置，__str__可讓其直接印出是誰
        return "戶名：{}，帳號：{}，餘額：{}元".format(self.name, self.number, self.__balance)
        