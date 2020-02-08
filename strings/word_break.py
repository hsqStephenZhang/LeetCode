class Solution(object):
    """
    139.给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，
    判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
    1.拆分时可以重复使用字典中的单词。
    2.你可以假设字典中没有重复的单词。
    """

    def __init__(self):
        self.my_dict = {}

    def wordBreak(self, s, wordDict):
        """
        别人的解答，显然更加简洁
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]

    def wordBreak2(self, s, wordDict, left=0, right=0):
        """
        feasible[i]=到第i个字符之前是否有拆分的方案，初始化为0
        """
        if right in self.my_dict.keys():
            return False
        while right <= len(s) and s[left:right] not in wordDict:
            right += 1
        if right == len(s) + 1 and s[left:len(s)] not in wordDict:
            return False
        if right == len(s) and s[left:len(s)] in wordDict:
            return True
        if self.wordBreak2(s, wordDict, right, right):
            return True
        else:
            self.my_dict[right] = 1
            return self.wordBreak2(s, wordDict, left, right + 1)


if __name__ == '__main__':
    strings1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict1 = [
        "a",
        "aa",
        "aaa",
        "aaaa",
        "aaaaa",
        "aaaaaa",
        "aaaaaaa",
        "aaaaaaaa",
        "aaaaaaaaa",
        "aaaaaaaaaa"]
    s1 = Solution()
    s2 = Solution()
    strings2 = "catsanddog"
    wordDict2 = ["cats", "dog", "sand", "and", "cat"]
    print(s1.wordBreak(strings1, wordDict1))
    print(s2.wordBreak(strings2, wordDict2))
