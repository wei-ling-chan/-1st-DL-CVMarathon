# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 22:52:24 2020

@author: JU
"""

#取出班次一的每一個時間
#將班次一的每一個時間用一種資料型
#將班次一到五與其所有時間用一種資料型態個別保存

#下載檔案
import csv

# 開啟 CSV 檔案
with open('./data/example.csv', newline='',encoding="utf-8") as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈輸出每一列
    for row in rows :
        #取出班次一的每一個時間
        print(row[5])
    
