#   input()返回的类型是str，如果想比较需要转换为int型号如：grade=int(input("请输入你的分数"))
grade=int(input("请输入你的分数"))
if(grade>60):
    print("你及格了")
    print("你的成绩是"+str(grade)) #字符串拼接时要保证grade是字符串


#字符串str类型和字节byte类型的转换，及传输时按照固定格式解码以及编码
if(True):
    print("abc")    #"abc"是一个字符串str类型的数据
    print(b"abc")   #b"abc"是一个字节byte类型的数据，用于数据传输
    print("\"中文\".encode(\"utf-8\")=","中文".encode("utf-8"))    #将字符串"中文"按照utf-8编码转换为byte类型数据
    print(r"b'\xe4\xb8\xad\xe6\x96\x87'="+b"\xe4\xb8\xad\xe6\x96\x87".decode("utf-8"))   #将bype类型数据用utf-8读取
    print("b\"abc\".decode(\"ascii\")="+b"abc".decode("ascii",errors="ignore"))   #转换时忽略存在的错误
#print()函数的一些问题
if(True):
    print("current rate: 7%%")  #此处%没有当占位符，故显示两个%%
    print("current rate: %d%%"%7) #此处%当占位符，故显示一个%
    print("imporve %4.1f%%"%((85-72)/72*100))

#格式化输出 有%s  .format()   f""  三种方法   占位符%的方法时，可以加数字如%.2f表示小数点后保留两位
if(True):
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
