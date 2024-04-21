# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 21:09:33 2023

@author: USER
"""

"""
 查詢所有欄位資料
 sql 語法: select * from product
 Django 語法: Goods.objects.all()

 查詢價格等於1000
 sql 語法: select * from product where price=1000
 Django 語法: Goods.objects.filter(price=1000)
             Goods.objects.get(price=1000) 只抓一筆，且一定要有資料，否則Error

 查詢價格大於1000
 sql 語法: select * from product where price>1000;
 Django 語法: Goods.objects.filter(price__gt=1000)  # gt: greater than

 查詢價格大於等於1000
 sql 語法: select * from product where price>=1000;
 Django 語法: Goods.objects.filter(price__gte=1000)  # gte: greater than equal

 查詢價格小於1000
 sql 語法: select * from product where price<1000;
 Django 語法: Goods.objects.filter(price__lt=1000)  # lt: less than

 查詢價格小於等於1000
 sql 語法: select * from product where price<=1000;
 Django 語法: Goods.objects.filter(price__lte=1000)  # lte: less than equal
 
 查詢價格大於1000 且 小於 3000
 sql 語法: select * from product where price>1000 and price <3000;
 Django 語法: Goods.objects.filter(price__gt=1000, price__lt=3000)
 
 查詢價格大於等於1000 且 小於等於 3000
 sql 語法: select * from product where price>=1000 and price <=3000;
          select * from product where price between 1000 and 3000;
 Django 語法: Goods.objects.filter(price__gte=1000, price__lte=3000)
 
 查詢name中有apple的產品
 sql 語法: select * from product where name like '%apple%';
 Django 語法: Goods.objects.filter(name__icontains='apple')
 
 查詢價格等於1000,2000,3000
 sql 語法: select * from product where price in(1000,2000,3000);
 Django 語法: Goods.objects.filter(price__in=[1000,2000,3000])  
 
 顯示5筆資料
 sql 語法: select * from product limit 5;
 MS-sql 語法: select top 5 * from product;
 Django 語法: Goods.objects.all()[:5] # 切片
 
 查詢name中有iphone 15的產品，並顯示10筆資料，且價格由大到小排列
 sql 語法: select * from product where name like '%iphone15%' limit 10;
 Django 語法: Goods.objects.filter(name__icontains='iphone15').order_by('-price')[:10]  
 
 查詢空值
 sql 語法: select * from product where price is null;
 Django 語法: Goods.objects.filter(price__isnull=True)
 
"""




