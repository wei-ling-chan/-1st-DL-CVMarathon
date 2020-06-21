# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 13:17:36 2020

@author: JU
"""

#Dcard 網址： https://www.dcard.tw/f
import requests

r = requests.get("https://www.dcard.tw/f")
response = r.text
#print(response)
print(type(response))

from bs4 import BeautifulSoup

soup = BeautifulSoup(response,"html5lib")
print(response)
print(type(soup))

#知乎： https://www.zhihu.com/explore
import requests

r = requests.get("https://www.zhihu.com/explore")
response = r.text
print(type(response))

from bs4 import BeautifulSoup

soup = BeautifulSoup(response,"html5lib")
print(response)
print(type(soup))
