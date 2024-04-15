# -*- coding: utf-8 -*-
"""
Created on Tue May  2 21:01:58 2023

@author: USER
"""

from abc import ABCMeta,abstractmethod

class Person(metaclass=ABCMeta):
    @abstractmethod
    def display(self,name):
        pass
    
    def pay(self):
        self.display(self.name,self.salary)
        

class Clerk(Person):
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def display(self,name,salary):
        print(name,'是Clerk')
        print('薪水：',salary)
        
bill = Clerk('Bill',31000)
bill.pay() 

p = Person()

