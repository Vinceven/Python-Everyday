#https://blog.csdn.net/daphne566/article/details/54782657?locationNum=10&fps=1

#有一点问题

#第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。

"""
* 0021
     通常，登陆某个网站或者 APP，需要使用用户名和密码。
     密码是如何加密后存储起来的呢？请使用 Python 对密码加密。
     以下代码参考了[道可叨-用户密码的存储与 Python 示例](http://zhuoqiang.me/password-storage-and-python-example.html)
    by VegB
     2017/1/30
"""

import os
from hmac import HMAC
from hashlib import sha256
import getpass

def encrypt(password, salt = None): # 关键词是None而非NULL
    if salt == None:
        salt = os.urandom(8) # 生成一个八个byte的随机串作为salt
    print('salt:')
    print(salt)
    print('\n')

    password = password.encode('UTF-8') # 改变编码方式

    rst = password
    for i in range(10):
        rst = HMAC(rst, salt, sha256).digest() # 先生成一个HMAC()对象，然后再调用digest()生成hash之后的结果
        print('ENCRYPTION %d: ')
        print(rst)
        print('\n')

    return salt + rst

def compare(input, hashed_password): # hashed_password的前8位是salt
    if encrypt(input, hashed_password[:8]) == hashed_password:
        return True
    return False

password = input("Please type in your password:")
hashed_password = encrypt(password)
input = input("Please type in your password again:")
while compare(input, hashed_password) == False:
    input = input("Please type in your password again:")
print("Correct input! Your password is " + password)