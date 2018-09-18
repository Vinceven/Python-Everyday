#copy from internet
# -*- coding: utf-8 -*-
"""
第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""
"""
分析一下，首先我们需要遍历目录，读取照片文件。
然后我们需要读取照片的尺寸，并与iphone5分辨率进行比较。(iphone5 分辨率：1136*640)
最后如果符合就跳过，如果不符合则缩小照片尺寸。
"""

import os
from PIL import Image

def resize_images_of_a_folder():
    # 通过os.walk()遍历文件夹，暂时只会固定文件夹
    # os.walk() --> 输入文件夹位置，输出3段元组，【文件夹位置】、【文件夹下的所有文件夹】、【文件夹下的所有文件】
    # os.sep --> 系统分隔符，避免多操作系统时，出现问题
    for i in os.walk('c:'+os.sep+'PE'+os.sep+'EE'):
        listOfImg = (i[2])

    # 设定iphone尺寸：1136*640
    widthOfIphone, heightOfIphone = 1136, 640
    # 生成所有文件的位置信息
    for n in listOfImg:
        # 打开图片，如果打不开（非图片）则报错提示
        try:
            myImg = Image.open('c:'+os.sep+'PE'+os.sep+'EE'+os.sep+n)
        except Exception:
            print ("以下文件格式有误："+'c:'+os.sep+'PE'+os.sep+'EE'+os.sep+n)
            continue
        widthOfImg, heightOfImg = myImg.size

        """
        # 对比图片大小
        # 思路：
        # 1.区分图片长短边
        # 2.与iphone分辨率的长短边分别取比值（图片除以iphone）
        # 3.对比比值，将原图长短边都除以较大的比值
        """
        # 区分长短边
        tempWidth, tempHeight = max(widthOfImg, heightOfImg), min(widthOfImg, heightOfImg) 
        # 取比值
        ratioOfWidth, ratioOfHeight = tempWidth/widthOfIphone, tempHeight/heightOfIphone
        # 比较比值，取较大比值继续判断
        biggerRatio =max(ratioOfWidth, ratioOfHeight)
        # 较大的比值大于1，则将原图比例除以该比值得到新的尺寸。
        if biggerRatio > 1:
            widthOfImg /= biggerRatio
            heightOfImg /= biggerRatio
            # 使用resize()函数定义新的尺寸
            # resize()需要整数，因为这边取整为了不超过指定尺寸，所以需要舍弃小数，int()方法默认舍弃，直接使用即可。
            newImg = myImg.resize((int(widthOfImg), int(heightOfImg)))
            newImg.save('c:'+os.sep+'PE'+os.sep+'EE'+os.sep+'resized_'+n)
            print ("已生成了新的图片："+'resized_'+n+ "，尺寸为："+ str(newImg.size))
            myImg.close()


if __name__ == '__main__':
    resize_images_of_a_folder()