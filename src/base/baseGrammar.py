#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
#申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码：

import time
print("3s后显示下一条")
time.sleep(3)

stonenumber=int(input("输入你的年龄"))
if(20<=stonenumber<=50):
    print("学习的好时机")
elif stonenumber>50:   #判断可以不带括号
    print("学习的坏时机")
else:
    print("玩的时机")

#这个是注释，以#为开头
a=int(input("请输入一个数字"))
if(a/2==0):
    print("你输入的是偶数")
else:
    print("你输入的是奇数")

#for循环和while循环的使用，可以搭配break和continue，和c和c++一样
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)


sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

pass#用于函数定义循环和判断中，相当于一个空语句，在未想好函数如何写时，先写pass编译器不会报错


