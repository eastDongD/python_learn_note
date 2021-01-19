if (False):
    #list 相当于可变数组，用[]表示
    #索引list的索引都是正着数0,1,2,3.....倒着数 -1,-2,-3,....
    #list内部数据类型可以不一样（如同时有整数和字符串） 
    #list内部可以包含list相当于多维数组，加多个classmates[0][1]去访问
    classmates = ['Michael', 'Bob', 'Tracy']
    classmates[0]="newMichael"#修改第一项值，注意索引从0开始，也可以倒着数，最后一项为-1 然后-2 -3 ...
    len(classmates) #获取list长度
    classmates.append("dong") #往最后添加dong
    classmates.insert(1,"newD")#索引为1的位置添加newD，索引可以为-1，代表最后一项的位置插入，然后原来的最后一项后移
    classmates.pop()#删除最后一项，同时好像还可以返回最后一项的内容
    classmates.pop(0)#根据索引值进行删除 可以为-1代表删除最后一项

if(False):
    #tuple相当于不可以改变的list，用()表示
    t=("hello","world")
    #注意当tuple只有一个元素时，为了和小括号区分，元素后面要加逗号，否则认为是括号
    a=("hello",) #这个是个tuple 内容是一个字符串
    a=("hello") #这个是个字符串，内容是hello
    a=()#tuple可以是一个空的tuple
    t=("a",1,["list1","list2"])#tuple的内容可以是list，然后list的内容是可变的
    t[2][0]="newlist1" #正确，因为list可变，可以理解为tuple指向一组数据或指针，数据和指针内容不变，但是指针指向的内容变了
                        #但是t[2]=["newList1","list2"] 错误，因为这个变得是指针

if False:
    #列表生成式
    #辅助函数range
    list(range(1, 11))#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
    [x * x for x in range(1, 11)]#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    [x * x for x in range(1, 11) if x % 2 == 0]#[4, 16, 36, 64, 100]
    [m + n for m in 'ABC' for n in 'XYZ']#['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
    #在dict中拼接字符串
    d = {'x': 'A', 'y': 'B', 'z': 'C' }
    [k + '=' + v for k, v in d.items()]#['y=B', 'x=A', 'z=C']
    #把大写字母改为小写，即可以批量操作字符串
    L = ['Hello', 'World', 'IBM', 'Apple']
    [s.lower() for s in L]#['hello', 'world', 'ibm', 'apple']

    #列表生成式中if及ifelse使用
    #在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。
    #if在for后做的是筛选条件，因为要筛选，所以无法加else
    [x for x in range(1, 11) if x % 2 == 0]#[2, 4, 6, 8, 10]
    #if在for前做的是一个表达式，必须根据x算一个结果，此时必须带else
    [x if x % 2 == 0 else -x for x in range(1, 11)]#[-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

if False:
    #列表生成器，如果列表特别大，而我们不需要所有的内容，那么会非常浪费空间
    #所有用列表生成器，需要list中哪个元素时，计算出哪个元素，不一次性得到整个list

    #第一中方法：将列表生成式中的[]改为()
    g = (x * x for x in range(10))#g为 <generator object <genexpr> at 0x1022ef630>

    next(g)#使用,每次获取下一个元素

    for n in g:#g可以迭代
        print(n)

    #第二种方法，通过带有yield的函数生成
    #如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
    #generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
    def fib(max):
        n, a, b = 0, 0, 1
        while n < max:
            yield b
            a, b = b, a + b
            n = n + 1
        return 'done' #此句返回值无法直接捕获，需要借助StopIteration错误
    f = fib(6)
    next(f)  #第一种用法
    for n in fib(6): #第二种用法
        print(n)
    #捕获函数的返回值
    g = fib(6)
    while True:
        try:
            x = next(g)
            print('g:', x)
        except StopIteration as e:
            print('Generator return value:', e.value)
            break

if False:
    #用列表生成式生成杨辉三角
    def triangles():
        max = 10
        pre = [1]
        n = 0
        while n < max:
            yield pre
            temp = []
            for x in range(len(pre)+1):
                if x == 0:
                    temp.append(1)
                elif x == len(pre):
                    temp.append(1)
                else:
                    temp.append(pre[x-1] + pre[x])
            n = n + 1
            pre = temp
    g=triangles()
    for x in g:
        print(x)








#切片，帮助取大量数据，list和tuple和字符串均可以用
if False:
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    L[0:3] #索引0，1，2下的内容，其中0可以省略
    L[-3:-1]#索引倒数第三个内容到倒数第二个内容
    L[0:3:2]#索引0，1，2下的内容，且每两个取一个，即只取1下内容
    L[::5]#所有数，每5个取一个，即头和尾可以省略

if False:
    #range():帮助生成list或者tuple
    print(list(range(15))) #共15个数字[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] 即从0开始小于15
    #排序函数
    a=[1,2,4,5,3,7,9,6]
    a.sort()
    print(a)