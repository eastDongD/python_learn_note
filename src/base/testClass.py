#这一页都是关于类的内容
#现有疑问：  一个下划线与两个下划线区别，没有重载函数吗——如重载构造函数，

#类的定义
if False:
    #所有函数第一个参数永远存在且为self，表示创建的实例本身，可以理解为this指针，但是要求你定义函数时显式传入，但是调用函数时不用传入(但是通过类名调用父类的函数时需要传入self)
    #在python中，私有变量和私有函数都是以__双下划线开头的
    #以一个下划线开头的实例变量名，比如_name，此变量的含义是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
    #在Python中，变量名类似__xxx__的，是特殊变量（有特殊功能），特殊变量是可以直接访问的，不是private变量。所以，不能用__name__、__score__这样的变量名。
    class People(object):        #object类为所有类的父类，括号内写的时当前类继承的父类，可以有多个，用逗号隔开。自己设计的基类父类为object
        count=0                   #类属性，类似静态变量，类的所有实例共用一个,访问时必须 类名.变量名 如 People.count （无论类内还是类外）
        def __init__(self,name,gender,age):  #类的构造函数，生成类的对象时，必须传入此函数要求的所有参数，但self不需要传
            People.count+=1             #访问类属性
            self._ID=People.count
            self.name=name       #代表你的People类有一个public的实例属性，类的每个对象都有一个此属性
            self._gender=gender  #代表你的People类有一个Protected的实例属性，实际上和public属性一样（就是public属性），但是约定上类外不访问它。只有类和子类访问
            self.__age=age       #代表你的People类有一个private的实例属性，类的每个对象都有一个此属性.只有此类能访问，子类不能访问
                                #私有变量不是真的不能访问，Python3解释器对外把__age变量改为_People__age，所以你可以通过访问_People__age进行访问
        def __str__(self):       #print(People("小明","男",1))  或者print(perOne)时显示的内容
            return "print类的实例本身显示的内容"  #因为一般在print中调用，所以是返回字符串而不是print一个字符串
        __repr__=__str__         #和__str__一样，调用方法一样，但是一个是调试时看的，一个是运行时看的，一般让两者相等
                                #返回程序开发者看到的字符串，即命令行下，查看到的变量样子，或者调试时看到的样子
        def __call__(self):      #__call__调用类本身时调用的方法, 如 perOne()
            print('Person is --->%s.' % self.name)
        def print_all(self):
            print("Person： _ID="+str(self._ID)+" name="+self.name+" _gender="+self._gender+" __age="+str(self.__age))
        #__slots__ = ("_name",'weight', 'cName',"cNameTwo") # __slots__  限制可以对类绑定的属性 具体情况看下面关于Dog的例子


    #perOne=People()   无法执行，因为构造函数__init__要求多个参数，定义了构造函数后，初始化一个类的实例必须传入其所需要的所有参数
    perOne=People("小明","男",1)
    perTwo=People("小红","女",2)
    perOne.print_all()
    perOne.height=140  #可以在类外给类的实例绑定新的属性，即使类的定义中没有,但是此时绑定的新属性只有你这个实例有，其他实例没有
    print(perOne.height)  #显示140
    #print(perTwo.height) #报错  'People' object has no attribute 'height'
    print(perOne.name)         #访问共有变量name
    print(perOne._People__age) #访问私有变量__age
    print(perOne._gender)  #？？？？？？？？？？？？访问类的保护成员？？？？？？？？？？？
    print(perOne) #打印类的实例，即调用__str__函数
    if callable(perOne()):      #判断perOne对象能否调用本身，即是否写了__call__函数
        perOne()      #即调用__call__函数

    print("------------------------------------------------上述都是父类的内容---------------------------------------------------------------")

    #子类的构造函数
    #1.子类不重写__init__()方法，实例化子类后，会自动调用父类的__init__()的方法。 所以此时要求实例化子类对象时按照父类的__init__函数的要求传参
    #2.子类重写__init__()方法，实例化子类后，将不会自动调用父类的__init__()的方法。
    #3.子类重写__init__()方法又需要调用父类的方法：使用super关键词：
                                        # 1. super(子类，self).__init__(参数1，参数2，....) 如：super(Son, self).__init__(name)
                                        # 2. 父类名称.__init__(self,参数1，参数2，...)

    class Student(People):  #student继承自People类
        def __init__(self,name,gender,age,grade):
            super(Student,self).__init__(name,gender,age)      #此时需要传入self
            #People.__init__(self,name,gender,age)             #此时需要传入self  两个方法都是调用父类的构造函数
            self.__grade=grade
        def print_all(self):#子类重写print_all(self)函数，Student调用print_all时调用此函数，此函数需要访问父类的私有变量，强制访问了，不推荐
            print("Student： _ID="+str(self._ID)+" name="+self.name+"  _gender="+self._gender+"  __age="+str(self._People__age)+" __grade="+str(self.__grade))

    stuOne=Student("小明","男",3,3)
    stuOne.print_all() #Student： name=小明  _gender=男  __age=13 __grade=3  即调用子类的print_all方法
    perThr=People("小黑","男",4)
    perThr.print_all()

    #class Dog(Mammal, RunnableMixIn): #多重继承 Mammal是主要功能  RunnableMixIn是额外功能
    #    pass

    #多重继承中同名函数调用：先子类，然后左父类，左父类左父类，到底后，右边的父类

    #多态的使用，因为python对参数没有要求传入类型，所以对参数一视同仁，只要有参数的相应的方法即可（如print_all)，调用的方法即为参数类型对应的方法
    #即使和People类没有任何关系，只要有print_all函数就不影响下面函数的调用
    def show_people(x):
        x.print_all()
    show_people(perThr)
    show_people(stuOne)
    class a(object):
        def print_all(self):
            print("a class 我有print_all函数")
    a1=a()
    show_people(a1)   #a class 我有print_all函数  证明只要有print_all即可用上述函数



#python是动态的，可以随时给类绑定数据和函数，同时你也可以对其进行限制，这部分都是动态绑定相关的
if False:
    class Dog(object):
        def __init__(self,name):
            self._name=name
        def showName(self):
            print("self._name="+self._name)
        __slots__ = ("_name",'weight', 'cName',"cNameTwo") # __slots__  限制可以对类绑定的属性，当前Dog类中的变量名只能是左侧tuple中存在的变量名
                                                        #用tuple定义允许绑定的属性名称,需要注意的是在__init__中定义的实例属性也要写一遍如 _name
                                                        # 但是类中定义的方法名不用出现


    #现在添加了__slots__后随便绑个属性试下
    #dog.newAtt="qwe"   报错无法执行
    #添加tuple出现的变量名在下面

    #__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的。除非在子类中也定义__slots__，
    # 这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
    #意思很简单，子类是一个新类了，新类不定义__slots__,当然可以有新的属性


    #给单个实例绑定，即你只给一个实例绑定了，当前类的其他实例无法使用你绑定的新内容
    dog=Dog("小狗1")
    dog.weight=30               # 动态给实例绑定一个属性
    print(dog.weight)

    def changeName(self,newName):  #定义一个函数，然后绑定到当前实例
        self._name=newName
    from types import MethodType
    dog.cName=MethodType(changeName,dog)
    dog.cName("小狗1的新名字")
    dog.showName()   #显示self._name=小狗1的新名字 说明上述函数成功绑定



    #给所有实例都绑定方法，即给class绑定方法： （变量的话，因为各个实例内容不一样，所以不应该绑定一样的内容）
    def changeNameTwo(self,newName):  #定义一个函数，然后绑定到当前类
        self._name=newName
    Dog.cNameTwo=changeNameTwo      #给class绑定方法后，所有实例均可调用,类似于类变量，类变量也是所有实例共用一个，和函数一样，所以写法也一样： 类名.方法名
    dog2=Dog("小狗2")
    dog.showName()
    dog2.showName()
    dog.cNameTwo("绑定类方法后小狗1的新名字")
    dog2.cNameTwo("绑定类方法后小狗2的新名字")
    dog.showName()
    dog2.showName()




#因为python对参数要求不严格，所以有需要可以自己对参数严格要求下主要是通过 isinstance type()判断哪个类,以及（动作如has)attr判断类的属性
#以及内部的__getattr__设置没有的变量的返回值
if False:
    isinstance(stuOne, People)#判断一个变量是否是某个类型可以用isinstance()判断 ，stuOne不仅仅是Student也是People
    type("str")                #返回内置对象的类型


    #判断类的类型用isinstance() isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上
    h = Student("小白","男",13,3)
    isinstance(h, Student) #True
    isinstance(h, People)#True
    isinstance(b'a', bytes)#判断是否为字节类型
    isinstance([1, 2, 3], (list, tuple))#判断一个变量是否是某些类型中的一种,可以判断是否是list或者tuple：

    #type()的使用
    if(type(123)==int):
        print("123是int类型")
    import types
    type(show_people)==types.FunctionType                              #show_people为自定义函数 True
    type(abs)==types.BuiltinFunctionType                      #abs为内置的求绝对值函数
    type(lambda x: x)==types.LambdaType                       #匿名函数也可以判断
    type((x for x in range(10)))==types.GeneratorType         #生成器也可以判断


    #对类属性的判断
    print(dir(stuOne))#获取stuOne对象所属类型Student的所有属性和方法，返回值为一个list
    hasattr(stuOne,"x")#判断stuOne对象是否有x属性
    setattr(stuOne,'y',19) #设置一个属性y，其值为19
    getattr(stuOne,'y') #得到属性y的值  和stuOne.y一样
    getattr(stuOne, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
    #属性也可以为函数
    hasattr(stuOne, 'print_all') # 有属性'power'吗？
    getattr(stuOne, 'print_all') # 获取属性'power'  <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
    fn = getattr(stuOne, 'print_all') # 获取属性'power'并赋值到变量fn
    fn() # Student： name=小明  _gender=男  __age=13 __grade=3 调用fn()与调用stuOne.print_all()是一样的
    #对函数的参数限制样例
    def readImage(fp):
        if hasattr(fp, 'read'):
            return readData(fp)
        return None


    # 类外的getattr方法用于返回某个属性的值（函数的方法调用），类内的__getattr__也是返回属性（也可以为方法）的值(通过 实例.属性 的方法调用)

    # 调用不存在的属性时，可以用__getattr__()方法动态返回一个属性
    class Student(object):
        def __init__(self):
            self.name = 'Michael'
        def __getattr__(self, attr):
            if attr=='score':
                return 99
            if attr=='age': #返回函数
                return lambda: 25
            raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr) #仿照python找不到属性时报错

    # 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
    # 这样，我们可以通过判断参数，返回score的值 s.score    
    # 返回函数也行   s.age()
    # 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
    # 注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让Student类只响应特定的几个属性
    # 当然也可以模仿python的默认约定，抛出AttributeError的错误
        # 注： 对一个函数，如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None也可以简写为return。
    a=Student()
    print(a.name)
    print(a.age()) #只写a.age()则显示是一个函数
    print(a.score)
    #print(a.adf)  会按照python的方法报错


    #使用： (这个暂时不是很懂)
    class Chain(object):
        def __init__(self, path=''):
            self._path = path
        def __getattr__(self, path):
            return Chain('%s/%s' % (self._path, path))
        def __str__(self):
            return self._path
        __repr__ = __str__
    print(Chain().status.user.timeline.list)  #'/status/user/timeline/list'



print("---------------------------------------------------下面都是易错点的内容---------------------------------------------------------------")
#易错点：
if False:
    #1.以为修改了私有变量__age，实际上是新建了一个__age变量，因为私有变量在类存的名字为_People__age和你自认为的名字不同,所以你没有对其进行操作
    perTwo.__age=15
    print(perTwo.__age) #新建的共有变量，显示15
    print(perTwo._People__age) #这个才是真正的私有变量，显示13

    #2.实例属性和类属性
    #错误的访问类属性很容易创建同名的实例属性
    #由于实例属性优先级比类属性高，因此当类属性和实例属性同名时，类属性会被屏蔽，所以你得不到你想要的值
    #通过  del s.name  可以删除掉你误创建的实例属性 name，然后你可以通过你的错误方法去访问 类属性name ，但是没意义啊，直接用 类名.类属性 正确访问就行了
    #总结----如果访问类属性，必须用类属性所在的直接类的类名取访问  即 所在类.类属性   这样才能正常访问和赋值，否则容易出问题，创建新的属性
    #访问必须使用People.count即用类名访问，如果用对象名访问，会创建一个名字为count的实例属性，然后实例属性优先级高，接下来访问的都是你新建的实例属性 如：
    print("count="+str(stuOne.count))  #访问count，因为有此类属性可以访问
    stuOne.count=19                    #因为类属性应该用类名访问，所以会创一个count的实例属性，其值为19
    print("stuOne.count="+str(stuOne.count))    # 19  访问的是新建的count的实例属性
    print("People.count="+str(People.count))    # 4   访问的是类的count类属性
    print("Student.count="+str(Student.count))  # 4   访问的是类的count类属性
    People.count=5
    print("stuOne.count="+str(stuOne.count))    # 19  访问的是新建的count的实例属性
    print("People.count="+str(People.count))    # 5   访问的是类的count类属性
    print("Student.count="+str(Student.count))  # 5   访问的是类的count类属性
    Student.count=6                          #因为count在其父类中，可以访问，但赋值会创建一个新的count变量，和People.count无关
    print("stuOne.count="+str(stuOne.count))    # 19  访问的是stuOne新建的count的实例属性
    print("People.count="+str(People.count))    # 5   访问的是基类的count类属性  基类的值没变
    print("Student.count="+str(Student.count))  # 6   访问的是Student新建的count的实例属性
    s1=Student("stu1","男",6,2)
    p1=People("peo1","男",7)
    print("People.count="+str(People.count))    #People.count=7   访问的是基类的count类属性  基类的值没变
    print("Student.count="+str(Student.count))  # Student.count=6   访问的是新建count类属性
    s1.print_all() #Student： _ID=6 name=stu1  _gender=男  __age=6 __grade=2
    p1.print_all() #Person： _ID=7 name=peo1 _gender=男 __age=7  ID和People.count保持一致，这说明Person.count才是你要用的
    #总结----如果访问类属性，必须用类属性所在的直接类的类名取访问  即 所在类.类属性   这样才能正常访问和赋值，否则容易出问题，创建新的属性




#一些花里胡哨的操作：直接访问私有变量，和让类的实例可以像个list，tuple，dict一样使用
if False:
    # 1. 对公有变量我们可以stuOne.name="小黑" 和stuOne.name 方便的查看和修改，而对于私有变量和保护变量我们也可以通过装饰器达到这一效果
    # Python内置的@property装饰器就是   负责把一个方法变成属性调用的
    # 要求：score在内部为保护或者私有即_score或者__score，装饰器装饰后，类外可以直接访问，但是当成public访问即stuOne.score（实际上调用的public方法score）
    # 因为访问实际上是调用的方法，所以修改时可以类型检查，访问时可以按照自己想的分类
    # 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    # 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
    class Student(object):
        def __init__(self,name,score):
            self.name=name
            self._score=score
        @property
        def score(self): #把方法变为属性后，通过这个名字直接访问
            if 100>=self._score>=60:
                return "及格"              
            elif 60>self._score>=0:
                return "不及格"
            else:
                return "无效成绩"          
        @score.setter
        def score(self, value): #把方法变为属性后，通过这个名字直接修改
            if not isinstance(value, int):
                raise ValueError('score must be an integer!')
            if value < 0 or value > 100:
                raise ValueError('score must between 0 ~ 100!')
            self._score = value
        @property
        def lossScore(self):       #对于lossScore方法，将其转换为了属性，因为没有set方法，所以其可以视为只读属性
            return 100-self._score
    stuOne = Student("小明",105)  #初始化时可以，此时直接在__init__中赋值，不会类型检查
    print(stuOne.score) #  无效成绩
    stuOne.score = 60 # OK，实际转化为s.set_score(60)，此时
    print(stuOne.score) # OK， 及格  实际转化为s.get_score()
    print(stuOne.lossScore) #访问只读属性



    # 2.帮助类像一个list，tuple，dict一样
    # 如果一个类想被用于for in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
    # 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
    # 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法 即此方法对于 f[*]的调用  *可以为数字2，切片1:3等等一切
    # 如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，返回的为value
    # 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。
    # 最后，还有一个__delitem__()方法，用于删除某个元素。
    # 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口
    class Fib(object):
        def __init__(self):
            self.a, self.b = 0, 1 # 初始化两个计数器a，b

        def __iter__(self):
            return self # 实例本身就是迭代对象，故返回自己

        def __next__(self):                #其和__iter__一块对应for in的循环
            self.a, self.b = self.b, self.a + self.b # 计算下一个值
            if self.a > 100000: # 退出循环的条件
                raise StopIteration()
            return self.a # 返回下一个值
        def __getitem__(self, n):   #此方法对于 f[*]的调用  *可以为数字2，切片1:3等等一切 n传入后判断其类型进行操作
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
    for n in f:  # for in中调用
        print(n)
    print(f[0])  #切片方法调用
    print(f[1])
    print(f[0:5])


#枚举类，python好像没有枚举类型，就用枚举类替代
if False:
    #无法自己设置的枚举类,从1开始递增
    from enum import Enum
    Month = Enum('Month1', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    #访问： Month为枚举类的实例，我们通过此实例进行访问（必须创建实例Month）。 枚举的每个变量为：Month1.Jan,  Month1.Feb
    print(Month.Jan)  #其为Month1.Jan  其值为  Month1.Jan.value=1
    print(Month.Jan.value) #其值为1
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value) #value属性则是自动赋给成员的int常量，默认从1开始计数。

    #自己设置的枚举类,其值可以自己设置。     不创建类的实例，直接访问即可 Weekday.Mon
    from enum import Enum, unique
    @unique #@unique装饰器可以帮助我们检查保证没有重复值。
    class Weekday(Enum):  #即继承自Enum类
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


#而创建class的方法就是使用type()函数。
#type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
#原来：
class Hello(object):
    def hello(self, name='world'): 
        print('Hello, %s.' % name)

#动态创建：
def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)
Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
h = Hello()
h.hello()  #Hello, world.
print(type(Hello)) #<class 'type'>
print(type(h)) #<class '__main__.Hello'>
#要创建一个class对象，type()函数依次传入3个参数：
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。


#除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
#先定义metaclass，就可以创建类，最后创建实例。
#metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”
#metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。
#所以暂时先不看

