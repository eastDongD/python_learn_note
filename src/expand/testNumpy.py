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
# 对max min sum 等有个axis属性控制行或者列
# 矩阵运算用dot()函数
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

