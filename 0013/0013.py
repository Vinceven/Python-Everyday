#copyright: https://blog.csdn.net/tavatimsa/article/details/79667716

#第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-) http://tieba.baidu.com/p/2166231880

#coding: utf-8

import requests
import os
from bs4 import BeautifulSoup


# 获得所有的img对象
def get_list_img(webUrl):
    rq = requests.get(webUrl)
    # 解析网页
    soup = BeautifulSoup(rq.text, "lxml")
    return soup.select('img')


# 循环保存
def listSave(picList):
    i = 0
    for img in picList:
        try:
            pic = requests.get(img['src'], timeout=5)
            if pic.status_code == 200:
                saveImg(pic, 'logo' + str(i))
                print (i)
                i += 1
        except requests.exceptions.ConnectionError:
            print("图片无法下载")
            continue
        except requests.exceptions.MissingSchema:
            print("地址无法访问")
            continue


# 保存图片到指定的文件夹
def saveImg(imgObject, filename):
    # 在目录D:\self\Python\codes\Python everyday下创建名为0013的文件夹
    if not os.path.exists(r'D:\self\Python\codes\Python everyday\0013'):
        os.makedirs(os.path.join(r"D:\self\Python\codes\Python everyday", "0013"))
    # 切换工作路径到D:\self\Python\codes\Python everyday\0013下
    os.chdir(r"D:\self\Python\codes\Python everyday\0013")
    # 不存在相同文件名时下载
    if not os.path.exists(r'D:\self\Python\codes\Python everyday\0013\\'+filename+'.jpg'):
        # 将图片存入本地
        fp = open(filename + ".jpg", 'wb')
        fp.write(imgObject.content)  # 写入图片
        fp.close()


if __name__ == '__main__':
    imgList = get_list_img('http://tieba.baidu.com/p/2166231880')
    listSave(imgList)