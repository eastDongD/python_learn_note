#这一页都是关于类的内容
#现有疑问：  一个下划线与两个下划线区别，没有重载函数吗——如重载构造函数，
#类的定义
#所有函数第一个参数永远存在且为self，表示创建的实例本身，可以理解为this指针，但是要求你定义函数时显式传入，但是调用函数时不用传入
#在python中，私有变量和私有函数都是以__双下划线开头的
#以一个下划线开头的实例变量名，比如_name，此变量的含义是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
#在Python中，变量名类似__xxx__的，是特殊变量（有特殊功能），特殊变量是可以直接访问的，不是private变量。所以，不能用__name__、__score__这样的变量名。
class People(object):        #object类为所有类的父类，括号内写的时当前类继承的父类，可以有多个，用逗号隔开。自己设计的基类父类为object
    def __init__(self,name,gender,age):  #类的构造函数，生成类的对象时，必须传入此函数要求的所有参数，但self不需要传
        self.name=name       #代表你的People类有一个public的实例属性，类的每个对象都有一个此属性
        self.__gender=gender #代表你的People类有一个private的实例属性，类的每个对象都有一个此属性 
        self.__age=age       #私有变量不是真的不能访问，Python3解释器对外把__age变量改为_People__age，所以你可以通过访问_People__age进行访问
    def print_all(self):
        print("name="+self.name+" gender="+self.__gender+" age="+str(self.__age))


#perOne=People()   无法执行，因为构造函数__init__要求多个参数，定义了构造函数后，初始化一个类的实例必须传入其所需要的所有参数
perOne=People("小明","男",13)
perTwo=People("小红","女",13)
perOne.print_all()
perOne.height=140  #可以在类外给类的实例绑定新的属性，即使类的定义中没有,但是此时绑定的新属性只有你这个实例有，其他实例没有
print(perOne.height)  #显示140
#print(perTwo.height) #报错  'People' object has no attribute 'height'
print(perOne.name)         #访问共有变量name
print(perOne._People__age) #访问私有变量__age

#子类的构造函数
#1.子类不重写__init__()方法，实例化子类后，会自动调用父类的__init__()的方法。
#2.子类重写__init__()方法，实例化子类后，将不会自动调用父类的__init__()的方法。
#3.子类重写__init__()方法又需要调用父类的方法：使用super关键词：
                                    # 1. super(子类，self).__init__(参数1，参数2，....) 如：super(Son, self).__init__(name)
                                    # 2. 父类名称.__init__(self,参数1，参数2，...)

class Student(People):
    def __init__(self,name,gender,age,grade):
        super(Student,self).__init__(name,gender,age)      #此时需要传入self
        #People.__init__(self,name,gender,age)             #此时需要传入self  两个方法都是调用父类的构造函数
        self.__grade=grade

s=Student("小明","男",13,3)
s.print_all()
print(s._Student__grade)



#易错点：
#1.以为修改了私有变量__age，实际上是新建了一个__age变量，因为私有变量在类存的名字为_People__age和你自认为的名字不同,所以你没有对其进行操作
perTwo.__age=15
print(perTwo.__age) #新建的共有变量，显示15
print(perTwo._People__age) #这个才是真正的私有变量，显示13


if False:
    class Animal(object):
        def run(self):
            print('Animal is running...')

    class Dog(Animal):  #Dog继承自Animal
        
        def run(self): #当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。
            print('Dog is running...')

        def eat(self):
            print('Eating meat...')

    dog = Dog()
    dog.run()  #Dog is running...
    isinstance(dog, Animal)#判断一个变量是否是某个类型可以用isinstance()判断
    #dog不仅仅是Dog还是Animal

    def run_twice(animal):
        animal.run()
    #传入Animal的实例时，Animal is running...
    #传入Dog的实例时，Dog is running...
    #多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，
    #即对对象的类型要求不严格，只要有方法就可以
    #Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。

    type("str")#返回内置对象的类型
    if(type(123)==int):
        print("123是int类型")
    else:
        print("123不是int类型")

    import types
    type(fn)==types.FunctionType #fn为自定义函数 True
    type(abs)==types.BuiltinFunctionType #abs为内置的求绝对值函数
    type(lambda x: x)==types.LambdaType
    type((x for x in range(10)))==types.GeneratorType

    #判断类的类型用isinstance() isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上
    h = Husky()
    isinstance(h, Husky) #True
    isinstance(h, Dog)#True
    isinstance(b'a', bytes)#判断是否为字节类型
    isinstance([1, 2, 3], (list, tuple))#判断一个变量是否是某些类型中的一种,可以判断是否是list或者tuple：

    dir("abc")#获取"abc"对象所属类型字符串的所有属性和方法，返回值为一个list
    hasattr(obj,"x")#判断obj对象是否有x属性
    setattr(obj,'y',19) #设置一个属性y，其值为19
    getattr(obj,'y') #得到属性y的值  和obj.y一样
    getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
    #属性也可以为函数
    hasattr(obj, 'power') # 有属性'power'吗？
    getattr(obj, 'power') # 获取属性'power'  <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
    fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
    fn() # 调用fn()与调用obj.power()是一样的

    def readImage(fp):
        if hasattr(fp, 'read'):
            return readData(fp)
        return None


    #实例属性和类属性
    #实例属性就是一般我们常用的属性，每个对象都有一套
    #类属性就是静态变量，一个类所有对象共用一个
    class Student(object):
        name = 'Student'
    #访问必须使用Student.name即用类名访问，如果用对象名访问，会创建一个名字为name的实例属性，然后实例属性优先级高，接下来访问的都是你新建的实例属性 如：
    s = Student()
    print(s.name) #Student,s没有name的实例属性，所以会访问类属性
    print(Student.name)#Student
    s.name = 'Michael' # 给实例绑定name属性，此时相当于新建了一个实例属性
    print(s.name)#由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性，进而显示类属性Michael
    print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问 Student
    del s.name # 如果删除实例的name属性
    print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了 Student

    #所以类内部访问类属性时必须加类名，否则会报错
    #不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。


    s = Student()
    s.name = 'Michael' # 动态给实例绑定一个属性
    print(s.name)
    Michael

    def set_age(self, age): # 定义一个函数作为实例方法
        self.age = age
    from types import MethodType
    s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
    s.set_age(25) # 调用实例方法
    s.age # 测试结果
    #但是给一个实例绑定的方法，对另一个实例是不起作用的，为了给所有实例都绑定方法，可以给class绑定方法：
    def set_score(self, score):
        self.score = score
    Student.set_score = set_score
    #给class绑定方法后，所有实例均可调用
    s.set_score(100)
    s.score
    #通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。


    #__slots__  限制可以对类绑定的属性，如只允许对Student实例添加name和age属性
    class Student(object):
        __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
    s = Student() # 创建新的实例
    s.name = 'Michael' # 绑定属性'name'
    s.score = 99 # 绑定属性'score' 报错
    #__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的。除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
    #意思很简单，子类是一个新类了，当然可以有新的属性
    #？？？？__init__中的属性是否可以有slots之外的属性


    #有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢
    #Python内置的@property装饰器就是负责把一个方法变成属性调用的：
    #把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    class Student(object):
        
        @property
        def score(self):
            return self._score           #？？？：这个属性不用再init中定义吗
                                        #不在init中定义，是否可以再其他函数中使用
                                        #未在init中定义的其他变量，是否可以再其他函数中使用

        @score.setter
        def score(self, value):
            if not isinstance(value, int):
                raise ValueError('score must be an integer!')
            if value < 0 or value > 100:
                raise ValueError('score must between 0 ~ 100!')
            self._score = value
    s = Student()
    s.score = 60 # OK，实际转化为s.set_score(60)
    s.score # OK，实际转化为s.get_score()

    #还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
    class Student(object):
        
        @property
        def birth(self):
            return self._birth  #为何加下划线 ,函数名为变量名，

        @birth.setter
        def birth(self, value):
            self._birth = value

        @property
        def age(self):
            return 2015 - self._birth

    #上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。



    class Dog(Mammal, RunnableMixIn): #多重继承 Mammal是主要功能  RunnableMixIn是额外功能
        pass

    #多重继承中同名函数调用：先子类，然后左父类，左父类左父类，到底后，右边的父类


    class Student(object):
        def __init__(self, name):
            self.name = name
        def __str__(self):
            return 'Student object (name=%s)' % self.name
        __repr__ = __str__

    __str__  #print(Student("a"))时显示的内容
    __repr__ #返回程序开发者看到的字符串，即命令行下，查看到的变量样子，或者调试时看到的样子

    #帮助类像一个list一样
    #如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
    class Fib(object):
        def __init__(self):
            self.a, self.b = 0, 1 # 初始化两个计数器a，b

        def __iter__(self):
            return self # 实例本身就是迭代对象，故返回自己

        def __next__(self):
            self.a, self.b = self.b, self.a + self.b # 计算下一个值
            if self.a > 100000: # 退出循环的条件
                raise StopIteration()
            return self.a # 返回下一个值
    for n in Fib():  #调用
        print(n)
    #要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
    class Fib(object):
        def __getitem__(self, n):
            if isinstance(n, int): # n是索引
                a, b = 1, 1
                for x in range(n):
                    a, b = b, a + b
                return a
            if isinstance(n, slice): # n是切片   slice代表切片对象
                start = n.start
                stop = n.stop
                if start is None:
                    start = 0
                a, b = 1, 1
                L = []
                for x in range(stop):
                    if x >= start:
                        L.append(a)
                    a, b = b, a + b
                return L
    f = Fib()
    f[0]
    f[1]
    f[0:5]

    #如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。

    #与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。

    #总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口


    #调用不存在的属性时，可以用__getattr__()方法动态返回一个属性
    class Student(object):
        
        def __init__(self):
            self.name = 'Michael'

        def __getattr__(self, attr):
            if attr=='score':
                return 99
            if attr=='age': #返回函数
                return lambda: 25

    #当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值 s.score=99
    #返回函数也行
    s.score
    s.age()
    #注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
    #如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。
    #注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误
    class Student(object):
        
        def __getattr__(self, attr):
            if attr=='age':
                return lambda: 25
            raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

    #使用：
    class Chain(object):
        
        def __init__(self, path=''):
            self._path = path

        def __getattr__(self, path):
            return Chain('%s/%s' % (self._path, path))

        def __str__(self):
            return self._path

        __repr__ = __str__

    Chain().status.user.timeline.list #'/status/user/timeline/list'


    #__call__调用类本身时调用的方法
    class Student(object):
        def __init__(self, name):
            self.name = name

        def __call__(self):
            print('My name is %s.' % self.name)

    s = Student('Michael')
    s() # self参数不要传入 显示My name is Michael.
    callable(Student())#判断Student对象能否调用本身，即是否写了__call__函数


    #枚举类
    from enum import Enum

    Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

    #访问：
    Month.Jan
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value) #value属性则是自动赋给成员的int常量，默认从1开始计数。


    from enum import Enum, unique

    @unique #@unique装饰器可以帮助我们检查保证没有重复值。
    class Weekday(Enum):
        Sun = 0 # Sun的value被设定为0
        Mon = 1
        Tue = 2
        Wed = 3
        Thu = 4
        Fri = 5
        Sat = 6

    #访问
    day1 = Weekday.Mon  #Weekday.Mon
    day2 = Weekday['Tue'] #Weekday.Tue
    Weekday.Tue.value  #2
    print(day1 == Weekday.Tue)
    Weekday(1)#Weekday.Mon 1为索引，即第几个元素，从0开始
    for name, member in Weekday.__members__.items():
        print(name, '=>', member)
    #Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。



