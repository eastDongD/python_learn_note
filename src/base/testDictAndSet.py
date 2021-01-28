# collections 模块包含很多对dict和set模块的改进？？？？？？？？
# collections是Python内建的一个集合模块，提供了许多有用的集合类。
# namedtuple帮助你自动创建tuple的子类，让你可以通过属性更直观的访问数据
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# defaultdict是一个当访问key不存在时返回一个默认值的dict。
# OrderedDict:key有序的dict
# ChainMap :把多个dict按顺序组成一个逻辑上的dict，但是查找的时候，会按照顺序在内部的dict依次查找。
# Counter是一个简单的计数器，例如，统计字符出现的个数：
# 具体在expand中的testCollections中

# dict为字典：即 key-value  set为无序和无重复元素的集合：即 key
# dict和set的key均不可重复，会自动去重


# 对dict的操作
if True:
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