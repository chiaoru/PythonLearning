# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:07:25 2023

@author: USER
"""

fn = 'file02.txt'

fobj = open(fn,encoding='utf-8')

data = fobj.read()

fobj.close()

print(data)





