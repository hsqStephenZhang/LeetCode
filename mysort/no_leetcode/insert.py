import re

def InsertSort(lst):
    n = len(lst)
    for i in range(1, n):
        temp = lst[i]
        j = i
        while j > 0 and temp < lst[j-1]:
            lst[j] = lst[j-1]
            j -= 1
        lst[j]=temp
    return  lst

x = input("请输入待排序数列：\n")
y = re.split(' *, *| +', x)
for i in range(len(y)):
    y[i]=int(y[i])
arr = InsertSort(y)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
