# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 21:29:07 2023

@author: USER
"""

content = {'A':'Good','B':'Very Good','O':'Good 2','AB':'It is Good'}

blood = input('pls input Blood:')


blood = blood.upper()

if content.get(blood) == None:
    print("not Blood:",blood)
else:
    print(blood,"is",content[blood])    