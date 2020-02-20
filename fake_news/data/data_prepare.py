#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: lqhou
@file: data_prepare.py
@time: 2020/02/15
"""

import csv

new_file = open("train.tsv", "w")

with open('weibo_data.csv', 'r') as f:
    reader = csv.reader(f)
    for item in list(reader)[1:]:
        data = item[1]
        label = item[2]

        new_item = label + "\t" + data + "\n"
        new_file.write(new_item)

new_file.close()
