#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
#所有的类的函数必须有参数self 如：def get_score(self):
#而任何类，最终都可以追溯到根类object
class Student(object):#object表示从哪个类继承下来的，默认为object类，所有类的父类
   
    def __init__(self, name, score,money): #我们认为必须绑定的属性
        self.name = name          #__init__方法的第一个参数永远是self，表示创建的实例本身,相当于this指针
        self.score = score    #有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传
        self.__money=money #这个是私有变量，无法被外部访问

#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))

# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()
bart=Student("dpmg",3)
bart.newname="sdf"  #可以自由地给一个实例变量绑定属性,即使类的定义中没有
print(bart.newname)

#和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.age = 8
bart.age#可访问，有此数据
lisa.age#不可访问，没有此数据
#在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
#你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
#双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：因为不同版本的Python解释器可能会把__name改成不同的变量名。
#总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。

bart = Student('Bart Simpson', 59)
bart.get_name()
bart.__name = 'New Name' # 设置__name变量！
bart.__name #表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。
bart.get_name() 


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
