# -*- coding: utf-8 -*-
"""
Created on Tue May  2 21:02:40 2023

@author: USER
"""

from abc import ABCMeta, abstractmethod 

class Person(metaclass=ABCMeta):
    @abstractmethod # 未完成的方法，即抽象類別，不可生成
    def display(self, name):
        pass
    
    def pay(self):
        self.display(self.name, self.salary)
        
    # 當子類別繼承抽象類別時，必須先完成方法，否則依然無法生成(用程式規範子類別)
        
class Clerk(Person): # clerk 醫生
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self, name, salary):
        print(name, '是Clerk')
        print('薪水:', salary)        
        
bill = Clerk('Bill', 32000)

bill.pay() # Clerk.name -> Bill => Person.pay(bill) => Clerk.display(bill, 'Bill', 32000)

#p = Person() # error，因為是未完成方法，所以不能生成使用