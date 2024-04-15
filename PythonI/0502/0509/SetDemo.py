# -*- coding: utf-8 -*-
"""
Created on Tue May  9 21:08:08 2023

@author: USER
"""

import random

#hashset 雜湊  ，略過重復項
data = set()

while len(data) < 6:
    data.add(random.randint(1,49))
    
    
print(list(data))    