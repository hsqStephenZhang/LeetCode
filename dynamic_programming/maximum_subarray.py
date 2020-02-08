class Solution(object):
    """
    最长的子序列之和
    """

    def maxSubArray(self, lis):
        start, all = lis[-1], lis[-1]
        length = len(lis)
        i = length - 2
        while i >= 0:
            start = max(lis[i], start + lis[i])
            all = max(all, start)
            i -= 1
        return all
