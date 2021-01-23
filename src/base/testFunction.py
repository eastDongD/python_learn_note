#函数基础操作
if False:
    #引入其他文件的函数
    from testFunction import my_abs  #引入自定义函数，testFunction为文件名，my_abs为函数名
    #函数定义
    def my_abs(x):
        if x >= 0:
            return x #如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。
        else:
            return -x
    def nop():
        pass #定义了函数，暂时不写实现，先用pass代替，帮助搭建函数间的框架

    #在函数执行前对函数的参数类型进行检查
    def my_abs(x):
        if not isinstance(x, (int, float)):
            raise TypeError('bad operand type')
        if x >= 0:
            return x
        else:
            return -x

    #函数传参时参数变化问题
    #对于赋值语句如=，无论参数为可变类型list还是不可变类型str，都相当于局部变量，不会真正改变传入参数的值，故函数对参数做的变化不会影响到原来的参数
    #对于某种类型的方法，如果参数为可变类型，则会修改其值
    a = [1, 2]
    b=(4,5,6)
    def fun(a):
        print('传入函数时a的值为：', a)   
        a.insert(2, 3)                                    #修改a
        print('函数改动后a的值为：', a)    
    fun(a)                                                #调用函数
    print('调用函数后全局中a的值为：', a)   
    # 结果为：
    # 传入函数时a的值为： [1, 2]
    # 函数改动后a的值为： [1, 2, 3]
    # 调用函数后全局中a的值为： [1, 2, 3]         即函数内部调用的insert函数导致原来的a发生了变化


#默认参数
if False:
    def add(x,y=2,z=3):
        return x+y+z
    print(add(1))   #x=1 y=2 z=3
    print(add(1,3)) #x=1 y=3 z=3
    print(add(1,z=6)) #x=1 y=2 z=6    说明默认参数可以不按照顺序调用，即前面用默认参数，后面单独赋值

    #默认参数最好是不变对象，可变对象会有大坑
    #因为默认参数被视为一个变量，当为可变对象时，如果对默认参数变化，则会导致下次调用该函数默认参数为改变后的值
    def add_end(L=[]):
        L.append('END')
        return L
    #add_end() 第一次调用为['END']
    #add_end() 第二次调用为['END', 'END']
    #add_end() 第三次调用为['END', 'END', 'END'] 即多次调用不是一个end而是多个end
    #改进为：
    def add_end_new(L=None):
        if L is None:
            L = []
        L.append('END')
        return L
    #add_end_new() 多次调用后依旧为['END']



#可变参数 即参数数量不定时使用，和c++中指针写法接近
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
if False:
    #定义
    def calc(*numbers): #即在参数前加个*号，表示参数数目是可变的，传入参数后函数将其组装为一个tuple
        # if len(numbers)<=0:      #这两句判断输入的参数长度是否为0，因为时tuple，所以直接用len判断
        #     raise TypeError("no data")        #如果没有参数，则报异常，程序终止
        sum = 0
        for n in numbers:#使用时将其视为一个tuple
            sum = sum + n * n
        return sum
    #调用：
    print(calc(1,2))
    print(calc())#参数数目可变当然可以没有参数
    #有list或者tuple时加个*即可直接用，
    nums=[1,2,3]
    print(calc(*nums))#*nums表示把nums这个list的所有元素作为可变参数传进去。


#关键字参数:允许你传入0个或任意个  含参数名的参数 (如a=3），这些关键字参数在函数内部自动组装为一个dict。
if False:
    #定义
    def person(name, age, **kw):#即参数前加**
        print('name:', name, 'age:', age, 'other:', kw)
    #使用
    person('Michael', 30)
    person('Bob', 35, city='Beijing')
    person('Adam', 45, gender='M', job='Engineer')
    #用dict封装，即dict前加两个*号，即**
    extra = {'city': 'Beijing', 'job': 'Engineer'}
    person('Jack', 24, city=extra['city'], job=extra['job'])  #很垃圾的调用方式
    person('Jack', 24, **extra)   #常用的调用方式
    # **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
    # 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。



#命名关键字参数:  限制关键字参数的名字.例如，只接收city和job作为关键字参数
#命名关键字参数可以添加默认值
if False:
    #定义
    def person(name, age, *, city, job="Student"):
        print(name, age, city, job)
    #如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
    def personTwo(name, age, *args, city, job):
        print(name, age, args, city, job)
    #使用
    person('Jack', 24, city='Beijing')  #使用默认参数
    person('Jack', 24, city='Beijing', job='Engineer')
    #使用封装好的dict，此时和关键字参数一样
    extra = {'city': 'Beijing', 'job': 'ITEngineer'}
    person('Jack', 24, **extra)
    personTwo('Jack', 24,30, **extra) #对带有可变参数的使用

#各种参数组合使用
if False:
    #在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
    #但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
    def f1(a, b, c=0, *args, **kw):
        print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

    def f2(a, b, c=0, *, d, **kw):
        print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

    args = [1,2,3,4,5]
    kw = {'d': 99, 'x': '#'}
    f1(*args, **kw)  #tuple和list均可以对参数进行分别赋值，但是函数参数中要加上*.
                    #此时a=1 b=2 c=3 args=[4,5] kw={'d': 99, 'x': '#'}
    arg2 = (1,2,3)
    f2(*arg2, **kw)  #dict可以对命名关键字进行赋值，只要dict中有命名关键字的名字即可


#返回多个值,其实返回的是一个tuple， tuple可以直接按照位置对各个变量分别赋值
if False:
    def move(x, y, step=1, angle=0):
        nx = x + step *(angle+1)
        ny = y - step *(angle+0)
        return nx, ny

    x, y = move(100, 100, 60, 1)#x和y相当于用tuple分别按照位置赋值
    r=move(100, 100, 60, 1)#r为一个tuple


# 将函数视为参数，传入另一个函数 即高阶函数
if False:
    # 变量可以指向函数，函数的参数和返回值一般都是变量，所以函数的参数和返回值也可以是函数
    # 函数式编程可以把变量指向函数
    def p(x):
        print(x)
        return 1

    a=p                    #即变量指向函数
    a(5)                    #通过变量调用函数
    #可以理解为：函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！

    # 由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，
    # 要用import builtins; builtins.abs = 10  用这个名字去修改

    #高阶函数：一个函数接收另一个函数作为参数
    def add(x, y, f):
        return f(x) + f(y)
    add(-5, 6, abs)#结果为11

#对迭代器的操作如对list  map一次作用与list上 reduce迭代式作用于list上，filter筛选list ，sorted筛选list
if False:
    #map和reduce最好不要直接用现成的函数，容易找不到，先自己封装下(即随便定义一个函数，该函数直接调用已有的函数）
    #找到函数方法：str.capitalize 即函数名前加所属的类名（数据类型名称）
    #map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
    def f(x):
        return x*x
    r=map(f,list(range(10)))
    list(r)#由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list

    #reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
    #如 reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
    from functools import reduce
    def fn(x, y):
        return x * 10 + y
    reduce(fn, [1, 3, 5, 7, 9])

    from functools import reduce
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]
    reduce(fn, map(char2num, '13579')) #即将字符串转换为整数

    #filter筛选序列用，不符合条件的删除
    #filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
    def is_odd(n):
        return n % 2 == 1
    list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))#结果为[1, 5, 9, 15]

    #sorted函数进行排序
    #sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
    #list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，
    # 而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
    #sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
    #key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
    sorted([36, 5, -12, 9, -21], key=abs)#按绝对值大小排序
    #默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
    sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)#忽略大小写的排序
    sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True



if False:

    #python没有做尾递归优化，所以依旧会溢出
    #即尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。


    #可以用lambda函数进行化简 ？？？？？？？
    from functools import reduce
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def char2num(s):
        return DIGITS[s]
    def str2int(s):
        return reduce(lambda x, y: x * 10 + y, map(char2num, s))

    

    

    #返回函数
    def lazy_sum(*args):#定义一个返回求和函数的函数
        def sum():
            ax = 0
            for n in args:
                ax = ax + n
            return ax
        return sum
    f = lazy_sum(1, 3, 5, 7, 9)#此时f是一个函数，但是未执行
    f()#执行返回的该函数，结果为传入值的求和
    #当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
    #即两次相同的调用返回的函数不一样，但是函数的计算结果是一样的。
    #返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
    #返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
    #因为循环变量你认为是从小到大的，但是因为返回函数是最后计算的，计算时
    #循环变量已经变为最大了，故和你想的结果不一样 如：
    def count():
        fs = []
        for i in range(1, 4):
            def f():
                return i*i
            fs.append(f)
        return fs

    f1, f2, f3 = count()
    #此时 f1() f2() f3()的值均为9
    #如果一定要循环变量，则再建一个函数
    def count():
        def f(j):
            def g():
                return j*j
            return g
        fs = []
        for i in range(1, 4):
            fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
        return fs
    #返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。

    #匿名函数，不用显示的定义函数，防止命名冲突
    #用法： 关键字lambda表示匿名函数，冒号前面的x表示函数参数,冒号后面为返回的表达式
    #此时如map需要传入函数时，不用显示的定义一个函数了
    list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    f = lambda x: x * x#即匿名函数也可以当成一个函数对象，然后用f调用 f(5)，同时也可以返回一个匿名函数

    #装饰器：在代码运行期间，增加函数的功能，而不修改函数的定义
    def now():
        print('2015-3-25')
    now.__name__ #函数的名字 ，__name__取函数的名字(左右都是两个下划线)

    #不带参数的装饰器：
    import functools

    def log(func):
        @functools.wraps(func)   #让now的函数名字还是now
        def wrapper(*args, **kw):
            print('call %s():' % func.__name__)
            return func(*args, **kw)
        return wrapper
    @log            #相当于now = log(now)
    def now():
        print('2015-3-25')

    #带参数的装饰器：
    import functools

    def log(text):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
    @log('execute')
    def now():
        print('2015-3-25')

    #用了装饰器后在执行now会在打印2015-3-25前加一个call now()


    #偏函数 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
    #functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
    import functools
    int2 = functools.partial(int, base=2)#把int的base值默认设为2
    max2 = functools.partial(max, 10) #把10作为max的一个输入参数

    #总结：
    #int2 = functools.partial(参数1，参数2，参数3)
    #参数1：函数对象， 参数2：*args  可变参数，接收tuple，list
    #参数3：*kw  关键字参数，接收dict
    #参数1必填，参数2和参数3可省略，那就和原函数没区别了，因为参数1就是原函数，参数2就是可变参数，参数3为关键字参数，int自带关键字参数base，当不传为默认值，传入时必须以base=xxx的形式，对应原始的关键字，参数2传入的话会组装成tuple或list，再通过*args 传入int（*args）如max

    #上两句相当于定义了一个int2函数：
    def int2(x, base=2):
        return int(x, base)


    int2('1000000')
    int2('1000000', base=10)#同时调用时base的值可以显示的输入


    #常用函数
    abs(-1)
    max(1,2)
    int("123")
    int('12345', base=8)#int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
    #函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
    a = abs # 变量a指向abs函数
    a(-1) # 所以也可以通过a调用abs函数

    import math
    math.sqrt(5) #需要带math.