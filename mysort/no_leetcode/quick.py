import re
def QuickSort(lst, start, end):
    if start < end:
        i, j = start, end
        base = lst[i]
        while i < j:
            while (i < j) and (lst[j] >= base):
                j -= 1
            lst[i]=lst[j]
            while (i < j) and (lst[i] <= base):
                i += 1
            lst[i]=lst[j]
        lst[i] = base
        QuickSort(lst, start, i - 1)
        QuickSort(lst, j + 1, end)
    return lst


x = input("请输入待排序数列：\n")
y = re.split(' *, *| +', x)
for i in range(len(y)):
    y[i]=int(y[i])
arr = QuickSort(y,0,len(arr)-1)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
