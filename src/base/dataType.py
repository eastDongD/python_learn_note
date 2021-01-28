# 整数与浮点数
if False:
    number1=0xa12b  #用0x表示是一个16进制数字
    number2=1000_0000_10   #整数下可以加_方便区分有多少个0，便于阅读
    number3=1.23e3     #这是一个浮点数，e代表10  该数字代表 1.23*10**3


# 特殊符号
if False:
    True and False      #两个bool值
    None                #空值


# 字符串str
# str的创建
if False:
    str1="i'm a boy"
    str2="i'm a \"boy\" "           # 内部有和外部相同的引号要用转义符
    str3="i'm a \\boy\\"            # 内部有转义符要用转义符
    str4=r"i'm a \\boy\\"           # 禁止转义用 r""，常用于写正则规则
    str5="""i'm a boy          
    and i have some books"""        # 多行字符串用"""   """"，可以保留换行
   
# str常用函数，str为不可变对象，其函数不会对其本身造成改变
if False:
    a="asASsd"
    print(a.replace("s","K"))         # aKASKd 将s替换为K
    print(a.upper())                  # ASASSD 大写
    print(a.lower())                  # asassd 小写
    print(a.capitalize())             # Asassd 首字母大写
    print(a)                          # asASsd 操作后本身不变
    len("中文")                       # 获取字符串的长度 len("中文")= 2
    len("中文".encode("utf-8"))       # len("中文".encode("utf-8"))= 6
    l="13,14,15,16,17,18".split(",")  # 用split分割字符串，返回一个list ['13', '14', '15', '16', '17', '18']
    print(','.join(l))                # l为一个list，将list的内容以','为间隔，拼接为一个字符串显示 13,14,15,16,17,18

# Counter是一个简单的计数器，例如，统计字符出现的个数：
# Counter实际上也是dict的一个子类，下面的结果可以看出每个字符出现的次数。
if False:
    from collections import Counter
    # c = Counter()
    # for ch in 'programming':
    #     c[ch] = c[ch] + 1
    c = Counter('programming')  #和上面那种写法的结果是一样的
    print(c) # Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
    c.update('hello') # 也可以一次性update
    print(c) # Counter({'r': 2, 'o': 2, 'g': 2, 'm': 2, 'l': 2, 'p': 1, 'a': 1, 'i': 1, 'n': 1, 'h': 1, 'e': 1})

# 字符串和各种数据类型间的转换
if False:
    # 字符串str类型和字节byte类型的转换，即传输时按照固定格式解码以及编码
    print("abc")    # "abc"是一个字符串str类型的数据
    print(b"abc")   # b"abc"是一个字节byte类型的数据，用于数据传输
    "中文".encode("utf-8")    # 将字符串按照utf-8格式进行编码，返回bytes类型数据b'\xe4\xb8\xad\xe6\x96\x87'
    b"\xe4\xb8\xad\xe6\x96\x87".decode("utf-8")  # 将bytes类型数据用utf-8格式进行解码，返回str： 中文
    b"abc".decode("ascii",errors="ignore")   #解码时忽略存在的错误 abc
    # 字符和其对应的Unicode码的转换
    print("ord(\"中\")=",ord("中"))   # 获取字符对应的整数编码 可能是Unicode编码
    print("chr(20013)="+chr(20013))   # 将整数变为其对应的字符
    # 字符串和整数的转换
    print(int("1011",2))# 11   把字符串转换为整数，其中字符串是二进制表示的.显示的是十进制
    print(int("1011"))  # 1011 把字符串转换为整数，其中字符串默认是十进制的
    # 字符串和list的转换
    l="13,14,15,16,17,18".split(",")  # 用split分割字符串，返回一个list ['13', '14', '15', '16', '17', '18']