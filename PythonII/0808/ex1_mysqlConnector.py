# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 18:45:40 2023

@author: USER
"""

import mysql.connector

connect = mysql.connector.connect(host='localhost', user='root', passwd='123456789', database='myweb', auth_plugin='mysql_native_password')

cursor = connect.cursor()