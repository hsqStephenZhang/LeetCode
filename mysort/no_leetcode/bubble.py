import re
def Bubblesort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    else:
        for i in range(n):
            for j in range(n - i - 1):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


x = input("请输入待排序数列：\n")
y = re.split(' *, *| +', x)
for i in range(len(y)):
    y[i]=int(y[i])
arr = Bubblesort(y)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
