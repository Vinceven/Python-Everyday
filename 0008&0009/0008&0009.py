#copyright: https://blog.csdn.net/qq_35614920/article/details/76746902

#第 0008 & 0009 题： 一个HTML文件，找出里面的正文&链接。

# coding=utf-8

from bs4 import BeautifulSoup
def sechBodyUrl(path):
    with open(path,encoding='utf-8') as fp:
        text = BeautifulSoup(fp, 'lxml')
        urls = text.findAll('a')
        for u in urls:
            print(u['href'])
        content = text.get_text().strip('\n')
    return content

sechBodyUrl('0007.html')
print (sechBodyUrl('0007.html'))