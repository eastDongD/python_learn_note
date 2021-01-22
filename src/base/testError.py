#异常主要用于 可能出错  的代码块
#将可能出错的代码块放入try下（如果执行出错，则后续代码不会继续执行），用except捕获所有可能出现的错误，else是没有出现错误时执行的，finally是无论是否有错误都会执行的
#将代码块放入try下后，有了问题不会退出，而是执行except相应错误下的内容，然后接着往下执行。所以except下对错误的处理有两种
# 1.raise直接抛出，和python原来的机制一样 （python的机制是看你有没有raise抛出，有了错误会一直向上层提交，等待你将其抛出。如果你一直不处理，解释器会帮你抛出错误。
# 2.用log写入日志文件中
# 3.不做处理，print打印，或者其他，让程序执行下去
# 所有的错误类型都是一个类，基类为BaseException，会捕获所有该类型及子类的错误
# 常用的错误类型：ValueError（如 int("a"))  ZeroDivisionError(如 10/0)
# 所有的错误列表： #https://docs.python.org/3/library/exceptions.html#exception-hierarchy
if False:
    try:
        print('try...')
        r = 10 / int('2')
        print('result:', r)
    except ValueError as e:
        print('ValueError:', e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError:', e)
    else:
        print('no error!')
    finally:
        print('finally...')
    print('END')


# try  except可以跨多层调用，及main函数中的一段程序写在了try中，此段程序调用的任何子函数出了问题，都可以在main的try except中捕获
# 也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。这样一来，就大大减少了写try...except...finally的麻烦。
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。
# 出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。 一般最下面是错误的原因
if False:
    import logging                        #引入log头文件
    def foo(s):
        return 10 / int(s)
    def bar(s):
        return foo(s) * 2
    def main():
        try:
            bar('0')
        except Exception as e:
            print('Error:', e)
            logging.exception(e)            #将错误记录下来
        finally:
            print('finally...')
    main()
    print('END')


# 因为错误都是一个类，如果要抛出错误，可以根据需要，自己定义一个错误的class，选择好继承关系，然后，用raise语句抛出
# 因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。
if False:
    class FooError(ValueError):
        pass

    def foo(s):
        n = int(s)
        if n==0:
            raise FooError('invalid value: %s' % s)
        return 10 / n

    foo('0')


#由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。
#raise语句如果不带参数，就会把当前错误原样抛出。
#try except 处理后不raise,程序就不会断，
#在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
if False:
    try:
        10 / 0
    except ZeroDivisionError:
        raise ValueError('input error!')





#平时有问题经常用print显示，python提供了assert和logging
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!' #assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
                                #如果断言失败，assert语句本身就会抛出AssertionError
    return 10 / n

def main():
    foo('0')

#$ python -O err.py   启动Python解释器时可以用-O参数来关闭assert.关闭后，你可以把所有的assert语句当成pass来看。


import logging
logging.basicConfig(level=logging.INFO) #它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
                         #logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
s = '0'
n = int(s)
logging.info('n = %d' % n)#logging不会抛出错误，而且可以输出到文件
print(10 / n)



#$ python -m pdb err.py  调试运行 输入命令l来查看代码 输入命令n可以单步执行代码  任何时候都可以输入命令p 变量名来查看变量：输入命令q结束调试，退出程序

#我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
#运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：
import unittest
                #测试Dict类 （仿造dict写的）
class TestDict(unittest.TestCase):

    def test_init(self):  #以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
        d = Dict(a=1, b='test')  #对每一类测试都需要编写一个test_xxx()方法
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):  #另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError：
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
    def setUp(self):  #调用测试方法前被调用，如连接数据库
        print('setUp...')

    def tearDown(self): ##调用测试方法后被调用，如关闭数据库
        print('tearDown...')
        
if __name__ == '__main__':
        unittest.main()  #运行单元测试，不推荐

#$ python -m unittest mydict_test  第二种运行单元测试的方法


