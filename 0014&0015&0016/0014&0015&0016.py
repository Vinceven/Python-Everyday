#copyright: https://blog.csdn.net/jingza/article/details/53054178

#第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示

#第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示

#第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示

import json
import xlwt
from collections import OrderedDict
 
 
def ex0014():
 
    with open(r'D:\self\Python\codes\Python everyday\0014&0015&0016\student.txt','r', encoding = 'utf-8') as f:
        content = f.read()
 
    #转化为json，注意转化后的dict的元素位置可能和转化前可能不一样，因此需要ordereddict
    #loads()方法把str对象反序列化为json对象，自定义解码器为ordereddict
    d = json.loads(content,object_pairs_hook=OrderedDict)
    print(d)
    #初始化xls文件
    file = xlwt.Workbook()
    #添加sheet,工作表，名字为test
    table = file.add_sheet('test')
    for row ,i in enumerate(d):   #读取所有字典，row为序号，i为字典关键字key
        table.write(row,0,i)    #写入（行号，列号，key)
        for col,j in enumerate(d[i]):   #col为序号，j为value,有多个，需要迭代
            table.write(row,col+1,j)
 
    file.save(r'D:\self\Python\codes\Python everyday\0014&0015&0016\student.xls')
 
 
 
def ex0015():
    with open(r'D:\self\Python\codes\Python everyday\0014&0015&0016\city.txt','r', encoding = 'utf-8') as f:
        content = f.read()
    #同上
    d = json.loads(content,object_pairs_hook=OrderedDict)
    print (d)
    file = xlwt.Workbook()
    table = file.add_sheet('rest')
    for row ,i in enumerate(d):
        table.write(row,0,i)
        table.write(row,1,d[i])
    file.save(r'D:\self\Python\codes\Python everyday\0014&0015&0016\city.xls')
 
 
def ex0016():
    with open(r'D:\self\Python\codes\Python everyday\0014&0015&0016\numbers.txt','r', encoding = 'utf-8') as f:
        content = f.read()
    #同上
    d = json.loads(content,object_pairs_hook=OrderedDict)
    print (d)
    file = xlwt.Workbook()
    table = file .add_sheet('test')
    for row , i in enumerate(d):
        for col, j in enumerate(i):
            table.write(row,col,j)
 
    file.save(r'D:\self\Python\codes\Python everyday\0014&0015&0016\number.xls')
 
 
if __name__ =="__main__":
    ex0014()
    ex0015()
    ex0016()
