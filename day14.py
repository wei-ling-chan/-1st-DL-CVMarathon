# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:10:08 2020

@author: JU
"""

import requests
import re
from bs4 import BeautifulSoup

# 先觀察一下目前上映中的電影數量
url = 'https://movies.yahoo.com.tw/movie_intheaters.html'
resp = requests.get(url)
resp.encoding = 'utf-8'

soup = BeautifulSoup(resp.text, 'lxml')
html = soup.find("div", attrs={'class':'release_box'})  # 尋找正在上映中的全部電影筆數，其所在的tag
print("正在上映中總共: ", html.p.string)