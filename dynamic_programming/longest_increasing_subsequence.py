"""
给定一个数组，求其中的最长的递增子序列
"""
import sys


class Solution(object):
    def lengthOfLIS(self, lis):
        """
        可以换一种思路，对于同样长度的子序列，其末尾的数字越小越好，
        因此，可以记录对于长度为i+1的子序列，其末尾的最小值，这样有个好处，那就是更新
        的时候可以使用二分查找的方式,总的时间复杂度为O(n*logn)
        即d[i+1]=长度为i的子序列的末尾的最小值
        """
        """ 
        二分查找其实也就是二分修改，维护一个数组，该数组是递增有序的，每次新加入一个元素，
        如果大于当前长度下的最大元素，就加入到当前长度的之后一位，否则在原数组中二分查找，
        如果可以更新那么就更新该元素
        """
        if not lis:
            return 0
        length = len(lis)
        dp = [sys.maxsize] * (length + 1)
        dp[1] = lis[0]
        for cur in lis[1:]:
            Solution.binary_search(1, length, dp, cur)
        for i in range(1, length + 1):
            if i == length or dp[i + 1] == sys.maxsize:
                return i

    @staticmethod
    def binary_search(low, high, dp, cur):
        while low <= high:
            mid = low + (high - low) // 2
            if dp[mid] > cur and (mid == 1 or dp[mid - 1] < cur):
                dp[mid] = cur
                return
            elif dp[mid] <= cur:
                low = mid + 1
            else:
                high = mid - 1

    def solution1(self, lis):
        """
        典型的动态规划的问题，
        普通的动态规划的复杂度是O(n^2)
        d[i]=以第i个数为末尾的最长递增子序列的长度
        """
        length = len(lis)
        d = [1] * length
        maxlength = 0
        for i in range(length):
            for j in range(i):
                if lis[j] < lis[i]:
                    d[i] = max(d[i], d[j] + 1)
            maxlength = max(maxlength, d[i])
        return maxlength


if __name__ == '__main__':
    s = Solution()
    nums = [10, 9, 2, 5, 3, 7, 200, 18, 101, 102, 103]
    print(s.solution1(nums))
    print(s.lengthOfLIS(nums))
