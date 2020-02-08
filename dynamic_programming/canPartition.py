class Solution(object):
    """
    416.分割等和子集问题
    给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集,
    使得两个子集的元素和相等。
    返回True或者False
    """
    """
    注意到，这里的dp[i][j]仅仅依赖前一行的值，所以不需要那么大的存储空间，只需要一维即可
    但是为了防止和当前行冲突，需要两行，一行是pre,一行是cur 
    """

    def canPartition(self, nums):
        sum_of_nums = sum(nums)
        if sum_of_nums % 2 == 1:
            return False
        length = len(nums)
        if length <= 1:
            return False
        half_sum = sum_of_nums // 2
        dp = [[False for _ in range(1 + half_sum)] for k in range(2)]
        dp[0][0], dp[1][0] = True, True
        for i in range(1, length + 1):
            for j in range(1, half_sum + 1):
                if j >= nums[i - 1]:
                    dp[i %
                       2][j] = dp[(i + 1) %
                                  2][j] | dp[(i + 1) %
                                             2][j - nums[i - 1]]
                else:
                    dp[i % 2][j] = dp[(i + 1) % 2][j]
        return dp[length % 2][half_sum]

    def canPartition2(self, nums):
        """
        转换为01背包问题，也就是求是否存在前i个数，使得其中一部分数的和为sum/2
        dp[i][j]表示前i个数是否存在一部分的和，使得其等于j,
        这个问题又可以分为dp[i][j]=dp[i-1][j]或者dp[i][j]=dp[i-1][j-nums[i-1]]
        """
        """
        注意到，这里的dp[i][j]仅仅依赖前一行的值，所以不需要那么大的存储空间，只需要一维即可
        """
        sum_of_nums = sum(nums)
        if sum_of_nums % 2 == 1:
            return False
        length = len(nums)
        if length <= 1:
            return False
        half_sum = sum_of_nums // 2
        dp = [[False for j in range(half_sum + 1)]
              for i in range(length + 1)]
        for k in range(1, length):
            dp[k][0] = True
        for i in range(1, length + 1):
            for j in range(1, half_sum + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[length][half_sum]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 5, 4, 10]
    print(s.canPartition(nums))
