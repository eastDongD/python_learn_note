# Numpy的基本使用
# array是数组，只有维度的概念，没有行列的概念，用tuple表示，如(3,2,4)表示3维的，第一维3数据，第二维度2数据
# 注意对于一维为(3,) 因为tuple在只有一个元素时必须加逗号（将tuple与括号区分）
# 当array为2维时，其很多操作和矩阵matrix相似（但是乘法不一样）
# dtype属性可选，限制数组元素的数据类型 dtype= np.float32 np.float64 np.int32 np.int64


# 创建一个数组
if False:
    import numpy as np
    array=np.array([[1,2,3],[2,3,4]])       #用list手动创建
    a=np.array([[2,23,4],
                [1,2,3]],dtype=np.int64)
    a1=a #浅复制，a1即是a，对其任何一个改变，另一个也随之改变
    a2=a.copy() #深复制，a2和a内容一样，但此后两者没有关系了
    # 特殊数组
    np.zeros((3,4),dtype=np.int16)    # 全0数组
    np.ones((3,4,5),dtype=np.int16)   # 全1数组
    np.empty((3,4))                 # 空矩阵，类似全0，但是内部有很小的值
    np.arange(10,20,2)              # 10到20 步长为2 [10 12 14 16 18]
    np.arange(0,12).reshape((3,4))  # 用reshape改变m和n
    np.linspace(1,10,20)            # 从一到10共20段 即步长0.5
    b=(np.random.random(6)*10).reshape(2,3)
    c=np.array(b,dtype=np.int16)    # 2*3的随机数组，如：[[1 8 1] [1 5 5]]

    print("number of dim:",array.ndim) # number of dim: 2  行数
    print("shape:",array.shape)        # shape: (2, 3)     维度mxn
    print("size",array.size)           # size 6            元素数目
    print(a.dtype)                     # float64




# array的常用运算
# 其加减乘除sin，con，tan，平方等均是相应位置相加减乘除，sin，con，tan，平方（不是矩阵那一套）
# 两个array运算和两个数字运算一样，但是他会批量的将相应位置的两两运算，并放入相应位置
# 对max min sum mean等有个axis属性控制去掉哪一个维度进行运算 (太复杂，详细说明放在了最后)
# 大部分函数都可以： np.min(a)   a.min() 两种写法
# 矩阵乘法用dot()函数
if False:
    import numpy as np
    a=np.array([10,20,30,40]).reshape(2,2)
    b=np.arange(4).reshape(2,2)  # [[0 1] [2 3]]
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
    # axis=0代表去掉第一个维度，即去掉行这个维度，则对二维，即行进行合并，留min的  np.sum np.min np.max....等均可加此属性
    # axis=1代表去掉第二个维度，即[]内的每个[]只留一个数字，留min的，
    print("np.min(a, axis=0)=",np.min(a, axis=0)) #np.min(a, axis=0)= [10 20]
    print("np.min(a，axis=1)=",np.min(a,axis=1)) #np.min(a，axis=1)= [10 30]
    # 矩阵乘法
    print("np.dot(a,b)=",np.dot(a,b))  #np.dot(a,b)= [[ 40  70] [ 80 150]]
    print("a.dot(b)=",a.dot(b))
    # 转换为矩阵
    b=mat(a) #将array a转换为矩阵
    b.I #矩阵求逆
    b*b #矩阵乘法
    eye(4) # 4*4 的单位矩阵
    # 对数组常用操作
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
    print("np.nonzero(k)=",np.nonzero(k))#用两个数组表示是否非零，显示非零处位置，一个行数，一个列数 (array([0, 0, 1, 1, 1, 2, 2], dtype=int64), array([0, 2, 0, 1, 2, 1, 2], dtype=int64))
    print("np.sort(k)=",np.sort(k)) #逐行排序 [[ 0  4  6] [-1  1  7] [ 0  1  8]]
    print("np.clip(k,3,6)=",np.clip(k,3,6))#让矩阵中小于3的数变为3大于6的数变为6 [[4 3 6] [6 3 3] [3 6 3]]
    print("np.flatten(k)=",k.flatten()) # [ 4  0  6  7 -1  1  0  8  1] 合成一行，对每一个元素做相同的操作时用
    print("k.flat=",k.flat) # <numpy.flatiter object at 0x0000023FA95EAF90> 是个迭代器，可以在for in中访问
    print("k.T=",k.T) # 维度的反转，二维时即转置 k.T= [[ 4  7  0] [ 0 -1  8] [ 6  1  1]]
    print("np.transpose(k)=",np.transpose(k)) # 维度的反转  [[ 4  7  0] [ 0 -1  8] [ 6  1  1]]
                     # 当数据为一维时，其维度反转还是本身，此时维度反转和矩阵转置不一样


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
  

# 对axis的理解：
# axis=0，1，2 表示从外到内的维度。(2, 3, 2) 表示包含2个三行两列的数组。
# axis代表维度，axis=0代表去掉第一个维度。即当axis=n的时候a.shape中相应的索引就会被去除，数组发生了降维
# 对二维，axis=0代表去掉第一个维度，即去掉行的概念，故按照规则合并行。axis=1代表去掉第二个维度，即合并[]内各个[]的内容，即去掉列的概念，按规则合并列

if False:
    import numpy as np
    a=np.array([[[1,13],
                [3,4],
                [5,6],
                [7,8]],
                [[2,3],
                [4,15],
                [5,6],
                [6,7]],
                [[1,2],
                [3,4],
                [25,6],
                [7,9]]])
    #print(a)
    #print(a.shape)  # (3, 4, 2) shape是对每个的最外层说的，第一个[]内有3个大的[]，3个打的[]内都有4个大的[]，4个大的[]内都有两个数字
    #print(np.max(a,axis=0)) #去掉第一个维度， 现在剩下3个(4,2)维度的数据，结果也应为(4,2)维度的数据
        #  [[1,13],      [[2,3],              [[1,2],            结果为：  [[ 2 13]
        #    [3,4],       [4,15],              [3,4],                       [ 4 15]
        #    [5,6],       [5,6],               [25,6],                      [25  6]
        #    [7,8]]       [6,7]],              [7,9]]                       [ 7  9]]
    #print(np.max(a,axis=1)) #去掉第二个维度， 现在剩下4个(3,2)维度的数据，结果也应为(3,2)维度的数据
        # 结果为(3,2)则将有四个数字的维度合并，即 上面注释每一列都是4个数字，选择一个最大的
        # 即原来（3，4，2）---》选最大的变为（3，1，2），然后内容不变，去掉一个[]变为（3，2）
        # [[ 7 13]  7---1，3，5，7   13------13，4，6，8
        #  [ 6 15]  6---2，4，5，6   15------3，15，6，7
        #  [25  9]] 25--1，3，25，7  9--------2，4，6，9
    #print(np.max(a,axis=2)) #去掉第三个维度， 现在剩下2个(3,4)维度的数据，结果也应为(3,4)维度的数据
        # 首先将第三个维度的两个数据按照大小，合并为一个，变为（3，4，1），然后去掉中括号
        # [[[13],[4],[6],[8]],                 [[13,4,6,8],      
        #  [[3],[15],[6],[7]],     -------->    [3,15,6,7],
        #  [[2],[4],[25],[9]]]                  [2,4,25,9]]
    b=np.array([[3,2,7],
                [4,8,6],
                [9,5,1],
                [1,3,5]])
    #print(b)
    #print(np.max(b,axis=0)) # axis=0代表去掉第一维度，结果应为 剩下维度[x,x,x]，x是取第二维度在第一个维度相同位置的最大值
                            # 第二维度在第一个维度相同位置是指每列，故axis=0代表对每列取最大值 [9 8 7]
    #print(np.max(b,axis=1)) # axis=1代表去掉第2维度，结果应为 [x,x,x,x]，x是取第1维度在第2个维度相同位置的最大值
                            # 第1维度在第2个维度相同位置是指每行，故axis=0代表对每行取最大值 [7 8 9 5]
    # 对于2维，可以记为0代表行，1代表列，axis=0代表去掉行，即只留一行，将各行合并时，相应位置取各个行的最大值
                                    # axis=1代去掉列，即只留一列，将各列合并时，相应位置取各个列的最大值 
    # array为数组，不是矩阵，只有维度的概念没有行列的概念，所以行向量和列向量对array来讲一样，都是一维，都是一行[1,2,3]
    # 故axis=1得到的是一维的，相当于行向量，不是列向量
    # print(a)
    # print(a.shape)   # (3, 4, 2)
    # print(np.transpose(a))
    # print(np.transpose(a).shape)  # (2, 4, 3)
    # 对于列向量 d=[1,1,1] 其只有一维(3,) ，所以transpose对tuple变化后还是 (3,) ，
    # 故 无法由行向量变为列向量证明了上述观点
    d=np.array([1,1,1])
    # print(d)                                # [1 1 1]
    # print(d.shape)                          # (3,)
    # print(np.transpose(d))                  # [1 1 1]
    # print(np.transpose(d).shape)            # (3,)
    # 行向量变列向量： 加维度后transpose
    # 先看切片 :
    # print(a[0,:])    # 第一个维度第一个 [[ 1 13] [ 3  4] [ 5  6] [ 7  8]]
    # print(a[:,0,:])  # 第二个维度第一个 [[ 1 13] [ 2  3] [ 1  2]]
    # print(a[:,0])    # 第二个维度第一个 [[ 1 13] [ 2  3] [ 1  2]]  即后面可以省略不写
    # print(a[:,:,0])  # 第三个维度第一个 [[ 1  3  5  7] [ 2  4  5  6] [ 1  3 25  7]]
    print(d[np.newaxis,:]) # 原来为（3，）  现在为 （1，3） 即    [[1 1 1]]
    print(d[:,np.newaxis]) # 原来为（3，）  现在为 （3,1） 即  [[1] [1] [1]]
