#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
从腾讯较真平台获取谣言数据
@author: lqhou
@file: get_data.py
@time: 2020/02/14
"""
from bs4 import BeautifulSoup
import requests

id_list = []
label_list = []
label_set = set()
for i in range(31):
    url = "https://vp.fact.qq.com/loadmore?artnum=0&page=" + str(i)
    json_data = requests.get(url).json()

    news_list = json_data['content']

    for news in news_list:
        id_list.append(news['id'])
        label_list.append(news['markstyle'])
        label_set.add(news['markstyle'])

# print(label_set)
label_id = {'true': '0', 'fake': '1', 'doubt': '1'}

with open("./get_data/test.tsv", "w") as file:
    for id_item, label in zip(id_list, label_list):
        response = requests.get('https://vp.fact.qq.com/article?id=' + id_item)
        soup = BeautifulSoup(response.text, "html.parser")

        js = str(soup.findAll("script"))
        lens = len(str("originRumor = `"))
        begin = js.find("originRumor = `")
        end = js.find('        (function (win, doc) {')
        data = js[begin+lens:end]
        data = data.strip()
        data = data[:-2]
        file.write(label_id[label] + "\t" + data.replace('\n', '').replace('\r', '') + "\n")



