# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 22:03:10 2020

@author: JU
"""

#取出知乎問題發問時間
#取出第一筆與最後一筆回答的時間



import requests,json

headers = {"user-agent": "my-app/0.0.1"}
r = requests.get('https://www.zhihu.com/api/v4/questions/55493026/answers', headers = headers)

response = r.text

data = json.loads(response)

for d in data["data"]:
    print(d["question"][ 'created'],d["question"]['updated_time'])

