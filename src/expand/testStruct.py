# struct模块：bytes和其他数据类型的转换
# struct的pack函数把任意数据类型变成bytes。 unpack可以把bytes转化为其他数据类型
# pack和unpack的第一个参数是处理指令，表示如何读取或转换接下来的内容，剩下的参数为要转换的其他数据或bytes
# 后面的参数个数要和处理指令一致。
# 常用处理指令含义：
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。H：2字节无符号整数。
# struct模块定义的数据类型可以参考Python官方文档：https://docs.python.org/3/library/struct.html#format-characters
if False:
    import struct
    struct.pack('>I', 10240099) #b'\x00\x9c@c'
    struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')#(4042322160, 32896) >后一个处理指令去读几个字节进行转换
    print(struct.pack(">II",163,456))   # b'\x00\x00\x00\xa3\x00\x00\x01\xc8'  将两个数据按照4字节无符号整数转换为bytes
    print(struct.unpack(">II",b'\x00\x00\x00\xa3\x00\x00\x01\xc8'))  #(163, 456) 将bytes转换为两个4字节无符号整数


    # 用unpack读bmp格式的文件
    s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
    # BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
    # 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图； 一个4字节整数：表示位图大小； 
    # 一个4字节整数：保留位，始终为0； 一个4字节整数：实际图像的偏移量； 一个4字节整数：Header的字节数；
    # 一个4字节整数：图像宽度； 一个4字节整数：图像高度； 一个2字节整数：始终为1； 一个2字节整数：颜色数。
    # 故处理指令为 '<ccIIIIIIHH'
    struct.unpack('<ccIIIIIIHH', s)# (b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)
    # 结果显示，b'B'、b'M'说明是Windows位图，位图大小为640x360，颜色数为24。