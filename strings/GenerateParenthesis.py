class Solution(object):
    """
    22.给定一个数字，生成所有可能的并且有效的括号组合。
    """

    def generateParenthesis(self, n):
        """
        根据括号的特性:对于任意一个位置，其左边'('的数目 一定多于 ')'的数目
        """
        if n == 0:
            return None
        res = [[None] for _ in range(n + 1)]
        res[0] = [None]
        res[1] = "()"
        for i in range(2, n + 1):
            cur = []
            for j in range(i):
                left = res[j] # 长度为j的一组字符串，而不是一个字符串
                right = res[i - 1 - j]
                for k1 in left:
                    for k2 in right:
                        if k1 is None:
                            k1 = ""
                        if k2 is None:
                            k2 = ""
                        cur.append('(' + k1 + ')' + k2)
                res[i] = cur
        return res[n]


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
