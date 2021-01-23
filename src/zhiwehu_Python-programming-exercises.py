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
if False:
    s=input("please input some words:")
    print(sorted(list(set(s.split(" ")))))
    a=[x for x in s.split(" ")]
    print(sorted(list(set(a))))  #此sort会先大写，后小写，然后按照字母顺序排,所以你复制的Then一直在最前


# 11.Question: Write a program which accepts a sequence of comma separated 4 digit binary numbers
#  as its input and then check whether they are divisible by 5 or not. The numbers that are divisible 
# by 5 are to be printed in a comma separated sequence. Example: 0100,0011,1010,1001 Then the output 
# should be: 1010 Notes: Assume the data is input by console.
if False:
    s=input("please input some binary numbers:")
    l=s.split(",")
    k=[x for x in l if int(x,2)%5==0]
    print(",".join(k))

#12.Write a program, which will find all such numbers between 1000 and 3000 (both included) such 
# that each digit of the number is an even number. The numbers obtained should be printed in
#   a comma-separated sequence on a single line.
if False:
    l=[str(x) for x in range(1000,3001) if int(str(x)[0])%2==0 and int(str(x)[1])%2==0 and int(str(x)[2])%2==0 and int(str(x)[3])%2==0]
    print(",".join(l))


#13. Write a program that accepts a sentence and calculate the number of letters and digits. 
# Suppose the following input is supplied to the program: hello world! 123 Then, 
# the output should be: LETTERS 10 DIGITS 3
if False:
    s=input("please input a sentence:")
    letNum,digNum=0,0
    for x in s:
        if x.islower() or x.isupper():
            letNum+=1
        if x.isdigit():
            digNum+=1
    print(letNum)
    print(digNum)

#14. Write a program that accepts a sentence and calculate the number of upper case letters and
#  lower case letters. Suppose the following input is supplied to the program: Hello world! 
# Then, the output should be: UPPER CASE 1 LOWER CASE 9
if False:
    s=input("please input a sentence:")
    lowNum,uppNum=0,0
    for x in s:
        if x.islower():
            lowNum+=1
        if x.isupper():
            uppNum+=1
    print(uppNum)
    print(lowNum)

#15.Write a program that computes the value of a+aa+aaa+aaaa with a given digit as
#  the value of a. Suppose the following input is supplied to the program: 9 
# Then, the output should be: 11106
# a = input()
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# n4 = int( "%s%s%s%s" % (a,a,a,a) )
# print(n1+n2+n3+n4)
if False:
    def sum(x):
        if not isinstance(x,int):
            raise TypeError("x is not a digit")
        i=1
        sum=0
        while(i<5):
            j=1
            y=x
            while(j<i):
                y=y*10+x
                j+=1
            i+=1
            print(y)
            sum+=y
        return sum
    print(sum(9))

#16.Use a list comprehension to square each odd number in a list. The list is input by a 
# sequence of comma-separated numbers. Suppose the following input is supplied to the
#  program: 1,2,3,4,5,6,7,8,9 Then, the output should be: 1,3,5,7,9
if False:
    s=input("please input a sequence of comma-separated numbers:")
    l=[x for x in s.split(",") if int(x)%2!=0]
    print(",".join(l))

#17  Write a program that computes the net amount of a bank account based a transaction 
# log from console input. The transaction log format is shown as following: D 100 W 200
#D means deposit while W means withdrawal. Suppose the following input is supplied
#  to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500
if False:
    s=input("please you account:")
    D=[]
    W=[]
    k=s.split(" ")
    for i,value in enumerate(k):
        if(value=="D"):
            D.append(k[i+1])
        if(value=="W"):
            W.append(k[i+1])
    d,w=0,0
    for x in D:
        d+=int(x)
    for y in W:
        w+=int(y)
    print(d-w)

#18.A website requires the users to input username and password to register. 
# Write a program to check the validity of password input by users. 
# Following are the criteria for checking the password:
# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12 Your program should accept
#  a sequence of comma separated passwords and will check them according to
#   the above criteria. Passwords that match the criteria are to be printed, 
#   each separated by a comma. Example If the following passwords are given as input
#    to the program: ABd1234@1,a F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1
