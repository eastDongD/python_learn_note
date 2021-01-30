# Numpy的基本使用


# 创建一个矩阵或者数组
if False:
    import numpy as np
    array=np.array([[1,2,3],[2,3,4]])       #用list手动创建
    # dtype属性可选，限制数组元素的数据类型 dtype= np.float32 np.float64 np.int32 np.int64
    a=np.array([[2,23,4],
                [1,2,3]],dtype=np.int64)
    # 特殊矩阵
    np.zeros((3,4),dtype=np.int16)    # 全0矩阵
    np.ones((3,4),dtype=np.int16)     # 全1矩阵
    e=np.empty((3,4))                 # 空矩阵，类似全0，但是内部有很小的值
    a=np.arange(10,20,2)              # 10到20 步长为2 [10 12 14 16 18]
    a=np.arange(0,12).reshape((3,4))  # 用reshape改变m和n
    a=np.linspace(1,10,20)            # 从一到10共20段 即步长0.5
    a=np.random.random(2,4)

    print("number of dim:",array.ndim) # number of dim: 2  行数
    print("shape:",array.shape)        # shape: (2, 3)     维度mxn
    print("size",array.size)           # size 6            元素数目
    print(a.dtype)                     # float64

# array的常用运算
# 其加减乘除sin，con，tan，平方等均是相应位置相加减乘除，sin，con，tan，平方（不是矩阵那一套）
# 两个array运算和两个数字运算一样，但是他会批量的将相应位置的两两运算，并放入相应位置
# 对max min sum mean等有个axis属性控制对行或者列进行运算
# 大部分函数都可以： np.min(a)   a.min() 两种写法
# 矩阵乘法用dot()函数
if False:
    import numpy as np
    a=np.array([10,20,30,40]).reshape(2,2)
    b=np.arange(4).reshape(2,2)
    print("a=",a," b=",b)
    print("a-b=",a-b)
    print("a+b=",a+b)       # a+b= [[10 21] [32 43]]
    print("a*b=",a*b)       # a*b= [[0 20] [ 60 120]]
    print("10*b=",10*b)     # 10*b= [[ 0 10] [20 30]]
    print("b**2=",b**2)     # b**2= [[0 1] [4 9]]
    print("np.sin(a)=",np.sin(a)) #np.sin(a)= [[-0.54402111  0.91294525] [-0.98803162  0.74511316]]
    print("np.cos(a)=",np.cos(a))
    print("np.tan(a)=",np.tan(a))
    print("b<3=",b<3)             #[[ True  True] [ True False]]
    print("np.sum(a)=",np.sum(a)) #np.sum(a)= 100
    print("np.min(a)=",np.min(a))
    print("np.max(a)=",np.max(a)) #np.max(a)= 40
    # 可以加上axis属性，从行或者类找 axis=0代表从列找，axis=1代表从行找  np.sum np.min np.max....等均可加此属性
    print("np.min(a，axis=1)=",np.min(a,axis=1)) #np.min(a，axis=1)= [10 30]
    print("np.min(a, axis=0)=",np.min(a, axis=0)) #np.min(a, axis=0)= [10 20]
    # 矩阵乘法
    print("np.dot(a,b)=",np.dot(a,b))  #np.dot(a,b)= [[ 40  70] [ 80 150]]
    print("a.dot(b)=",a.dot(b))
    # 对矩阵常用操作
    k=np.array([[4,0,6],
                [7,-1,1],
                [0,8,1]])
    print("np.argmin(k)=",k.argmin()) # 4 最小值的索引，第四个元素为-1.位置：第一行第一个为0，以行为单位递增
    print("np.argmax(k)=",k.argmax()) # 7 最大值的索引，第7个元素为8
    print("np.mean(k)=",k.mean())      #k中元素平均值 26/9=2.888888
    print("np.mean(k)=",np.mean(k,axis=0))  #k每列中元素平均值 [3.66666667 2.33333333 2.66666667]
    print("np.average(k)=",np.average(k)) # k中元素平均值  2.888888888888889
    print("np.median(k)=",np.median(k))# 中位数 1.0
    print("np.cumsum(k)=",k.cumsum())  #逐步累加，每个位置为原来各位置及前面位置相加的和 [ 4  4 10 17 16 17 17 25 26]
    print("np.diff(k)=",np.diff(k))# 每行相邻两个元素的差 [[-4  6] [-8  2] [ 8 -7]]
    print("np.nonzero(k)=",np.nonzero(k))#用两个矩阵表示是否非零，显示非零处位置，一个行数，一个列数 (array([0, 0, 1, 1, 1, 2, 2], dtype=int64), array([0, 2, 0, 1, 2, 1, 2], dtype=int64))
    print("np.sort(k)=",np.sort(k)) #逐行排序 [[ 0  4  6] [-1  1  7] [ 0  1  8]]
    print("np.clip(k,3,6)=",np.clip(k,3,6))#让矩阵中小于3的数变为3大于6的数变为6 [[4 3 6] [6 3 3] [3 6 3]]
    print("np.flatten(k)=",k.flatten()) # [ 4  0  6  7 -1  1  0  8  1] 合成一行，对每一个元素做相同的操作时用
    print("k.flat=",k.flat) # <numpy.flatiter object at 0x0000023FA95EAF90> 是个迭代器，可以在for in中访问
    print("k.T=",k.T) # 矩阵的转置 k.T= [[ 4  7  0] [ 0 -1  8] [ 6  1  1]]
    print("np.transpose(k)=",np.transpose(k))#矩阵的转置  [[ 4  7  0] [ 0 -1  8] [ 6  1  1]]


# 用索引访问数组中各元素，第一个位置代表行，第二个位置代表列，切片可以使用
if False:
    import numpy as np
    a=np.arange(3,15).reshape(3,4)
    print(a)
    # 索引从0开始
    print(a[2]) #[11 12 13 14]
    print(a[2][1]) # 12
    print(a[2,1])  # 12
    # 对单独的一行、一列可以用切片
    print(a[2,:])  #[11 12 13 14]  取一行
    print(a[:,1])  # [ 4  8 12]   取一列
    print(a[1,1:2]) # [8]

    for row in a:
        print(row) # 依次显示每一行
    for col in np.transpose(a):
        print(col) # 依次显示每一列 （通过转置实现）
    for col in a.T:  # a.T也是转置
        print(col)
    for item in a.flat: #依次显示每一个元素
        print(item) 
# 数组的合并与拆分
# 合并
import numpy as np
a=np.array([1,1,1])  #两个行向量
b=np.array([2,2,2])
c=np.array([[1],[1],[1]])
print(a)
print(b)
print(a.shape) # (3,)  代表是一维的，该维度上有3个元素
print(c.shape) # (3, 1) 代表是二维的，第一个维度上有3个元素，第二个维度都是1个元素
print(np.vstack((a,b))) #上下合并 [[1 1 1] [2 2 2]]
print(np.hstack((a,b))) # 左右合并 [1 1 1 2 2 2]
print(np.concatenate((a,b,b,a),axis=0)) # 左右合并 [1 1 1 2 2 2 2 2 2 1 1 1]  0代表列，对列上做操作即左右合并
# print(np.concatenate((a,b,b,a),axis=1)) # 上下合并  报错 ？？？？
# a.T 没有转置，还是行向量
# np.newaxis加新的维度
# https://blog.csdn.net/weixin_42866962/article/details/82811082
print(a[np.newaxis,:]) # [[1 1 1]]      (1, 3) 原来是(3,) newaxis在:左侧，所以变为 (1,3)
print(a[:,np.newaxis]) # [[1] [1] [1]]  (3, 1) 原来是(3,) newaxis在:右侧，所以变为 (3,1)
print(a.reshape(-1,1)) #[[1] [1] [1]]



# 分割
A=np.arange(12).reshape((3,4))
#相等的分割
print(np.split(A,2,axis=1)) # 即一行分成两段，看起来是前2列一块，后两列一块
print(np.split(A,3,axis=0)) # 即一列分成3段，看起来是每行算一块
#不等的分割
print(np.array_split(A,3,axis=1))#  1 1 1 1 ->11 1 1
print(np.vsplit(A,3)) #纵向分割
print(np.hsplit(A,2)) #横向分割


# is 语句

#赋值
import numpy as np
a=np.arange(4)
b=a  # b就是a，浅复制，相当于指针，指向同一块内存
c=a
d=b
a[0]=11
print(a)
d[1:3]=[22,33]

# 实现深复制，用copy实现
e=a.copy() # 深复制，a变化时，e不变，真正的复制


# 书上
b=mat(a) #将array a转换为矩阵
b.I #矩阵求逆
b*b #矩阵乘法
eye(4) # 4*4 的单位矩阵

#axis=0 表示对行（上下）进行操作计算，axis=1表示对列（左右）进行操作计算。可以把 1 看作一竖表示列，很自然。
#一句话看懂axis：设axis=i ,则numpy沿着第i个下标变化的方向进行操作。
#原文：https://blog.csdn.net/xiongchengluo1129/article/details/79062991
# axis针对的是下标，不是行和列
#二维数组的话，第0个下标是行，axis=0即沿着行变化的方向，也就是列不变行变化的方向，如[【1 2 3】，【4 5 6】，【 7 8 9】]沿着147,258,369方向变化，最小值就是1 2 3，即每一列的最小值
# axis表示轴，对于二维数组来说，axis = 0对列操作，axis = 1是对行操作。
#  axis=0，1，2 表示从外到内的维度。(2, 3, 2) 表示包含2个三行两列的数组。
# 当axis=n的时候shape中相应的索引就会被去除，数组发生了降维，那么是如何降维的呢？首先要清楚shape里的数字都代表什么意义：
# 3代表这个numpy数组里嵌套着3个数组（有三层）， 2代表其中每个数组的行数，3代表其中每个数组的列数。