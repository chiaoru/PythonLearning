# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 19:48:57 2023

@author: USER
"""

import copy

list1 = [1,2,3,4,5]
list2 = [1,[2,3]]

newlist1 = copy.copy(list1)
newlist2 = copy.copy(list2)

list1[1] = 100

print(list1)
print(newlist1)
print()

list2[1][0] = 100
print(list2)
print(newlist2)

print()

newlist3 = copy.deepcopy(list1)
newlist4 = copy.deepcopy(list2)

list2[1][1] = 99

print(list2)
print(newlist4)







