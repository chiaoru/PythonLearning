# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 21:41:15 2023

@author: USER
"""

fruit = {"apple":34,"orange":68,"banana":49}

fruit['orange'] = 168

print(fruit)

del fruit['apple']

print(fruit)


fruit.clear()

print(fruit)