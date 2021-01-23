#   input()返回的类型是str，如果想比较需要转换为int型号如：grade=int(input("请输入你的分数"))
if False:
    grade=int(input("请输入你的分数"))
    if(grade>60):
        print("你及格了")
        print("你的成绩是"+str(grade)) #字符串拼接时要保证grade是字符串


#字符串str类型和字节byte类型的转换，及传输时按照固定格式解码以及编码
if(False):
    print("abc")    #"abc"是一个字符串str类型的数据
    print(b"abc")   #b"abc"是一个字节byte类型的数据，用于数据传输
    print("\"中文\".encode(\"utf-8\")=","中文".encode("utf-8"))    #将字符串"中文"按照utf-8编码转换为byte类型数据
    print(r"b'\xe4\xb8\xad\xe6\x96\x87'="+b"\xe4\xb8\xad\xe6\x96\x87".decode("utf-8"))   #将bype类型数据用utf-8读取
    print("b\"abc\".decode(\"ascii\")="+b"abc".decode("ascii",errors="ignore"))   #转换时忽略存在的错误
#print()函数的一些问题
if(False):
    print("current rate: 7%%")  #此处%没有当占位符，故显示两个%%
    print("current rate: %d%%"%7) #此处%当占位符，故显示一个%
    print("imporve %4.1f%%"%((85-72)/72*100))

#格式化输出 有%s  .format()   f""  三种方法   占位符%的方法时，可以加数字如%.2f表示小数点后保留两位
if(False):
    #%s
    print("hello,%s" %"dong")    #一个变量时可以省略()
    print("hello,%s,do you have %d$" %("dong",5))
    print("%.2f--%02d"%(2.01010,2))            #占位符和c中的占位符接近，意思差不多
    #.format()
    print( "hello,{0},成绩提升了{1}%".format("ming",17.25))    #按照{0}  {1}去填 ，对数字可加格式
    print( "hello,{0},成绩提升了{1:.03f}%".format("ming",17.25))
    #f""
    r=2.5
    s=3.14*r**2
    print(f"the area of a circle with radius {r} is {s:.1f}")          #按照变量名去填，对数字可加格式
    print(','.join(l))#l为一个list，将list的内容以','为间隔，拼接为一个字符串显示


# 文件读写
# 在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘， 所以，读写文件就是请求操作系统
# 打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件）， 或者把数据写入这个文件对象（写文件）。
# 通用的步骤是先通过open打开文件，并获取文件的描述符，然后read或者write，最后关闭close
# 曾经的语言如c或者c++我们都是在文件部分用try catch 中处理文件（访问文件不存在），python提供了with方法，既可以处理异常(try catch)，也自动close文件
if False:
    # 以前的风格：
    try:
        f = open('/path/to/file', 'r')
        print(f.read())
    finally:
        if f:    #NameError: name 'f' is not defined  这段实际上无法执行，因为open错误直接抛出异常，故没有创建f变量
            f.close()  
    # 现在的风格：
    with open('/path/to/file', 'r') as f:                   #Python引入了with语句来自动帮我们调用close()方法：
        print(f.read())              #这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
    with open('/Users/michael/test.txt', 'w') as f:
        f.write('Hello, world!')

    #读文件时，如果文件不存在，open()函数就会抛出一个IOError的错误
    f = open('/Users/michael/test.txt', 'r')#标示符'r'表示读，其读的是UTF-8的文本文件
    f = open('/Users/michael/test.jpg', 'rb')#要读取的是二进制文件，比如图片、视频等等，用'rb'模式打开文件即可，也是UTF-8的
    f = open('/Users/michael/test.txt', 'w')#写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
    #以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入
    f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
    #要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。
    f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，
    #因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

    # 对文件路径来说，正斜杠和反斜杠效果一样，且反斜杠在字符串中会有转义的含义，容易出问题
    # 文件路径不能用反斜杠‘\’。举个例子，如果我传入的文件路径是这样的：
    # sys.path.append('c:\Users\mshacxiang\VScode_project\web_ddt')
    # 则会报错SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: tr
    # 原因分析：在windows系统当中读取文件路径可以使用\,但是在python字符串中\有转义的含义，如\t可代表TAB，\n代表换行，
    # 所以我们需要采取一些方式使得\不被解读为转义字符。目前有3个解决方案
    # 1、在路径前面加r，即保持字符原始值的意思。
    # sys.path.append(r'c:\Users\mshacxiang\VScode_project\web_ddt')
    # 2、替换为双反斜杠
    # sys.path.append('c:\\Users\\mshacxiang\\VScode_project\\web_ddt')
    # 3、替换为正斜杠
    # sys.path.append('c:/Users/mshacxiang/VScode_project/web_ddt')


    f.read()  #read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
    #读取方法：
    #   read()会一次性读取文件的全部内容
    #   read(size)方法，每次最多读取size个字节的内容
    #   readline()可以每次读取一行内容
    #   readlines()一次读取所有内容并按行返回list
    for line in f.readlines():  #读一些格式化文件常用方法，如配置文件
        print(line.strip()) # 把末尾的'\n'删掉
    f.write('Hello, world!')#往文件写内容
    #要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。


    f.close()
    #最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
    #由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现
    #当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
    # 只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。

    #常用读写模式：
    # t	    文本模式 (默认)。
    # x 	写模式，新建一个文件，如果该文件已存在则会报错。
    # b	    二进制模式。
    # +	    打开一个文件进行更新(可读可写)。
    # U	    通用换行模式（Python 3 不支持）。
    # r	    以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    # rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
    # r+	打开一个文件用于读写。文件指针将会放在文件的开头。
    # rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
    # w	    打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    # wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
    # w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    # wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
    # a	    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    # ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    # a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    # ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。


#StringIO和BytesIO是在内存中操作str和bytes的方法，用的是和读写文件一样的接口。
if False:
    #内存中读写str用StringIO
    #要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
    from io import StringIO
    f=StringIO()
    f.write("hello")      #因为在内存中，所以现在不需要文件路径
    print(f.getvalue())  #显示写入后的str
    #从stringIO中读用read
    g=StringIO("Hello \nhi\n goodbye")
    while True:
        s=f.readline()
        if s=="":            #一行一行的刚好读完
            break
        print(s.strip())

    #内存中读写二进制数据（如图片，歌曲）用BytesIO。
    #BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
    from io import BytesIO
    f=BytesIO()
    f.write("中文".encode("utf-8"))#因为用的字节，所以要调用encode方法
    print(f.getvalue())   #请注意，写入的不是str，而是经过UTF-8编码的bytes。
    g=BytesIO(b"\xe4\xb8\xad\xe6\x96\x87")
    print(g.read())      #读



#Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path
if False:
    import os
    os.name #操作系统类型 如posix-->linux ,unix,mac os x   nt-> windows
    os.uname() #系统详细信息 windows上不能用
    os.environ #系统的环境变量，返回一个dict
    os.environ.get("PATH") #获取环境变量中PATH的值
    os.environ.get("x","default") #没有则返回default
    os.path.abspath('.')# 查看当前目录的绝对路径:
    os.path.join('/Users/michael', 'testdir')# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
    os.mkdir('/Users/michael/testdir') ## 然后创建一个目录:
    os.rmdir('/Users/michael/testdir') ## 删掉一个目录:
    #把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
    #同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
    os.path.split('/Users/michael/testdir/file.txt')#('/Users/michael/testdir', 'file.txt')
    os.path.splitext('/path/to/file.txt')#('/path/to/file', '.txt')os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
    #这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作
    os.rename('test.txt', 'test.py')# 对文件重命名:
    os.remove('test.py')# 删掉文件:
    #但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。
    #幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
    [x for x in os.listdir('.') if os.path.isdir(x)]#列出当前目录下的所有目录
    [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']#列出所有的.py文件

#序列化： 变量从内存（程序中使用的）中变成可存储或传输（文件）的过程
#序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
#从文件中读取内容，变为变量放入内存称为反序列化
if False:
    #Python提供了pickle模块来实现序列化和反序列化。（不通用，只能用于python，无法和其他语言交互，想交互要用json）
    #序列化
    #主要步骤是引入pickle模块，然后调用dumps方法序列化为bytes，然后把bypes写入文件，或者直接调用dump方法，直接序列化为bytes并写入文件
    import pickle
    d=dict(name="bob",age=20,score=88)
    pickle.dumps(d)                           #pickle.dumps()方法把任意对象序列化成一个bytes,然后，就可以把这个bytes写入文件
    f = open('dump.txt', 'wb')
    pickle.dump(d, f)                          #pickle.dump()直接把对象序列化后写入一个file-like Object
    f.close()
    # 反序列化：
    # 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象
    # 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
    f = open('dump.txt', 'rb')
    d = pickle.load(f)
    f.close()

    # 不同语言间的通用格式json的序列化和反序列化
    # json和python的数据类型对应： {}--dict  []---list  "string"--str  123.456---int或float  true--True  null---None

    # python内置对象和json的序列化和反序列化
    # 序列化：
    # 依旧是通过dumps方法序列化为json字符串，或者dump方法直接序列化为json字符串并写入文件
    import json
    d=dict(name="bob",age=20,score=33)
    json.dumps(d)#dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
    # 反序列化：
    # 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    json.loads(json_str)#{'age': 20, 'score': 88, 'name': 'Bob'}
    # JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。

    # 类的序列化和反序列化 json
    # 因为类无法直接序列化，所以先用函数返回类的各个属性的对应关系，并用dict存储，然后对dict进行序列化，（用default等于该函数）
    # 则反序列化是反序列出一个dict，然后我们用dict创建类的实例（用object_hook等于该函数）
    # 序列化
    import json
    class Student(object):
        def __init__(self, name, age, score):
            self.name = name
            self.age = age
            self.score = score
    def student2dict(std):#为Student专门写一个转换函数，帮助json序列化。此函数在类外
        return {           #返回一个dict，然后对dict序列化
        'name': std.name,
        'age': std.age,
        'score': std.score
        }
    s = Student('Bob', 20, 88)
    #print(json.dumps(s)) #报错无法执行，因为不知道如何序列化student
    print(json.dumps(s, default=student2dict)) #告诉dumps用student2dict去序列化  dump也能用，直接对文件操作

    #上述方法太麻烦，我们通过类的__dict__属性，把任意class的实例变为dict。（但是此类不能定义__slots__属性）
    print(json.dumps(s, default=lambda obj: obj.__dict__))
    #因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class

    # 反序列化
    # loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例
    def dict2student(d):
        return Student(d['name'], d['age'], d['score'])
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    print(json.loads(json_str, object_hook=dict2student))  #load也能用，直接读文件

    #对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数
    #如果“ensure_ascii”为false，则返回值可以包含非ASCII字符，如果它们出现在obj中包含的字符串中。 否则，全部这样的字符在JSON字符串中转义。




