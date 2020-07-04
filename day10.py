# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 15:30:46 2020

@author: JU
"""

#requests + BeautifulSoup

import requests
from bs4 import BeautifulSoup

resp = requests.get('https://google.com')
x = BeautifulSoup(resp.text)
print(x)


#Grap+PyQuery

from grab import Grab
from pyquery import PyQuery as pq 
g = Grab()
resp = g.go('https://google.com')
resp.body
 
doc = pq(resp.body)
title = doc("title")
print(type(title), title.text)
