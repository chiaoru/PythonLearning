# -*- coding: utf-8 -*-
"""
Created on Tue May  9 19:29:27 2023

@author: USER
"""

import requests

url = 'https://kprofiles.com/wp-content/uploads/2021/11/EuL8ZU5VoAEJaYi-600x800.jpg'

data = requests.get(url, stream=True)

with open('lcc.jpg', 'wb') as f:
    for block in data.iter_content(1024):
        if not block:
            break       
        f.write(block)
        
        