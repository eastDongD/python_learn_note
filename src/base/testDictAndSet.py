# 首先是dict和set的基本使用
# dict为字典：即 key-value  set为无序和无重复元素的集合：即 key
# dict和set的key均不可重复，会自动去重
# 接下来是用python的内建模块collections进行对dict和set进行改进
# defaultdict是一个当访问key不存在时返回一个默认值的dict。
# OrderedDict:key有序的dict
# ChainMap :把多个dict按顺序组成一个逻辑上的dict，但是查找的时候，会按照顺序在内部的dict依次查找。
# Counter是一个简单的计数器，例如，统计字符出现的个数，会统计字符，并转换为dict

# 对dict的操作
if False:
    # dict可以将key作为索引，进行访问和赋值
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print("Bob="+str(d["Bob"]))              # 根据key进行访问
    d["Bob"]=78                              # 根据key进行赋值
    print("Bob="+str(d["Bob"]))
    # 判断key是否存在
    # 第一种方式
    if("Bob" in d):                          
        print("Bob="+str(d["Bob"]))
    if("bob" in d):
        print("bob="+str(d["bob"]))
    else:
        print("bob不存在")
    # 第二种方式
    d.get("bob")#不存在不返回None
    d.get("bob",-1)#不存在返回自己指定的内容
    #插入与删除
    d["a"]="a"
    print(d)
    d.pop("a")
    print(d)

# 对set的操作：
if False:
    s = set([1, 2, 3])      # {1, 2, 3}
    b = set([2,3,4,5,6])
    c = set([1,2,(3,4,5)])  # {1, 2, (3, 4, 5)} 
    # 但是d = set([1,2,[3,4,5]]) 不行，因为[3,4,5]是可变对象 
    s.add(4)                # {1, 2, 3, 4}
    s.remove(4)             # {1, 2, 3}
    #可以做数学上的交集&，并集|等操作
    print(s&b)              # {2, 3}
    print(s|b)              # {1, 2, 3, 4, 5, 6}
    print(s)                # {1, 2, 3}  即做交集并集等操作后本身不变


# defaultdict是一个当访问key不存在时返回一个默认值的dict。
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
# 默认值是调用函数返回的，而函数在创建defaultdict对象时传入
if False:
    from collections import defaultdict
    dd = defaultdict(lambda: 'N/A')
    dd['key1'] = 'abc'
    dd['key1'] # 'abc' key1存在
    dd['key2'] # 'N/A' key2不存在，返回默认值


# OrderedDict:key有序的dict
if False:
    # OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
    from collections import OrderedDict
    d = dict([('a', 1), ('b', 2), ('c', 3)]) #{'a': 1, 'c': 3, 'b': 2}
    order = OrderedDict([('a', 1), ('b', 2), ('c', 3)])#OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    od = OrderedDict()
    od['z'] = 1
    od['y'] = 2
    od['x'] = 3
    list(od.keys()) # 按照插入的Key的顺序返回   ['z', 'y', 'x']

    #OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
    from collections import OrderedDict
    class LastUpdatedOrderedDict(OrderedDict):
        def __init__(self, capacity):
            super(LastUpdatedOrderedDict, self).__init__()
            self._capacity = capacity
        def __setitem__(self, key, value):
            containsKey = 1 if key in self else 0
            if len(self) - containsKey >= self._capacity:
                last = self.popitem(last=False)
                print('remove:', last)
            if containsKey:
                del self[key]
                print('set:', (key, value))
            else:
                print('add:', (key, value))
            OrderedDict.__setitem__(self, key, value)



# ChainMap :把多个dict按顺序组成一个逻辑上的dict，但是查找的时候，会按照顺序在内部的dict依次查找。
# ChainMap本身也是一个dict
# 用途：如ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数。
# 下面的代码演示了如何查找user和color这两个参数：
if False:
    from collections import ChainMap
    import os, argparse
    # 构造缺省参数:
    defaults = {
        'color': 'red',
        'user': 'guest'
    }
    # 构造命令行参数:
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user')
    parser.add_argument('-c', '--color')
    namespace = parser.parse_args()
    command_line_args = { k: v for k, v in vars(namespace).items() if v }
    # 组合成ChainMap:
    combined = ChainMap(command_line_args, os.environ, defaults)
    # 打印参数  
    # 没有任何参数时，打印出默认参数  python3 use_chainmap.py
    print('color=%s' % combined['color'])  #color=red
    print('user=%s' % combined['user'])    #user=guest
    #当传入命令行参数时，优先使用命令行参数  python3 use_chainmap.py -u bob
    print('color=%s' % combined['color'])  #color=red
    print('user=%s' % combined['user'])    #user=bob
    # 同时传入命令行参数和环境变量，命令行参数的优先级较高 user=admin color=green python3 use_chainmap.py -u bob
    print('color=%s' % combined['color'])  #color=green
    print('user=%s' % combined['user'])    #user=bob


# Counter是一个简单的计数器，例如，统计字符出现的个数：
# Counter实际上也是dict的一个子类，下面的结果可以看出每个字符出现的次数。
if False:
    from collections import Counter
    # c = Counter()
    # for ch in 'programming':
    #     c[ch] = c[ch] + 1
    c = Counter('programming')  #和上面那种写法的结果是一样的
    print(c) # Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
    c.update('hello') # 也可以一次性update
    print(c) # Counter({'r': 2, 'o': 2, 'g': 2, 'm': 2, 'l': 2, 'p': 1, 'a': 1, 'i': 1, 'n': 1, 'h': 1, 'e': 1})