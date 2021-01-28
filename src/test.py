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

# def gk(times=20):
#     last=[1]
#     yield last
#     last=[1,1]
#     yield last
#     k=2
#     while(k<times):
#         now=len(last)-1
#         nowList=[1]
#         for i in range(0,now):
#             nowList.append(last[i]+last[i+1])
#         nowList.append(1)
#         yield nowList
#         last=nowList
#         k+=1
# hh=gk()
# for i in hh:
#     print(i)


        