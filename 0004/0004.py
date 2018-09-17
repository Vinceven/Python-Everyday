#第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。

# -*- coding: utf-8 -*-

'''
Created on Sat Sep 17 2018

@author: Vince
'''

import os


file = open('d:\\user\\01378049\\desktop\\wz.txt',mode='r',encoding = 'utf-8')

dict = {}

for line in file:
    h_line = line.split()
    for key in h_line:
        if (key.lower() not in dict) and ((key[-1]>='a' and key[-1] <='z') or (key[-1]>='A' and key[-1] <= 'Z')):
            dict[key.lower()]=1
        elif (key[-1]>='a' and key[-1] <='z') or (key[-1]>='A' and key[-1] <= 'Z'):
            dict[key.lower()]+=1
count = 0
for key,value in dict.items():
    count += value
print(count)
print(dict)
