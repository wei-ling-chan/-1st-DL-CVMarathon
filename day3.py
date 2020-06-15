# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 21:59:21 2020

@author: JU
"""
import zipfile
import urllib.request

res ="http://opendata.cwb.gov.tw/govdownload?dataid=F-D0047-093&authorizationkey=rdec-key-123-45678-011121314"

urllib.request.urlretrieve(res, "./data/example.zip")
f = zipfile.ZipFile("./data/example.zip")
f.extractall('./data')

import os,sys

dirs = os.listdir("./data")

for file in dirs:
    print(file)
    
with open("./data/64_72hr_CH.xml", "r",encoding = "UTF-8") as fh:
    fd = fh.read()
print(fd)
 
import xmltodict

# 存取檔案

with open('./sample.xml',encoding = "UTF-8") as fd:
    doc = dict(xmltodict.parse(fd.read()))

# 存取我們的資訊
print(doc['CUPOY']['Title'])

# 用迴圈存取我們的資訊
chapters = doc['CUPOY']['Chapters']['Chapter']
for chapter in chapters:
    print (chapter['@name'], chapter['#text'])



