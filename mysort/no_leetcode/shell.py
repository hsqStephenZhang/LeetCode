import re


def ShellSort(lst):
    def shellinsert(arr, d):
        n = len(arr)
        for i in range(d, n):
            temp = arr[i]
            j = i-d
            while j >= 0 and temp < arr[j]:
                arr[j+d] = arr[j ]
                j -= d
            if j!=i-d:
                arr[j+d]=temp
    n = len(lst)
    d = n // 2
    if n <= 1:
        return lst
    else:
        while d >= 1:
            shellinsert(lst, d)
            d = d // 2
        return lst


x = input("请输入待排序数列：\n")
y = re.split(' *, *| +', x)
for i in range(len(y)):
    y[i]=int(y[i])
arr = ShellSort(y)
print(y)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
