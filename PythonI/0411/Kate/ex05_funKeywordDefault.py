# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 20:10:17 2023

@author: USER
"""

# 關鍵字函式


def city(area, name):
    print("居住區域:", area)
    print("姓名:", name)

city("中區", "Peter")
city(name="David", area="東區") # 關鍵字引數

#city(name="Mary","西屯區") 因為 "西屯區" 未指定關鍵字引數，且不符合位置指定填寫，所以會出錯
city("西屯區", name="Mary")
print()

# 預設值引數
# 函式中若有預設值引數時，你的位置引數必須在預設值引數之前，不可以在後。
# 
def students(name, sex, school= "聯成", age=19): # name, sex為位置引數，school為預設值引數
    print("姓名:", name)
    print("性別:", sex)
    print("學校:", school)
    print("年齡:", age)
    
students("David", "Male") # 當未給予值時，已預設值取代
students("Mary", "Female", "台中女中", 16)
students("John", "Male", age=14) # 當有兩個以上預設值引數時，可用關鍵字引數來取代預設值