import sys


class SegmentTree(object):
    """
    range minimum query_minimal 的线段树,能够在logn的时间内完成在i-j范围内的最小值的查找以及更新
    """

    def __init__(self, nums):
        self.length = len(nums)
        self.tree = [0] * 2 * self.length
        for i in range(self.length, self.length * 2):
            self.tree[i] = nums[i - self.length]
        for i in range(self.length - 1, 0, -1):
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])

    def query_minimal(self, low=None, high=None, include_right=True):
        if high is None:
            high = self.length - 1
        if low is None:
            low = 0
        high = high if include_right else high - 1
        if low > high:
            raise IndexError("the low boundry is bigger than high boundry!")
        left = low + self.length
        right = high + self.length
        res = sys.maxsize
        while left <= right:
            if left % 2 == 1:
                res = min(self.tree[left], res)
                left += 1
            if right % 2 == 0:
                res = min(self.tree[right], res)
                right -= 1
            left = left >> 1
            right = right >> 1
        return res

    def update(self, i, new_val):
        if i < 0 or i >= self.length:
            raise IndexError("out of range")
        i = i + self.length
        self.tree[i] = new_val
        while i > 0:
            self.tree[i // 2] = min(self.tree[(i // 2) * 2],
                                    self.tree[(i // 2) * 2 + 1])
            i = i // 2


if __name__ == '__main__':
    nums = [4, 3, 8, 1, 6, 7]
    s = SegmentTree(nums)
    s.update(0, -8)
    print(s.query_minimal(1, 1, include_right=True))
