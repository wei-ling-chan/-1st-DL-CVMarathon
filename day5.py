# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:42:39 2020

@author: JU
"""


#1. 這個 API 一次會回傳幾筆資料？每一筆資料包含哪些欄位？

#2. 取出每一筆資料的「標題」、「貼文時間」、「留言人數」、「按讚人數」

#3. 計算熱門/非熱門文章的「平均留言人數」與「平均按讚人數」



#1. 這個 API 一次會回傳幾筆資料？每一筆資料包含哪些欄位？

import requests,json

r="  https://www.dcard.tw/_api/forums/pet/posts?popular=true"
t = requests.get(r)
response = t.text

data = json.loads(response)

for d in data:
    print(d)
    
#2. 取出每一筆資料的「標題」、「貼文時間」、「留言人數」、「按讚人數」
    
r="  https://www.dcard.tw/_api/forums/pet/posts?popular=true"
t = requests.get(r)
response = t.text

data = json.loads(response)

for d in data:
    print(d["title"],d["createdAt"],d["id"])