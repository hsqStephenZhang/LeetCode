class Solution(object):
    """
    115.给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。
    """

    def numDistinct(self, s, t):
        """
        典型的动态规划的问题
        dp[i][j]表示到第i个字符，匹配到模式串的第j个字符的总的数目
        当s[i]==p[j]的时候，dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        当s[i]!=p[j]的时候，dp[i][j]=dp[i-1][j]
        """
        len1 = len(s)
        len2 = len(t)
        if len1==0: return 0
        dp = [[0] * len2 for i in range(len1)]
        if s[0] == t[0]:
            dp[0][0] = 1
        for i in range(1,len1):  # 初始化dp表的第一行和第一列
            if s[i] == t[0]:
                dp[i][0] = dp[i - 1][0] + 1
            else:
                dp[i][0] = dp[i - 1][0]
        for i in range(1, len1):
            for j in range(1, len2):
                if s[i] == t[j]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp


if __name__ == '__main__':
    s = Solution()
    S = "b"
    T = "b"
    result = s.numDistinct(S, T)
    for row in result:
        print(row)
