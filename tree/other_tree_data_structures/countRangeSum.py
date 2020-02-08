import bisect


class Solution(object):
    """
    给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
    区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
    """
    """
    最简单的算法复杂度为O(n^2)，尝试优化算法
    """

    def countRangeSum(self, nums, lower, upper):
        """
        通过树状数组可以在logn时间内计算出部分和
        """
        length = len(nums)
        tree = self.buildTree(nums)
        count = 0
        for i in range(length):
            for j in range(i, length):
                if lower <= self.getsum(j + 1, tree) - \
                        self.getsum(i, tree) <= upper:
                    count += 1
        return count

    def buildTree(self, nums):
        """
        树状数组的公式(lowbit代表最低的二进制为1的位置):
        C[i]=A[i-lowbit(i)+1]+A[i-lowbit(i)+2]+......A[i]
        lowbit(x)=x & (-x)
        其中i-lowbit(x)=i&(i-1)
        """
        length = len(nums)
        tree = [0] * (length + 1)
        sums = [0] * (length + 1)
        for i in range(length):
            sums[i + 1] = sums[i]+nums[i]
        for i in range(1, length + 1):
            tree[i] = sums[i] - sums[i & (i - 1)]
        return tree

    def getsum(self, x, tree):
        result = 0
        while x > 0:
            result += tree[x]
            x=x&(x-1)
        return result


class Solution2(object):
    def countRangeSum(self, nums, lower, upper):
        p = [0]  # 前缀和初始化，前缀和p[x]，就是区间数组[0, x)的和
        for i in nums:
            p += [p[-1] + i]  # 前缀和计算
        ans = 0
        q = []  # 有序的前缀和队列
        for pi in p[:: -1]:  # 逆序遍历前缀和
            i, j = pi + lower, pi + upper  # 给出当前前缀和两个对应边界
            l = bisect.bisect_left(q, i)  # 二分查找
            r = bisect.bisect_right(q, j)  # 找到对应边界的在前缀和数组里的插入位置
            ans += r - l  # 序号大于自己的前缀和里有多少个前缀和在边界里面，就是以当前区间为起点，符合区间和条件的个数
            bisect.insort(q, pi)  # 二分插入更新队列
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [-2, 5, -1]
    upper, lower = 2, -2
    # print(s.countRangeSum(nums, lower, upper))