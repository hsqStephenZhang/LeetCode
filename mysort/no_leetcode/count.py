import re

def CountingSort(lst,maxValue):
    tmplen=maxValue+1
    Index=0
    tmp=[0]*tmplen
    n=len(lst)
    for i in range(n):
        if not tmp[lst[i]]:
            tmp[lst[i]]=0
        tmp[lst[i]]+=1
    for j in range(tmplen):
        while tmp[j]>0:
            lst[Index]=j
            Index+=1
            tmp[j]-=1
    return lst

x = input("请输入待排序数列：\n")
y = re.split(' *, *| +', x)
for i in range(len(y)):
    y[i]=int(y[i])
arr = CountingSort(y,10)
print(y)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
