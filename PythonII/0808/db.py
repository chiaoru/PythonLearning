# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 18:45:40 2023

@author: USER
"""

import mysql.connector

connect = mysql.connector.connect(host='127.0.0.1', user='root', passwd='Chiao0923', database='myweb', auth_plugin='mysql_native_password', buffered=True)

# 資料集 dataset
cursor = connect.cursor()


# if show Error Unread result found, add buffered=True in connect