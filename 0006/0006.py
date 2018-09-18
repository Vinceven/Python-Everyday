#copyright: https://blog.csdn.net/danation/article/details/76780012

#第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

'''
-*- coding: utf-8 -*-

'''

import os
import re

path='F:/Python/practice/6/'
filelist=os.listdir(path)
list=''
def get_word_frequencies(file_name):
    dic = {}
    txt = open(file_name, 'r').read().splitlines()

    n=0
    for line in txt:
        #print line
        line = re.sub(r'[.?!,""/]', ' ', line)   #要替换的标点符号，英文字符可能出现的
        line = re.sub(r' - ', ' ', line)  
        for word in line.split():

            #当一行的最后一个字符是-的时候，需要跟下一个英文字符串联起来构成单词
            if word[-1] =='-':
                    m=word[:-1]
                    n=1
                    break
            if n==1:
                word=m+word
                n=0
            #print word
            dic.setdefault(word.lower(), 0)  #不区分大小写
            dic[word.lower()] += 1

    return dic

count=5 
for file in filelist: 
    if re.match(file[-4:],'.txt'):         #提出日记目录中非txt文件
        #print file
        filepath=path+file
        print filepath
        dic=get_word_frequencies(filepath) 
        #选出对应value最大的key值，作为重要的词，其中可以通过判断key值字母个数做简单筛选 
        for k in dic:
            if dic[k]>count:
                print k

#print dic