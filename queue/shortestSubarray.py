from collections import deque


class Solution(object):
    """
    862.和至少为k的最短子数组
    返回 A 的最短的非空连续子数组的长度，该子数组的和至少为K
    如果没有和至少为 K 的非空子数组，返回 -1
    """

    def shortestSubarray(self, nums, K):
        """
        这个题目普通来写的时间复杂度为O(n^2)
        这里维护了一个单调双端队列，能十分方便地在两顿插入和删除
        最重要的一点就是如果已经找出一对(x,y)满足prefix[y]-prefix[x]>=K
        则对于之后的所有的y',y'-x>y-x,所以此时x已经不需要再被考虑了，也就是可以向后
        找x了
        之所以要使得这个队列是单调的，一个原因就是假如现在的prefix[y]变成了之后的prefix[x]
        那么后入队的一定比先入队的被减数要大，这样长度也更小
        """
        length = len(nums)
        prefix = [0] * (length + 1)
        sum = 0
        for i in range(length):
            sum += nums[i]
            prefix[i + 1] = sum
        ans = length + 1
        monoq = deque()
        for y, Py in enumerate(prefix):
            while monoq and prefix[monoq[-1]] >= Py:
                monoq.pop()
            while monoq and prefix[y] - prefix[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())
            monoq.append(y)
        if ans < length + 1:
            return ans
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    nums = [2, -1, 2]
    print(s.shortestSubarray(nums, 3))
