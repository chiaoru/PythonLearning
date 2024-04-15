# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 20:59:37 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup

# HW 將各種彩卷的彩號抓下來
url = 'https://www.taiwanlottery.com.tw/index_new.aspx'

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15'
    }

data = requests.get(url, headers=header).text

soup = BeautifulSoup(data, 'html.parser')


for i in range(1, 8):
    
    if i == 1:
        print("Bingo Bingo")
        class1 ='contents_box01'
        class2 ='ball_tx ball_yellow'
    
    elif i == 2:
        print("雙贏彩")
        class1 ='contents_box06'
        class2 ='ball_tx ball_blue'
 
    elif i == 3:
        print('威力彩 & 38樂合彩' )
        class1 ='contents_box02'
        class2 ='ball_tx ball_green'    
        
    elif i == 4:
        print('大樂透 & 49樂合彩' )
        class1 ='contents_box02'
        class2 ='ball_tx ball_yellow'
        class3 ='contents_mine_tx02'
        
    elif i == 5:
        print('今彩539 ＆ 39樂合彩')
        class1 ='contents_box03'
        class2 ='ball_tx ball_lemon'
    
    elif i == 6:
        print('三星彩')
        class1 ='contents_box04'
        class2 ='ball_tx ball_purple'
    
    elif i == 7:
        print('四星彩')
        class1 ='contents_box04'
        class2 ='ball_tx ball_purple'
        
    data = soup.find('div', class_=class1)
    date = data.find('span').text
    numbers = data.find_all('div',class_=class2)

    if i == 1:
        print(date)
        print("獎號：", end="")
        for number in numbers:
            number = number.text
            print(number, end=" ")
            
        print() 
        print("超級獎號：", data.find('div', class_="ball_red").text)
        print("猜大小：", data.find('div', class_="ball_blue_BB1").text)
        print("猜單雙：", data.find('div', class_="ball_blue_BB2").text)
        print()
        
    elif i == 3:
        number = list()
        for i in numbers:
            i = i.text
            number.append(i)
            
        size = int(len(number)/2)
        
        print(date)
        print("獎號：")
        print("  開出順序：", number[0:size])
        print("  大小順序：", number[size::])  
        print("威力彩第二區：", data.find('div', class_="ball_red").text)
        print()
        print('-'*50)
        
    elif i == 4:
        data = soup.find_all('div', class_=class1)
        date = data[2].find('span', class_='font_black15').text
        numbers = data[2].find_all('div', class_=class2)
        
        number = list()
        for i in numbers:
            i = i.text
            number.append(i)
                    
        size = int(len(number)/2)
                
        print(date)
        print("獎號：")
        print("  開出順序：", number[0:size])
        print("  大小順序：", number[size::]) 
        print("大樂透特別號：", data[2].find('div', class_="ball_red").text)
        print()
        print('-'*50)
        
    elif i == 6:
        data = soup.find_all('div', class_=class1)
        date = data[0].find('span').text
        numbers = data[0].find_all('div',class_=class2)
        
        number = list()
        for i in numbers:
            i = i.text
            number.append(i)
                    
    
        print(date)
        print("中獎號碼：", number)
        print()
        print('-'*50)
        
        
    elif i == 7:
        data = soup.find_all('div', class_=class1)
        date = data[1].find('span').text
        numbers = data[1].find_all('div',class_=class2)
        
        number = list()
        for i in numbers:
            i = i.text
            number.append(i)
            
        print(date)
        print("中獎號碼：", number)
        print()
        print('-'*50)
        
        
    else:  
        number = list()
        for i in numbers:
            i = i.text
            number.append(i)
            
        size = int(len(number)/2)
        
        print(date)
        print("獎號：")
        print("  開出順序：", number[0:size])
        print("  大小順序：", number[size::])      
        print()
        print('-'*50)



