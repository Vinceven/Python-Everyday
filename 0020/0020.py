#copyright: https://blog.csdn.net/huangxiongbiao/article/details/46300795

#第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计。

#coding: utf-8
import xlrd 
import time

# 存放文件的路径
filepath = '/home/bill/Desktop/list(201504).xls'

def run():
    # 打开表格
    xls = xlrd.open_workbook(filepath)
    sheet = xls.sheet_by_index(0)
    initiative_call = 0
    passtive_call = 0
    # 遍历表格，查到类型为被叫或主叫的行，记录通话时长
    for i in range(3, sheet.nrows):
        rv = sheet.row_values(i)
        if rv[2] == u'被叫':
            struct_time = time.strptime(rv[5], "%H:%M:%S")
            passtive_call += struct_time.tm_hour * 3600 + struct_time.tm_min * 60 + struct_time.tm_sec
        if rv[2] == u'主叫':
            struct_time = time.strptime(rv[5], "%H:%M:%S")
            initiative_call += struct_time.tm_hour * 3600 + struct_time.tm_min * 60 + struct_time.tm_sec
    print '主叫时长：%d分钟' % (initiative_call/60)
    print '被叫时长：%d分钟' % (passtive_call/60)
    print '总通话时长：%d分钟' % ((passtive_call+initiative_call)/60)

if __name__ =="__main__":
    run()