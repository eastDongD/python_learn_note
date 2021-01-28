#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码。
# 申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码。

pass#用于函数定义循环和判断中，相当于一个空语句，在未想好函数如何写时，先写pass编译器不会报错

# 赋值
n, a, b = 0, 0, 1 # n=0，a=0，b=1


a, b = b, a + b   # 先根据现有的a，b算出右侧的值，然后分别赋值给左侧
                  # 相当于 t = (b, a + b)    a = t[0]          b = t[1]


q,w,e=(1,2,3)  # q=1 w=2 e=3

# /为除，//为整除 %为取余
print("10/3=",10/3,"10//3=",10//3,"10%3=",10%3)



# 条件判断
if False:
    stonenumber=int(input("输入你的年龄"))
    if(20<=stonenumber<=50):
        print("学习的好时机")
    elif stonenumber>50:   #判断可以不带括号
        print("学习的坏时机")
    else:
        print("玩的时机")

# 循环
# for循环要求作用对象是iterable. 一类是集合数据类型，如list、tuple、dict、set、str等
# 一类是generator，包括生成器和带yield的generator function。
# for循环和while循环的使用，可以搭配break和continue，和c和c++一样
#判断是否为可以迭代对象
if False:
    from collections.abc import Iterable
    isinstance('abc', Iterable) # 判断str是否可迭代，返回True

    # 对字符串进行循环
    for ch in 'ABC':
        print(ch)                    #A

    # 对list的正常循环
    names = ['Michael', 'Bob', 'Tracy']
    for name in names:
        print(name)            # Michael
    # 对list index-value的循环，enumerate函数可以把一个list变成索引-元素对
    for i, value in enumerate(['A', 'B', 'C']):
        print(i, value)#此时i为value的索引 0-A 1-B 2-C

    # 对dict值的循环
    d = {'a': 1, 'b': 2, 'c': 3}
    for value in d.values():
        print(value)                   #1
    # 对dict key-value的循环
    for k, v in d.items():
        print("k="+k)                  #k=a
        print("v="+str(v))             #v=1

    # while循环
    sum = 0
    n = 99
    while n > 0:
        sum = sum + n
        n = n - 2
    print(sum)


