# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 18:49:07 2023

@author: USER
"""
# 高雄市公車xml

import requests
import io
import xml.sax

busId = list()
busRoute = list()
busStart = list()
busEnd = list()

busGo = list()
busBack = list()

lateGo = list()
lateBack = list()

class KBusHandler(xml.sax.ContentHandler):
    def startElement(self,tag,attr):
        if tag == "Route":
            busId.append(attr['ID'])
            busRoute.append(attr['nameZh'])
            busStart.append(attr['departureZh'])
            busEnd.append(attr['destinationZh'])
# https://ibus.tbkc.gov.tw/xmlbus/StaticData/GetRoute.xml
            
class KBusStop(xml.sax.ContentHandler):
    def startElement(self, tag, attr):
        if tag == "Stop":
            #print("站牌：", attr['nameZh'])
            
            if attr['GoBack'] == '1':
                busGo.append(attr['nameZh'])
                
            else:
                busBack.append(attr['nameZh'])
            
# https://ibus.tbkc.gov.tw/xmlbus/StaticData/GetStop.xml?routeIds=16

class lateStop(xml.sax.ContentHandler):
    def startElement(self, tag, attr):
        if tag == "BusData":
            if attr['GoBack'] == '1':
                lateGo.append(attr['BusID'])
                
            else:
                lateBack.append(attr['BusID']) 

if __name__ == "__main__":
    parser = xml.sax.make_parser() # 建立一個解析器
    bus = KBusHandler()
    parser.setContentHandler(bus)
    
    url = "https://ibus.tbkc.gov.tw/xmlbus/StaticData/GetRoute.xml"
    data = requests.get(url)
    data.encoding = 'utf-8'
    data = data.text
    
    busObject = io.StringIO(data)
    parser.parse(busObject)
    
    #print(busRoute)
    
# 輸入欲查詢路線
    print('路線：', busId)
    busid = input("請輸入欲查詢的公車路線：")
    if busId.count(busid) > 0: # 當有資料才進來
        index = busId.index(busid) # 索引值一定要有值
        print(busId[index])
        print(busRoute[index])
        print(busStart[index])
        print(busEnd[index])
        
    routeUrl = "https://ibus.tbkc.gov.tw/xmlbus/StaticData/GetStop.xml"
    param = dict() # 參數
    param['routeIds'] = busid
    result = requests.get(routeUrl, params=param)
    result.ecoding = 'utf-8'
    result = result.text
    
    stop = KBusStop()
    parser.setContentHandler(stop)
    stopObject = io.StringIO(result) # 立即解析
    parser.parse(stopObject)
    
# HW1 顯示去與回的站牌
# 提示：可宣告二個串列，一個紀錄去、一個紀錄回
    print("去程站牌：", busGo)
    print()
    print("回程站牌：", busBack)
    
    print()

# HW2 顯示公車位置：去的公車車牌有哪些、回的公車車牌有哪些
    lateUrl = "https://ibus.tbkc.gov.tw/xmlbus/GetBusData.xml"
    param = dict() # 參數
    param['routeids'] = busid
    result = requests.get(lateUrl, params=param)
    result.ecoding = 'utf-8'
    result = result.text
    
    late = lateStop()
    parser.setContentHandler(late)
    lateObject = io.StringIO(result)
    parser.parse(lateObject)
    
    print("目前去程公車有：", lateGo)
    print()
    print("目前回程公車有：", lateBack)
    
    
    
    
    
