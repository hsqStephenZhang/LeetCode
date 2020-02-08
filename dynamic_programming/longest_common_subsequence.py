class Solution(object):
    def __init__(self):
        self.n = 0
        self.m = 0

    def longestCommonSubsequence(self, text1, text2):
        """
        通过定义一个转移table，找到转移关系，从而递推求解
        使用DP table的好处就是可以迅速找到转移方程
        """
        self.n = len(text1)
        self.m = len(text2)
        memo = [[0 for j in range(self.m)] for i in range(self.n)]
        for i in range(self.m):  # 初始化第一行(其实可以省略)
            if text2[i] == text1[0]:
                memo[0][i] = 1
            elif i != 0:
                memo[0][i] = memo[0][i - 1]
            else:
                memo[0][i] = 0
        for i in range(self.n):  # 初始化第一列
            if text1[i] == text2[0]:
                memo[i][0] = 1
            elif i != 0:
                memo[i][0] = memo[i - 1][0]
            else:
                memo[i][0] = 0
        for i in range(1, self.n):
            for j in range(1, self.m):
                if text1[i] == text2[j]:
                    memo[i][j] = 1 + memo[i - 1][j - 1]
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i]
                                     [j - 1], memo[i - 1][j - 1])
        return memo[self.n - 1][self.m - 1]


if __name__ == '__main__':
    str1 = "abcdeh"
    str2 = "agcgeh"
    s = Solution()
    print(s.longestCommonSubsequence(str1, str2))
