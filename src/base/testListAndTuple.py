# 首先是list列表和不变列表tuple的基本使用，然后介绍了切片帮助从list和tuple中取大量的数据
# 然后介绍了列表生成式简便的生成有规律的列表，然后是列表生成器用于一边使用一边生成的列表（节约空间，可以表示无穷序列）
# 接下来是用python的内建模块collections进行对list和tuple的改进
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# namedtuple帮助你自动创建tuple的子类，让你可以通过属性更直观的访问数据

# list列表，存储一组各种各样的数据。list内容可修改。list内部数据类型可以不一样（如同时有整数和字符串）
# 通过索引访问，索引正着数0,1,2,3.....倒着数 -1,-2,-3,....
# list内部可以包含list相当于多维数组，加多个classmates[0][1]去访问
if False:
    classmates = ['Michael', 'Bob', 'Tracy']
    classmates[0]="newMichael"#修改第一项值，注意索引从0开始，也可以倒着数，最后一项为-1 然后-2 -3 ...
    len(classmates) #获取list长度
    classmates.append("dong") #往最后添加dong
    classmates.insert(1,"newD")#索引为1的位置添加newD，索引可以为-1，代表最后一项的位置插入，然后原来的最后一项后移
    classmates.pop()#删除最后一项，同时好像还可以返回最后一项的内容
    classmates.pop(0)#根据索引值进行删除 可以为-1代表删除最后一项
    a=[1,2,4,5,3,7,9,6]
    a.sort() #因为list是可变类型，所以此时a=[1, 2, 3, 4, 5, 6, 7, 9]


# tuple相当于不可以改变的list（不能修改和增删），用()表示
# tuple的元素可以是list，因为list是可变的，故导致看到tuple内容变化。
# （但实际上，tuple存的是指向原来list的指针，该指针还是指向原来的list，故tuple未变）
if False:
    t=("hello","world")
    #注意当tuple只有一个元素时，为了和小括号区分，元素后面要加逗号，否则认为是括号
    a=("hello",)                    # 这个是个tuple 内容是一个字符串
    a=("hello")                     # 这个是个字符串，内容是hello
    a=()                            # tuple可以是一个空的tuple
    t=("a",1,["list1","list2"])     # tuple的内容可以是list，然后list的内容是可变的
    t[2][0]="newlist1"              # 正确，因为list可变，可以理解为tuple指向一组数据或指针，数据和指针内容不变，
                                    # 但是指针指向的内容变了，
                                    # 但是t[2]=["newList1","list2"] 错误，因为这个变得是指针

#切片，帮助取大量数据，list和tuple和字符串均可以用
if False:
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    print(L[0:3])    # 索引0，1，2下的内容，其中0可以省略    ['Michael', 'Sarah', 'Tracy']
    print(L[-3:-1])  # 索引倒数第三个内容到倒数第二个内容    ['Tracy', 'Bob']
    print(L[0:3:2])  # 索引0，1，2下的内容，且每两个取一个   ['Michael', 'Tracy']
    print(L[::5])    # 所有数，每5个取一个，即头和尾可以省略 ['Michael']
     
                                    
# 列表生成式 帮助生成有规律的list（或批量操作原来的list，dict等iterable），需要tuple可以由list进行转换
# 写列表生成式时，把要生成的元素f(x)放到前面，后面跟for循环（for可以有多个）(对循环的x可以用if进行判断），
# 在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，因为要筛选，不能带else。
if False:
    print(list(range(15))) #共15个数字[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] 即从0开始小于15
    list(range(1, 11))#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [x * x for x in range(1, 11)]                         # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    [x * x for x in range(1, 11) if x % 2 == 0]           # [4, 16, 36, 64, 100]
    [m + n for m in 'ABC' for n in 'XYZ']                 # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
    d = {'x': 'A', 'y': 'B', 'z': 'C' }                   # 在dict中拼接字符串
    [k + '=' + v for k, v in d.items()]                   # ['y=B', 'x=A', 'z=C']
    L = ['Hello', 'World', 'IBM', 'Apple']                # 把大写字母改为小写，即可以批量操作字符串
    [s.lower() for s in L]                                # ['hello', 'world', 'ibm', 'apple']
    [x for x in range(1, 11) if x % 2 == 0]               # [2, 4, 6, 8, 10]
    # if在for前做的是一个表达式，必须根据x算一个结果，此时必须带else
    [str(x) if x % 2 == 0 else -x for x in range(1, 11)]  # [-1, '2', -3, '4', -5, '6', -7, '8', -9, '10']

# 列表生成器：如果列表特别大，而我们不需要所有的内容，可以需要list中哪个元素时，计算出哪个元素，不一次性得到整个list
# 优点：节约空间，可以表示无穷的数列
# 生成方法：第一种：将列表生成式中的[]改为()  第二种：通过带有yield的函数生成，每次调用函数相当于产生一个列表生成器
# 访问： 第一种：依次使用next()获取下一个元素   第二种：用for...in对列表生成器进行迭代
if False:
    # 第一种方法：将列表生成式中的[]改为()
    g = (x * x for x in range(10))    #g为 <generator object <genexpr> at 0x1022ef630>
    next(g)                    # 
    print("next(g)=",next(g))  # 1       使用,每次获取下一个元素
    print("next(g)=",next(g))  # 4       使用,每次获取下一个元素
    print("next(g)=",next(g))  # 9       使用,每次获取下一个元素
    for n in g:                # g可以迭代  从上次用的位置接着往下用
        print(n)               # 16 25 36 49 64 81

    # 第二种方法，通过带有yield的函数生成。（带yield的函数称为generator）
    # generator：在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
    # 若有return语句，则无法直接捕获，需要借助StopIteration错误（try  except中捕获）
    # 每次调用函数相当于产生一个列表生成器，此生成器是新的，调用next时和原来的next位置无关
    def fib(max):
        n, a, b = 0, 0, 1
        while n < max:
            yield b
            a, b = b, a + b
            n = n + 1
        return 'done' #此句返回值无法直接捕获，需要借助StopIteration错误
    f = fib(6)
    # 通过next访问
    print("next(f)=",next(f))        # next(f)= 1
    print("next(f)=",next(f))        # next(f)= 1
    print("next(f)=",next(f))        # next(f)= 2
    print("next(f)=",next(f))        # next(f)= 3
    # 通过for in访问
    for n in fib(6):                 # 直接用传参函数，故从头开始访问（相当于一个新的列表生成器）
        print(n)                     # 1 1 2 3 5 8
    for n in f:                      # 用的上面的f，故接着往下走
        print(n)                     # 5 8
  
    #捕获函数的返回值
    g = fib(6)
    while True:
        try:
            x = next(g)
            print('g:', x)
        except StopIteration as e:
            print('Generator return value:', e.value)
            break


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