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


#迭代器Iterator和可迭代对象Iterable
#凡是可作用于for循环的对象都是Iterable类型（即可以迭代）
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列，如列表生成器（既可以for，也可以next，即是一个迭代器，当然可以迭代）
#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
isinstance(iter('abc'), Iterator)#由可迭代转化为迭代器


#可以用for进行循环的有：一类是集合数据类型，如list、tuple、dict、set、str等；
                     #一类是generator，包括生成器和带yield的generator function。
#for循环和while循环的使用，可以搭配break和continue，和c和c++一样
#当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行
#判断是否为可以迭代对象
from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代，返回True

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

d = {'a': 1, 'b': 2, 'c': 3}
for value in d.values():
    print(value)
for k, v in d.items():
    print("k="+k)
    print("v="+str(v)) 


for ch in 'ABC':
     print(ch)
#enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
     print(i, value)#此时i为value的索引 0-A 1-B 2-C


sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

pass#用于函数定义循环和判断中，相当于一个空语句，在未想好函数如何写时，先写pass编译器不会报错


