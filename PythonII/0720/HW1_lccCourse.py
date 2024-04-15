# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 21:13:12 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup

url = "https://member.lccnet.com.tw/"

header = {
    
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',

    'cookie': '_gcl_au=1.1.494418226.1689849427; _fbp=fb.2.1689849427349.1870436601; _ga_TDP4KNDS80=GS1.1.1689849428.1.0.1689849428.60.0.0; _ga_QY8DQDPMSR=GS1.1.1689849428.4.0.1689849428.60.0.0; _gid=GA1.3.664890655.1689849428; _ss_pp_id=55ee6d32ab1c83c5e0d1689820628444; _hjSessionUser_1446807=eyJpZCI6IjRjM2VmNjhmLTcxZjktNTY2Yi05YzZiLWEyYTc5NDEzMjY0YyIsImNyZWF0ZWQiOjE2ODk4NDk0Mjg1NTYsImV4aXN0aW5nIjpmYWxzZX0=; _cuid=a1be7173-7062-4022-b367-75655fb96617; _cuserid=; _cusertrait=%7B%7D; _ctrait=%7B%7D; _cgrpid=; _cgrptrait=%7B%7D; script_flag=fd13385c-97e5-4e21-ac73-ac7f33c5bbc8; pid=https://www.lccnet.com.tw/lccnet; _td=6a497fb9-64c2-48b8-9b8b-78d0a5e9091d; _uetsid=63707c7026e911eeb06ebb5bc79ebfa5; _uetvid=6370e25026e911eeb1d173b04f53c620; __RequestVerificationToken=_bUNoWeZFqyr3JpZpOrW_SW3LjsqbIJU6vKlbZbu12PhR7vCwRoIrZK-yMBlmAQ2KzthQEfDC8K2Em_0bEdbvg7aSkDFicoZQD3s9SoEhPY1; _ga=GA1.4.691231131.1689849428; _gid=GA1.4.664890655.1689849428; _ga=GA1.1.691231131.1689849428; adgeek_lccnet_user_id=19-1110523003; _dc_gtm_UA-8399363-4=1; _ga_RV6BDWB9GV=GS1.1.1689858187.1.1.1689858770.0.0.0'
    }


param = {
    'Account': '',
    'Password': '',
    'RememberMe': 'false',
    '__RequestVerificationToken': ''        
    }

session_requests = requests.session() # 建立一個session連線的方法
content = session_requests.post(url, headers=header, data=param).text

url2 = "https://member.lccnet.com.tw/Booking"

lesson = session_requests.get(url2).text

soup = BeautifulSoup(lesson, 'html.parser')

# 聯成登記課程
main = soup.find('ul', class_="courseListWrapper")
allli = main.find_all('li')

for item in allli:
    title = item.find('h4').text
    date = item.find('p').text
    
    classInfo = item.find('div', class_='courseListInfo')
    time = classInfo.find('p').text
    lector = classInfo.find('div', class_='courseListDate').text
    link = "https://member.lccnet.com.tw" + item.find('a').get('href')
    
    print(title)
    print(lector)
    print(date)
    print(time)
    print(link)
    print()
    
    
    
    
