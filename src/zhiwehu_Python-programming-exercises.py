#1. 编写一个程序，该程序将查找所有可被 7 除除但不是 5 的倍数，介于 2000 和 3200 之间（包括）。获取的数字应按逗号分隔的序列打印在一行上
if False:
    k=[x for x in range(2000,3201) if x%7==0 and x%5!=0]  #正确答案
#2. 编写一个可以计算给定数字因子的程序。结果应按逗号分隔的序列打印在一行上。假设向程序提供以下输入： 8 然后，输出应为： 40320
# 他的意思是求阶乘
if False:
    def JieCheng(n):
        if not isinstance(n,int):
            raise TypeError("n is not int")
        k=1
        for x in range(1,n+1):
            k*=x
        return k
#3.使用给定的积分数 n，编写一个程序以生成包含 （i， i*i） 的字典，这样该字典是介于 1 和 n 之间的积分数（包括）。然后程序应该打印字典。
# 假设向程序提供以下输入： 8 然后，输出应为：[1： 1， 2： 4， 3： 9， 4： 16， 5： 25， 6： 36， 7： 49， 8： 64]
if False:
    def creatDict(n):
        if not isinstance(n,int):
            raise TypeError("n is not int")
        d={}
        for x in range(1,n+1):
            d[x]=x*x
        print(d)

#4.编写一个程序，该程序接受控制台中的逗号分隔数序列，并生成一个列表和包含每个数字的元组。
# 假设向程序提供以下输入：34，67，55，33，12，98
#  然后， 输出应为：[34'、'67'、'55"，'33'，'12'，'98'= （'34'，'67'，'55'，'33'，'12'，'98'）
if False:
    def four():
        value=input("请输入一串数字如34，67，55，33，12，98:")
        l=value.split("，")
        t=tuple(l)
        print(l)
        print(t)
    four()
#5.定义一个类，该类至少有两种方法：getString：从控制台输入 printString 获取字符串：在大写中打印字符串。也请包括简单的测试函数来测试类方法。
if False:
    class String(object):
        def __init__(self):
            self.__string=""
        def getString(self):
            self.__string=input("请输入字符串：")
        def printString(self):
            print(self.__string.upper())
    s=String()
    s.getString()
    s.printString()

#6. Write a program that calculates and prints the value according to the given formula:
#  Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and
#  H: C is 50. H is 30. D is the variable whose values should be input to your program 
# in a comma-separated sequence. Example Let us assume the following comma separated input 
# sequence is given to the program: 100,150,180 The output of the program should be: 18,22,24
if False:
    import math
    def six(D):
        answer=[]
        
        for d in D:
            answer.append(int(math.sqrt(2*50*d/30)))
        return answer
    l=six([100,150,180])
    k=[str(x) for x in l]
    print(','.join(k))

#7.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1. 
# Example Suppose the following inputs are given to the program: 3,5 
# Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#即输入矩阵维数，输出矩阵，矩阵值为i*j
if False:
    def juZhen(x,y):
        i,j=0,0
        matrx=list()
        while i<x:
            j=0
            L=[]
            while(j<y):
                L.append(i*j)
                j+=1
            matrx.append(L)
            i+=1
        print(matrx)
    juZhen(3,5)

#8.Write a program that accepts a comma separated sequence of words as input and prints the words in a
#  comma-separated sequence after sorting them alphabetically. Suppose the following input is supplied to the program:
#  without,hello,bag,world Then, the output should be: bag,hello,without,world
if False:
    def splitAndSort(s):
        l=s.split(",")
        l.sort()
        print(','.join(l))
    splitAndSort("without,hello,bag,world")

#9.Write a program that accepts sequence of lines as input and prints the lines after making all
#  characters in the sentence capitalized. Suppose the following input is supplied to the program:
#  Hello world Practice makes perfect Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT
if False:
    lines = []
    while True:
        s = input()
        if s:
            lines.append(s.upper())
        else:
            break;

    print(" ".join(lines))

#10. Question: Write a program that accepts a sequence of whitespace separated words as input and 
# prints the words after removing all duplicate words and sorting them alphanumerically. 
# Suppose the following input is supplied to the program: hello world and practice makes perfect 
# and hello world again Then, the output should be: again and hello makes perfect practice world
s=input("please input some words:")
print(sorted(list(set(s.split(" ")))))
a=[x for x in s.split(" ")]
print(sorted(list(set(a))))  #此sort会先大写，后小写，然后按照字母顺序排,所以你复制的Then一直在最前





