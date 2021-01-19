number1=0xa12b  #用0x表示是一个16进制数字
number2=1000_0000_10   #整数下可以加_方便区分有多少个0，便于阅读
number3=1.23e3     #这是一个浮点数，e代表10  该数字代表 1.23*10**3
print("number1=",number1,"number2=",number2,"number3=",number3)

print("10/3=",10/3,"10//3=",10//3,"10%3=",10%3)




True and False      #两个bool值
None                #空值

n, a, b = 0, 0, 1#赋值

a, b = b, a + b#相当于

t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]


a=3
print("a是整数",a)
a="str"
print("a是字符串",a)     #即同一个变量可以赋不同类型的值
print(type(a))          #显示数据的类型 <class 'str'>



