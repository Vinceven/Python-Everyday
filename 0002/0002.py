''' 
-*- coding: utf-8 -*-

Created on Thur Sep 13 hh:mm:ss 2018

@author: 01378049
'''

from random import choice
import string
import pymysql.cursors

#根据给定字典长度来给出激活码
def get_code(dict, length, count):
	for i in range(1,int(count)+1):
		code = ''
		for j in range(0,int(length)):
			code = code + str(choice(dict))
		save_to_mysql(i,code)

#设置数据库连接相关信息
host = ('localhost')
user = ('root')
pass_ = ('wozuishuai')
#连接数据库并设置游标
connect = pymysql.connect(host, user, pass_)
connect.autocommit(1)
cursor = connect.cursor()
#创建数据库
DB_NAME = 'PythonEveryDay0002'
table_Name = 'RandomCode'
cursor.execute('drop database if exists %s' %DB_NAME)
cursor.execute('create database if not exists %s' %DB_NAME)
connect.select_db(DB_NAME)
cursor.execute('drop table if exists %s' %table_Name)
create_table_sql = ('''create table %s
					(
					Id int,
					Code varchar(255)
					)''' %table_Name)
cursor.execute(create_table_sql)

#保存到mysql数据库
def save_to_mysql(id, code):
	#执行sql语句
	insert_sql = "insert into PythonEveryDay0002.RandomCode(Id, Code) values('%d', '%s')"
	data = (id, code)
	cursor.execute(insert_sql %data)

if __name__ == '__main__':
	#设定字典为'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	dict = string.ascii_letters[:]
	count = input('请输入激活码个数：')
	if count == '':
		count = 1
	length = input('请输入激活码长度：')
	if length == '':
		length = 8
	get_code(dict, length, count)

