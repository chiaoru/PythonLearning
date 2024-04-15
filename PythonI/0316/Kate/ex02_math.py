# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 20:01:14 2023

@author: USER
"""

# 算術運算子
a = 5
b = 2
c = a + b

print(c)
print(a-b)
print(a*b)
print(a/b) #出來是浮點數
print(a//b) #取商數，只取整數
print(a%b) #取餘數

print() # 印出空白行

# 比較運算子
'''
>  大於
>= 大於等於 
<  小於
<= 小於等於
== 等於
not  相反
!= 不等於

True 成立
False 不成立
    只有 Python 的 T/F 是大寫
'''

a = 5
b = 10
print(a > b) # False
print(a*2 >= b) # True
print(a < b) # True
print(a*2 == b) # True
print(a != b) # True

print()

# 邏輯運算子
'''
and 左右邊的條件都必須成立 
or  左邊或右邊的條件成立即成立

'''

print(a < b and a*2 == b)
print(a > b and a*2 == b)
print(a > b or a*2 == b)
print(not(a > b ))

print()

#指定運算子

a = 2
b = 3
a = a + b # a+b 後指派給 a
b += 2 # b = b+2，因為變數b相同，所以可以省略
print(a)
print(b)

a -= 3 #減法指定，5-3=2
print(a)

a *= b #乘法指定，2*5=10
print(a)

a /= b #除法指定，10/5=2
print(a)



