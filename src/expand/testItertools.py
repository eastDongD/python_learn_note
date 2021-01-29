# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
# itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。
# count(1)进行计数，从1开始 1，2，3，4，5
# cycle()会把传入的一个序列无限重复下去
# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
# takewhile()函数根据条件判断来从无限的序列中截取出一个有限的序列
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
# groupby()把迭代器中相邻的重复元素挑出来放在一起
# 无限循环时可以按ctrl+c退出



# count(1)进行计数，从1开始 1，2，3，4，5
if False:
    import itertools
    natuals = itertools.count(15)  # 从15开始计数
    for n in natuals:
        print(n)   # 15 16 17 18 19....


# cycle()会把传入的一个序列无限重复下去：
if False:
    import itertools
    cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
    for c in cs:
        print(c) # A B C A B C A B C....

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
if False:
    import itertools
    ns = itertools.repeat('A', 3)
    for n in ns:
        print(n) # A A A


# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
if False:
    import itertools
    natuals = itertools.count(1)
    ns = itertools.takewhile(lambda x: x <= 10, natuals)
    for x in ns:
        print(x) # 1,2,3,4,5,6,7,8,9,10


# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
if False:
    import itertools
    for c in itertools.chain('ABC', 'XYZ'):
        print(c) # A B C X Y Z

# groupby()把迭代器中相邻的重复元素挑出来放在一起
if False:
    import itertools
    for key, group in itertools.groupby('AAABBBCCAAA'):
        print(key, list(group))
    # A ['A', 'A', 'A']
    # B ['B', 'B', 'B']
    # C ['C', 'C']
    # A ['A', 'A', 'A']

    # 挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，

    for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
        print(key, list(group))
    # A ['A', 'a', 'a']
    # B ['B', 'B', 'b']
    # C ['c', 'C']
    # A ['A', 'A', 'a']