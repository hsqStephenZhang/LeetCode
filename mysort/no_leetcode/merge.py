import re

def MergeSort(lst):
    def merge(left,right):
        tmp=[]
        while left and right:
            if left[0]<right[0]:
                tmp.append(left.pop(0))
            else:
                tmp.append(right.pop(0))
        while left:
            tmp.append(left.pop(0))
        while right:
            tmp.append(right.pop(0))
        return tmp
    n = len(lst)
    if n<=1:
        return lst
    mid = n // 2
    left,right=lst[0:mid],lst[mid:]
    return merge(MergeSort(left),MergeSort(right))



x = input("请输入待排序数列：\n")
y = re.split(' *, *| +', x)
for i in range(len(y)):
    y[i]=int(y[i])
arr = MergeSort(y)
print(y)
print(type(y[1]))
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
