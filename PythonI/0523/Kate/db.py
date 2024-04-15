# -*- coding: utf-8 -*-
"""
Created on Thu May 18 21:20:15 2023

@author: USER
"""

import mysql.connector

# auth_plugin="mysql_native_password" 版本編碼問題，所以需要加上此句
connect = mysql.connector.connect(host="127.0.0.1", user="root", passwd="123456789", database="web", auth_plugin="mysql_native_password")

cursor = connect.cursor()
