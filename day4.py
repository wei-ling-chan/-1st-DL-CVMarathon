# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 07:32:46 2020

@author: JU
"""

#比較一下範例檔案中的「r.text」與「json.loads(r.text)」讀出來的內容有什麼差異
#自行尋找一個合適的 API 接口做練習，並且查看其回傳內容：
#https://cat-fact.herokuapp.com/facts (來源：https://alexwohlbruck.github.io/cat-facts/)
#http://odata.wra.gov.tw/v4/RealtimeWaterLevel (來源：https://data.gov.tw/dataset/25768)


import requests,json
r = requests.get('http://odata.wra.gov.tw/v4/RealtimeWaterLevel')
b = json.loads(r.text)
print(b)

import requests,json
r = requests.get('https://cat-fact.herokuapp.com/facts')
b = json.loads(r.text)
print(b)