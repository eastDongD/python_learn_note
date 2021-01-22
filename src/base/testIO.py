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