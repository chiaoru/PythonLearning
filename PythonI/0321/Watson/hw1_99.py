# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:20:25 2023

@author: USER
"""

for a in range(2,10):
    for b in range(2,10):
        print(b, "*", a, "=", a*b, sep="", end="\t")
    print()