#collections是Python内建的一个集合模块，提供了许多有用的集合类。
# namedtuple帮助你自动创建tuple的子类，让你可以通过属性更直观的访问数据
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# defaultdict是一个当访问key不存在时返回一个默认值的dict。
# OrderedDict:key有序的dict
# ChainMap :把多个dict按顺序组成一个逻辑上的dict，但是查找的时候，会按照顺序在内部的dict依次查找。
# Counter是一个简单的计数器，例如，统计字符出现的个数：




# namedtuple用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
# 作用：tuple存数据访问时用索引不直观，单独创建类麻烦，namedtuple帮助你自动创建类
# 可以理解为namedtuple返回的对象是一个类的定义，且只有属性的访问方法，可以通过该类的定义创建类的实例（但实例是tuple子类，定义不是）
# namedtuple('名称', [属性list])
if False:
    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    print(type(Point))                       # <class 'type'>
    p = Point(1, 2)
    q = Point(3, 4)
    print("p.x="+str(p.x)+" p.y="+str(p.y))  # p.x=1 p.y=2
    print("q.x="+str(q.x)+" q.y="+str(q.y))  # q.x=3 q.y=4
    print(isinstance(p, tuple))              # True
    print(isinstance(Point,tuple))           # False
    print(isinstance(p,Point))               # True

    # 定义一个圆
    Circle = namedtuple('Circle', ['x', 'y', 'r'])


# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# 常用方法有append()，pop()，appendleft()，popleft()
if False:
    from collections import deque
    q = deque(['a', 'b', 'c'])
    q.append('x')
    q.appendleft('y')
    print(q)   #deque(['y', 'a', 'b', 'c', 'x'])
    q.pop()
    q.popleft() 
    print(q)   #deque(['a', 'b', 'c'])


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
# Counter实际上也是dict的一个子类，上面的结果可以看出每个字符出现的次数。
if False:
    from collections import Counter
    c = Counter()
    for ch in 'programming':
        c[ch] = c[ch] + 1
    print(c) # Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
    c.update('hello') # 也可以一次性update
    print(c) # Counter({'r': 2, 'o': 2, 'g': 2, 'm': 2, 'l': 2, 'p': 1, 'a': 1, 'i': 1, 'n': 1, 'h': 1, 'e': 1})



