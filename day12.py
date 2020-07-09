# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 19:29:50 2020

@author: JU
"""

#標網址：https://www.ettoday.net/news/news-list.htm
#標內容：抓取「ETtoday> 新聞總覽」的新聞類別與標題

import requests
import os
from bs4 import BeautifulSoup
from html.parser import HTMLParser

res = requests.get("https://www.ettoday.net/news/news-list.htm")
soup = BeautifulSoup(res.text, "html.parser")


for d in soup.find(class_="part_list_2").find_all("h3"):
    print(d)
    print(d.find(class_="date").text)
    print(d.find_all("a")[-1].text)