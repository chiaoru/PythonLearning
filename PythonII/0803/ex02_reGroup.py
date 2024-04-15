# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:06:52 2023

@author: USER
"""

import re

text = "123大家好abc456ABC"

search = re.search("([0-9]*)大家好([a-z]*)([0-9]*)", text)

print(search.group())
print(search.group(0))
print(search.group(1))
print(search.group(2))
print(search.group(3))

print(search.groups())

