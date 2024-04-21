# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 21:12:37 2023

@author: USER
"""

from gameRole import Adviser, Tamer

if __name__ == '__main__':
    ad = Adviser('孔明', 600, 1800)
    ta = Tamer('孟獲', 900, 800)
    ad.fight()
    ta.fight()