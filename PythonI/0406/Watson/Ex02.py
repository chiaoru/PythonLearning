# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 19:39:32 2023

@author: USER
"""

member = {"Mary":30000,"Bill":1000000,'David':0}


keys = member.keys()

values = member.values()

items = member.items()

print(keys)
print(values)
print(items)

listk = list(keys)
listv = list(values)
listi = list(items)

print(listk)
print(listv)
print(listi)

print(min(listv))
print(max(listv))

print()

for it in listi:
    print(it)
    print(it[0],it[1])
    
print()

for k,v in listi:
    print(k,v)    








