#copyright: https://www.jianshu.com/p/28a47baef3bc

#第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

#第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

# -*- coding: utf-8 -*-
import re

def get_filters(path):
    if path is None:
        return
    filters = []
    with open(path, encoding="utf-8") as f:
        for line in f.readlines():
            if "\n" in line:
                filters.append(line[:-1])
            else:
                filters.append(line)
    return filters


def main_0011():
    filters = get_filters(r"D:\self\Python\codes\Python everyday\0011&0012\filtered_words.txt")
    while 1:
        tmp = input("plz input: ")
        if tmp == "0":
            print("Exit")
            break
        else:
            if tmp in filters:
            	print("Freedom")
            else: 
            	print("Human Rights")

def main_0012():
    filters = get_filters(r"D:\self\Python\codes\Python everyday\0011&0012\filtered_words.txt")
    while 1:
        tmp = input("plz input:")
        if tmp == "0":
            print("Exit")
            break
        for filter_word in filters: 
           new_str = "" 
           if filter_word in tmp:
                if len(re.findall(u"[\u4e00-\u9fa5]+", filter_word)) > 0:
                    len_new_str = len(filter_word)
                else:
                    len_new_str = 1

                for i in range(len_new_str): 
                   new_str += "*"
                tmp = str(tmp).replace(filter_word, new_str)

        print(tmp)

if __name__ == "__main__":
    main_0011()
    #main_0012()


