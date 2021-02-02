# matplotlib 数据绘图时用，让数据可视化
# 可能用处不大，因为大部分是用前端js展示
# 仿照matlab构建，是python的绘图库，实现数据可视化

# axis：轴

if False:
    # matplotlib的pyplot模块用于绘图
    from matplotlib import pyplot as plt
    # 第一种可以显示中文字体的方法 只在Windows和linux下有效,全局设置，以后不用在调用
    # 通过设置matplotlib的rc的font，修改默认字体，让其能够显示中文 ，只在Windows和linux下有效
    import matplotlib
    font = {'family' : 'MicroSoft YaHei',
                'weight' : 'bold'}
    matplotlib.rc("font",**font)
    # 第二种通用的显示中文字体的方法 ，Windows mac Linux均可，更自由，但每次需要指定
    from matplotlib import font_manager
    my_font=font_manager.FontProperties(fname=r"C:\Windows\Fonts\msyhl.ttc") # 用路径指定字体，通过源代码可以看有更多参数如size
    # 然后设置x轴 plt.xticks(range(2,26,3),x_p,rotation=45,fontproperties=my_font) # 显示说明x轴用这个字体
    # 但是每次x轴只有第一项正确显示，第二项乱码，其他标题什么都正常


    # 准备要绘制的数据 x和y
    x=range(2,26,2)
    y=[15,13,14,5,17,20,25,26,26,24,22,18]
    y_2=[16,13,15,4,16,25,24,23,21,24,21,21]
    # 接下来都是可选的，让图片显示的信息更充分，最后调用show()展示折线图
    plt.figure(figsize=(10,6),dpi=80) # figsize是图片大小，dpi是图片清晰度，放大后是否清晰  
                    # 此函数是全局的，导入pyplot模块后用，后续所有图片都按照此参数设置的图片大小清晰度进行显示。
                    # 此函数需要放在plot函数之前
    plt.plot(x, y,label="数据1",color="r",linestyle="--",linewidth=5)  # 传入x和y，通过plot绘制出折线图  
    # x 和y是必填，其他都选填，label标签，color线的颜色，linestyle线条风格，linewidth=5线条粗细
    plt.plot(x,y_2,label="数据2") # 当前图上的第二幅数据
    plt.legend(prop=my_font,loc="upper right") # 显示刚才的label 若用方法2，则用prop=my_font显示中文 里面两个参数都是可选的
    # loc控制显示位置，可以用字符串upper right 或者数组的索引0
    #plt.xticks(range(2,26,1)) # 通过传入一个list设置x轴上的刻度 此时x轴为 2，3，4，....24
    x_p=["{}秒".format(x) for x in range(2,26,3)]
    #plt.xticks(range(2,26,3),x_p) # 通过第二个参数让x轴显示的信息更完整（即每个刻度都加上修饰）
    plt.xticks(range(2,26,3),x_p,rotation=45) #参数太长让其旋转45度，能看清
    plt.yticks(range(min(y),max(y)+1))   # 通过传入一个list设置y轴上的刻度（range会自动转换为list）
    # plt.savefig(r"C:\Users\14228\Desktop\python\data.png")    #  图片保存，此函数需要放在plot绘图后，可以用./data.png表示存在当前路径下   
    # plt.savefig(r"C:\Users\14228\Desktop\python\data.svg")  # 可以保存为矢量图，其放大后不会失真

    # 添加描述信息
    plt.xlabel("时间",fontproperties=my_font)  # 若中文无法显示可以通过添加fontproperties=my_font显示中文（第二种中文方法时）
    plt.ylabel("y轴",fontproperties=my_font)
    plt.title("我的第一个图片",fontproperties=my_font)

    # 绘制背景网格，以x，y刻度画线
    plt.grid(alpha=0.4,linestyle=":") # alpha=0.4设置透明度  0为透明  线条风格为虚线....

    plt.show()  #展示图形

# 散点图
if False:
    from matplotlib import pyplot as plt
    import matplotlib
    font = {'family' : 'MicroSoft YaHei',
                'weight' : 'bold'}
    matplotlib.rc("font",**font)

    y=[1,2,2,3,5,4,6,5,6,4,7,8,8,12,9,10,5,11,7,12,10,13,14,15]

    plt.scatter(range(1,25),y)
    plt.xticks(range(1,25)[::3],["{}分".format(x) for x in range(1,25)[::3]],rotation=45)
    plt.title("散点图")
    plt.show()

#条形图
if False:
    from matplotlib import pyplot as plt
    import matplotlib
    font = {'family' : 'MicroSoft YaHei',
                'weight' : 'bold'}
    matplotlib.rc("font",**font)

    x=["哥斯拉","复仇者联盟","盗梦空间","切尔诺贝利","蜘蛛侠","肖申克的救赎","爱情公寓","侏罗纪世界","金刚：骷髅岛",]
    y=[43,23,54,32,54,65,23,67,87]
    y2=[x+4 for x in y]
    # plt.bar(range(len(x)),y,width=0.3) # 竖着的条形图，此时是宽度，且显示控制用x轴
    #plt.xticks(range(len(x)),x,rotation=45)

    plt.barh(range(len(x)),y,height=0.3,color="orange",label="Fir") # 横着的条形图，此时是高度，且显示控制用y轴
    plt.barh([x+0.3 for x in range(len(x))],y2,height=0.3,color="red",label="Sen") # 第二条,主要操作是让x偏移一下
    plt.legend(loc=0)  #在右下角显示两条柱状图啥意思
    plt.yticks(range(len(x)),x,rotation=45)
    plt.title("条形图")
    plt.show()

# 绘制直方图
if False:
    from matplotlib import  pyplot as plt
    x=[77, 59, 21, 22, 55, 8, 53, 72, 33, 96, 6, 45, 31, 39, 62, 70, 6, 63, 16, 70, 67, 33, 99, 35, 35, 73, 23, 81, 43, 4, 80, 18, 88, 79, 74, 53, 80, 37, 12, 35, 87, 70, 44, 21, 53, 40, 58, 39, 35, 36, 15, 1, 14, 14, 71, 99, 23, 10, 14, 17, 15, 17, 69, 45, 15, 69, 16, 78, 59, 50, 48, 66, 64, 24, 9, 7, 88, 44, 26, 83, 10, 74, 68, 10, 70, 40, 76, 89, 2, 40, 14, 9, 9, 82, 77, 15, 60, 67, 70, 3]
    plt.hist(x,20) # 绘制直方图，并分成20组 20可用 (max(x)-max(y))//组距 代替
    plt.xticks(range(0,101)[::5])
    plt.show()

