# matplotlib 数据绘图时用，让数据可视化
# 可能用处不大，因为大部分是用前端js展示
# 仿照matlab构建，是python的绘图库，实现数据可视化

# axis：轴

# matplotlib的pyplot模块用于绘图
from matplotlib import pyplot as plt
# 准备要绘制的数据 x和y
x=range(2,26,2)
y=[15,13,14,5,17,20,25,26,26,24,22,18]
# 接下来都是可选的，让图片显示的信息更充分，最后调用show()展示折线图
plt.figure(figsize=(10,6),dpi=80) # figsize是图片大小，dpi是图片清晰度，放大后是否清晰  
                # 此函数是全局的，导入pyplot模块后用，后续所有图片都按照此参数设置的图片大小清晰度进行显示。
                # 此函数需要放在plot函数之前
plt.plot(x, y)  # 传入x和y，通过plot绘制出折线图        
plt.xticks(range(2,25,1)) # 通过传入一个list设置x轴上的刻度 此时x轴为 2，3，4，....24
plt.yticks(range(min(y),max(y)+1))   # 通过传入一个list设置y轴上的刻度
# plt.savefig(r"C:\Users\14228\Desktop\python\data.png")    #  图片保存，此函数需要放在plot绘图后，可以用./data.png表示存在当前路径下   
# plt.savefig(r"C:\Users\14228\Desktop\python\data.svg")  # 可以保存为矢量图，其放大后不会失真
plt.show()  #展示图形
