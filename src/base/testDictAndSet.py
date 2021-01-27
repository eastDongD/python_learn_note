#dict和set的key均不可重复，会自动去重
if True:
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print("Bob="+str(d["Bob"]))
    d["Bob"]=78
    print("Bob="+str(d["Bob"]))
    #判断key是否存在
    if("Bob" in d):
        print("Bob="+str(d["Bob"]))
    if("bob" in d):
        print("bob="+str(d["bob"]))
    else:
        print("bob不存在")

    #其他判断是否存在
    d.get("bob")#不存在不返回None
    d.get("bob",-1)#不存在返回自己指定的内容

    #插入与删除
    d["a"]="a"
    print(d)
    d.pop("a")
    print(d)

#无序和无重复元素的集合
 s = set([1, 2, 3])
 s.add(4)
 s.remove(4)
 #可以做数学上的交集&，并集|等操作

# 要创建一个set，需要提供一个list作为输入集合，这个只是创建set的方法，
# 仅此而已（将list的每个元素作为set的每个元素）。
# 举例：s=set(['a','b','c']) 可以创建出{'a','b','c'} 这个set的元素都是不可变对象，
# 当然合法。如果s=set(['a',['b','c']])，就不行了，因为list的第2个元素是个可变对象。
# 并且，如果是使用tuple作为dict或者set的key，(tuple是不可变对象)，
# 必须保证tuple的每个元素本身也不可变,s=set([(1,2,3)])这样是可以的，
# 但是s=set([(1,[2,3])])这样不行。因为tuple(1,2,3)是每个元素本身也不可变，而tuple(1,[2,3])的第二个元素是可变的。



#collections是Python内建的一个集合模块，提供了许多有用的集合类。
# namedtuple帮助你自动创建tuple的子类，让你可以通过属性更直观的访问数据
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# defaultdict是一个当访问key不存在时返回一个默认值的dict。
# OrderedDict:key有序的dict
# ChainMap :把多个dict按顺序组成一个逻辑上的dict，但是查找的时候，会按照顺序在内部的dict依次查找。
# Counter是一个简单的计数器，例如，统计字符出现的个数：
# 具体在expand中的testCollections中