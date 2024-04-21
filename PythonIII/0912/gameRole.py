# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:57:28 2023

@author: USER
"""

# 一般每個類別分別存檔，但也可將類似的類別寫在一起，無對錯，只有複雜度，但可能造成效率較差

from Role import Role

# 軍師
class Adviser(Role): # 初始化已由父類別寫完
    # self 物件變數
    def fight(self):
        # 區域變數
        name = super().getName() # super() 子類別調用父類別方法
        # 需要變數 name 承接 有回傳值的 getName()，如無回傳值，可直接寫出
        print(name, '使用搖扇攻擊')
    def cure(self):
        name = super().getName()
        print(name, '大補血')
        
# 訓獸師
class Tamer(Role):
    def fight(self):
        name = super().getName()
        print(name, '使出皮鞭攻擊')
        
    def bite(self):
        name = super().getName()
        print(name, '放出猛獸')
    
    