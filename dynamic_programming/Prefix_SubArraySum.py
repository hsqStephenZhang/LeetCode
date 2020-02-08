class Solution(object):
    def subarraySum(self, nums, k):
        """
        560.求数组中子数组之和为k的种类个数
        这一题实现O(n^2)的解答是很简单的，但是如果想要实现O(n)的复杂度，确实要动一点脑子
        这个解答是参照别人的，我一开始也想到了对每个前缀和来一次计数，但是没有采用查找
        subarrrysum的方式，导致无法操作
        而且直接用前缀和计数的字典,记录每个前缀和出现的次数,
        初始化直接令prefix={0:1}即可
        比如[-1,1,-2,2,5],k=5
        这里前缀和为5的就有两处,这时result就可以加2
        """
        result = 0
        arraysum = 0
        prefix = {0: 1}
        for elem in nums:
            arraysum += elem
            subarraysum = arraysum - k
            if subarraysum in prefix.keys():
                result += prefix[subarraysum]
            prefix[arraysum] = prefix.get(arraysum, 0) + 1
        return result


if __name__ == '__main__':
    s = Solution()
    lis = [-1, -1, 1, 0]
    k = 0
    print(s.subarraySum(lis, k))
