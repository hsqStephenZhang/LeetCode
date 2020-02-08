from binary_indexed_tree import BIT
import sys


class Reversed_pairs(BIT):
    def __init__(self, nums):
        self.data = nums
        self.count = [0] * len(nums)
        super(Reversed_pairs, self).__init__(self.count)

    def countreverse(self):
        res = 0
        for i in range(self.length):
            max_index = -1
            max_val = -sys.maxsize
            for j in range(self.length):
                if self.count[j] != 1 and self.data[j] > max_val:
                    max_index = j
                    max_val = self.data[j]
            self.count[max_index] = 1
            self.update(max_index + 1, 1)  # update的序号从1开始
            res = res + self.getsum(max_index)  # 每次统计的复杂度都是logn
        return res


if __name__ == '__main__':
    lis = [3, 2, 1, 0, 5, 3.5]  # 这里没有对重复元素处理(可以将重复元素视为逆序对)
    s = Reversed_pairs(lis)
    print(s.countreverse())
