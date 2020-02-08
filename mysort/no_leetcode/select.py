import re
def SelectSort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    else:
        for i in range(n):
            tmp= i
            target = lst[i]
            for j in range(i+1,n):
                if lst[j] < target:
                    tmp = j
                    target=lst[j]
            lst[i],lst[tmp]=lst[tmp],lst[i]
    return lst


x = input("请输入待排序数列：\n")
y = re.split(' *, *| +', x)
for i in range(len(y)):
    y[i]=int(y[i])
arr = SelectSort(y)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
