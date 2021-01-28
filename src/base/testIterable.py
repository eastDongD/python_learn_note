# 迭代器Iterator和可迭代对象Iterable
# 凡是可作用于for循环的对象都是Iterable类型（即可以迭代）
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列，
# 如列表生成器（既可以for，也可以next，即是一个迭代器，当然可以迭代）
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。




from collections.abc import Iterable
isinstance('abc', Iterable)             # str是否可迭代，返回True
from collections.abc import Iterator
isinstance(iter('abc'), Iterator)       # 由可迭代转化为迭代器

