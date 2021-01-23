sorted([1,2,4,2,4])  #对可迭代对象排序？？？？？？？？？？？？？？
print(int("1011",2))#把字符串转换为整数，其中字符串是二进制表示的
"hello".isalpha() #检测字符串是否只由字母组成.如果字符串至少有一个字符并且所有字符都是字母则返回 True，否则返回 False。
"qwe".islower() 
"WQE".isupper()
"123".isdigit()

#map和reduce和filter和sorted的详细使用在testFunction.py中，这两个都是对一个序列的所有内容依次调用函数用的
#map是对每个元素调用同样的函数，reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
r=map(str.upper,list(range(10))) #map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
from functools import reduce
def fn(x, y):
    return x * 10 + y
reduce(fn, [1, 3, 5, 7, 9]) ##如 reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))#结果为[1, 5, 9, 15]  筛选list中的内容，传入参数也有函数

#sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
#list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，
# 而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
sorted([36, 5, -12, 9, -21], key=abs)#按绝对值大小排序
#默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)#忽略大小写的排序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
[1,25,5,2,5,7].sort()