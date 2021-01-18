#下面是字符和整数的转换
if(True):
    print("ord(\"中\")=",ord("中"))  #获取字符对应的整数编码 可能是Unicode编码
    print("chr(20013)="+chr(20013))   #将整数变为其对应的字符
#字符串str类型和字节byte类型的转换，及传输时按照固定格式解码以及编码
if(True):
    print("abc")    #"abc"是一个字符串str类型的数据
    print(b"abc")   #b"abc"是一个字节byte类型的数据，用于数据传输
    print("\"中文\".encode(\"utf-8\")=","中文".encode("utf-8"))    #将字符串"中文"按照utf-8编码转换为byte类型数据
    print(r"b'\xe4\xb8\xad\xe6\x96\x87'="+b"\xe4\xb8\xad\xe6\x96\x87".decode("utf-8"))   #将bype类型数据用utf-8读取
    print("b\"abc\".decode(\"ascii\")="+b"abc".decode("ascii",errors="ignore"))   #转换时忽略存在的错误
#字符串str的表示方式
if(True):
    str1="i'm a boy"
    str2="i'm a \"boy\" "
    str3="i'm a \\boy\\"
    str4=r"i'm a \\boy\\"           #禁止转义用 r""
    str5="""i'm a boy          
    and i have some books"""        #多行字符串用"""   """"
    print("str1=",str1,"str2=",str2,"str3=",str3,"str4=",str4,"str5=",str5)
#字符串常用函数
if(True):
    print("len(\"中文\")=",len("中文"))      #获取字符串的长度
    print("len(\"中文\".encode(\"utf-8\"))=",len("中文".encode("utf-8")))
    #替换字母
    a = 'abc'
    a=a.replace('a', 'A')



