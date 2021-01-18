#函数定义
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

def nop():
    pass

#在函数执行前对函数的参数类型进行检查
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
#同时可以带默认参数如angle=0
#返回多个值,其实返回的是一个tuple，但是tuple可以对各个变量分别赋值
def move(x, y, step=1, angle=0):
    nx = x + step *(angle+1)
    ny = y - step *(angle+0)
    return nx, ny

x, y = move(100, 100, 60, 1)#x和y相当于用tuple分别按照位置赋值
r=move(100, 100, 60, 1)#r为一个tuple
r=move(100,100,angle=3)#即默认参数可以不按照顺序调用


#默认参数最好是不变对象，可变对象会有大坑
#因为默认参数被视为一个变量，当为可变对象时，如果对默认参数变化，则会导致下次调用该函数默认参数为改变后的值
def add_end(L=[]):
    L.append('END')
    return L
#add_end() ['END']
#add_end() ['END', 'END']
#add_end() ['END', 'END', 'END'] 即多次调用不是一个end而是多个end

#可变参数 即参数数量不定时，和c++中指针接近
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
def calc(*numbers): #即在参数前加个*号，表示参数数目是可变的，传入参数后函数将其组装为一个tuple
    sum = 0
    for n in numbers:#使用时将其视为一个tuple
        sum = sum + n * n
    return sum

#调用：
calc(1,2)
calc()#参数数目可变当然可以没有参数
#有list或者tuple时加个*即可直接用，
nums=[1,2,3]
calc(*nums)#*nums表示把nums这个list的所有元素作为可变参数传进去。

#让可变参数x的长度不为0：
if len(x)<=0:
        raise TypeError()


#关键字参数
#关键字参数允许你传入0个或任意个  含参数名的参数 ，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):#即参数前加**
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
#用dict封装，即dict前加两个*号，即**
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

#命名关键字参数，同时命名关键字参数可以添加默认值
#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


#函数传参时参数变化问题
#对于赋值语句如=，无论参数为可变类型list还是不可变类型str，都相当于局部变量，不会真正改变传入参数的值
#对于某种类型的方法，如果参数为可变类型，则会修改其值
#如
a = [1, 2]
def fun(a):
    print('传入函数时a的值为：', a)
    a.insert(2, 3)                                    #修改a
    print('函数改动后a的值为：', a)
fun(a)                                                #调用函数
print('调用函数后全局中a的值为：', a)

# 结果为：

# 传入函数时a的值为： [1, 2]
# 函数改动后a的值为： [1, 2, 3]
# 调用函数后全局中a的值为： [1, 2, 3]

#使用
from testFunction import my_abs  #引入自定义函数，前面为文件名，后面为函数名



#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)  #tuple可以对参数进行分别赋值，但是函数参数中要加上*

#python没有做尾递归优化，所以依旧会溢出
#即尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

#常用函数
abs(-1)
max(1,2)
int("123")
#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs # 变量a指向abs函数
a(-1) # 所以也可以通过a调用abs函数