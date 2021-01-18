if (True):
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

if(True):
    #tuple相当于不可以改变的list，用()表示
    t=("hello","world")
    #注意当tuple只有一个元素时，为了和小括号区分，元素后面要加逗号，否则认为是括号
    a=("hello",) #这个是个tuple 内容是一个字符串
    a=("hello") #这个是个字符串，内容是hello
    a=()#tuple可以是一个空的tuple
    t=("a",1,["list1","list2"])#tuple的内容可以是list，然后list的内容是可变的
    t[2][0]="newlist1" #正确，因为list可变，可以理解为tuple指向一组数据或指针，数据和指针内容不变，但是指针指向的内容变了
                        #但是t[2]=["newList1","list2"] 错误，因为这个变得是指针

#range():帮助生成list或者tuple
print(list(range(15))) #共15个数字[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] 即从0开始小于15
#排序函数
a=[1,2,4,5,3,7,9,6]
a.sort()
print(a)