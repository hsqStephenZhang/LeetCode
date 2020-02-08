import heapq

""" 
Python中heapq实现了堆的具体操作，具体方法有:
'heapify':堆化一个可迭代序列
'heappop':弹出堆顶的最小的元素
'heappush': 将一个元素添加到堆里面
'heapreplace':删除最小的元素并且加入一个新的元素
'merge':合并多个堆
'nlargest':取出n个最大的元素
'nsmallest':取出n个最大的元素
"""


def show():
    nums1 = [4, 3, 2, 1, 6, 5, 7]
    nums2 = [0, 9, 8]
    heapq.heapify(nums1)
    print(nums1)
    merged=list(heapq.merge(nums1,nums2))
    print(merged)
    # print(dir(heapq))


def heapsort(nums,reverse=False):
    heapq.heapify(nums)
    res = [heapq.heappop(nums) for i in range(len(nums))]
    if reverse:
        return res[::-1]
    else:
        return res


if __name__ == '__main__':
    show()
    heapsort([3, 2, 1, 4, 6, 5])
