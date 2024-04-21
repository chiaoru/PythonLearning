# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 20:11:24 2023

@author: USER
"""

import MySQLdb

connect = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='123456789', db='mylcc')
cursor = connect.cursor()