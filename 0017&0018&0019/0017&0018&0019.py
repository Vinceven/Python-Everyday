#https://www.jianshu.com/p/f9c91e0bb18e
#没测试

#第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中

import xlrd
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree

wb = xlrd.open_workbook(r'file\stu.xls')
sh = wb.sheet_by_index(0)

data = dict()
for rx in range(sh.nrows):
    row = sh.row(rx)
    value_list = list()
    key = row[0].value
    for i in row[1:]:
        value = i.value
        value_list.append(value)

    data[key] = value_list
print(data)

root = Element('root')
comment = Comment('学生信息表"id" : [名字, 数学, 语文, 英文]')
root.append(comment)
child = SubElement(root, 'students')
child.text = str(data)
tree = ElementTree(root)
tree.write('file\\student22.xml', encoding='utf8')


#第 0018 题： 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中
import xlrd
from xml.etree.cElementTree import Element, ElementTree, Comment, SubElement

wb = xlrd.open_workbook('file\\city.xls')
ws = wb.sheet_by_index(0)
data = dict()
for rx in range(ws.nrows):
    row = ws.row(rx)
    key = row[0].value
    value = row[1].value
    data[key] = value

root = Element('root')
comment = Comment('城市信息')
root.append(comment)
child = SubElement(root, 'citys')
child.text = str(data)
tree = ElementTree(root)
tree.write('file\\city.xml', encoding='utf8')


#第 0019 题： 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中
import xlrd
from xml.etree.cElementTree import Element, ElementTree, SubElement, Comment

wb = xlrd.open_workbook('file\\num.xls')
ws = wb.sheet_by_index(0)
content = list()
for xr in range(ws.nrows):
    row = ws.row(xr)
    num_list = list()
    for i in row:
        value = i.value
        num_list.append(value)
    content.append(num_list)
print(content)

root = Element('root')
comment = Comment('数字信息')
root.append(comment)
child = SubElement(root, 'numbers')
child.text = str(content)
tree = ElementTree(root)
tree.write('file\\num.xml', encoding='utf8')
