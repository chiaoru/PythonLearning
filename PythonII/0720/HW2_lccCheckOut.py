#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 15:44:47 2023

@author: kate
"""

import requests
from bs4 import BeautifulSoup

url = "https://member.lccnet.com.tw/"

header = {
    
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',

    'cookie': '_gcl_au=1.1.494418226.1689849427; _fbp=fb.2.1689849427349.1870436601; _ga_TDP4KNDS80=GS1.1.1689849428.1.0.1689849428.60.0.0; _ga_QY8DQDPMSR=GS1.1.1689849428.4.0.1689849428.60.0.0; _gid=GA1.3.664890655.1689849428; _ss_pp_id=55ee6d32ab1c83c5e0d1689820628444; _hjSessionUser_1446807=eyJpZCI6IjRjM2VmNjhmLTcxZjktNTY2Yi05YzZiLWEyYTc5NDEzMjY0YyIsImNyZWF0ZWQiOjE2ODk4NDk0Mjg1NTYsImV4aXN0aW5nIjpmYWxzZX0=; _cuid=a1be7173-7062-4022-b367-75655fb96617; _cuserid=; _cusertrait=%7B%7D; _ctrait=%7B%7D; _cgrpid=; _cgrptrait=%7B%7D; script_flag=fd13385c-97e5-4e21-ac73-ac7f33c5bbc8; pid=https://www.lccnet.com.tw/lccnet; _td=6a497fb9-64c2-48b8-9b8b-78d0a5e9091d; _uetsid=63707c7026e911eeb06ebb5bc79ebfa5; _uetvid=6370e25026e911eeb1d173b04f53c620; __RequestVerificationToken=_bUNoWeZFqyr3JpZpOrW_SW3LjsqbIJU6vKlbZbu12PhR7vCwRoIrZK-yMBlmAQ2KzthQEfDC8K2Em_0bEdbvg7aSkDFicoZQD3s9SoEhPY1; _ga=GA1.4.691231131.1689849428; _gid=GA1.4.664890655.1689849428; _ga=GA1.1.691231131.1689849428; adgeek_lccnet_user_id=19-1110523003; _dc_gtm_UA-8399363-4=1; _ga_RV6BDWB9GV=GS1.1.1689858187.1.1.1689858770.0.0.0'
    }


param = {
    'Account': '105546807',
    'Password': 'M221981389',
    'RememberMe': 'false',
    '__RequestVerificationToken': 'Y9xj4pjbz8SGCbbOayx7kbAehtsZ2iloq2Frm22Eh2ywhs_Z9tYk3Ljt2a4udrDvKeavJt7D0hspX7QD2V3RdgnEAG3DfUajByPKx2OSM0s1'        
    }

session_requests = requests.session() # 建立一個session連線的方法
content = session_requests.post(url, headers=header, data=param).text

url2 = "https://member.lccnet.com.tw/ajax-signout/820221018212141/6"

param2 = {
    'MIME類型': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Item填寫簽退.評價分數': '10',
    'Item填寫簽退.Item加強項目s[0].Value': 'false',
    'Item填寫簽退.Item加強項目s[0].Key': 1,
    'Item填寫簽退.Item加強項目s[1].Value': 'false',
    'Item填寫簽退.Item加強項目s[1].Key': 2,
    'Item填寫簽退.Item加強項目s[2].Value': 'false',
    'Item填寫簽退.Item加強項目s[2].Key': 3,
    'Item填寫簽退.Item加強項目s[3].Value': 'false',
    'Item填寫簽退.Item加強項目s[3].Key': '99',
    'Item填寫簽退.Is與我聯絡': 'false'
    }


lesson = session_requests.get(url2, data=param2).text

soup = BeautifulSoup(lesson, 'html.parser')

# 聯成簽退

checkOut = soup.find('ul', id="signoutList")

if checkOut == None:
    print("已完成所有簽退！")


    



