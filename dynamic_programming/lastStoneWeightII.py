class Solution(object):
    """
    1049.最后一块石头的重量
    有一堆石头，每块石头的重量都是正整数。
    每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
    如果 x == y，那么两块石头都会被完全粉碎；
    如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
    最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。
    """

    def lastStoneWeightII(self, stones):
        """
        转换为01背包问题，背包的大小为sum/2,最大化背包的重量
        也就相当于最大化的价值=重量
        """
        half_sum = sum(stones) // 2
        dp = [0] * (half_sum + 1)
        for i in range(len(stones)):
            for j in range(half_sum,stones[i]-1,-1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        return sum(stones)-2*dp[half_sum]


if __name__ == '__main__':
    s = Solution()
    stones = [2, 7, 4, 1, 8, 1]
    print(s.lastStoneWeightII(stones))
