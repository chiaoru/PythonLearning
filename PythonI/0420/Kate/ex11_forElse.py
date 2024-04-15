#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:11:25 2023

@author: kate
"""

for i in range(2, 101):
    for x in range(2, i):
        if i % x == 0:
            break 
    
    else:
        print(i, "是質數")