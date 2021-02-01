# 通过生成器产生杨辉三角（看下它写这两侧的两个1的写法）
def triangles():
    max = 10
    pre = [1]
    n = 0
    while n < max:
        yield pre
        temp = []
        for x in range(len(pre)+1):
            if x == 0:
                temp.append(1)
            elif x == len(pre):
                temp.append(1)
            else:
                temp.append(pre[x-1] + pre[x])
        n = n + 1
        pre = temp
g=triangles()
for x in g:
    print(x)

# 能用了吗