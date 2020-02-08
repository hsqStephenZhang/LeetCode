class Solution(object):
    """
    214.最短回文串
    给定一个字符串 s,你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串
    """
    """
    普通的方法就是分别以每个单个的字符或者相邻的字符为中心扩展，时间复杂度为O(n^2)
    """

    def shortestPalindrome(self, s):
        """
        先逆序，然后分别从逆序的字符串的第i个字符开始，与正序的字符串的前...个字符比较，若相等，则返回
        此时的首尾加上重叠部分的长度，如:
           abca
        acba
        """
        """ 
        字符串中常用的就是将字符串翻转，尤其是在回文串的题目中 
        """
        if s=="": return ""
        rev = s[::-1]
        length = len(s)
        for j in range(length):
            if rev[j:] == s[:length - j]:
                return rev[:j] + s


if __name__ == '__main__':
    s = Solution()
    strings = "adcb"
    print(s.shortestPalindrome(strings))
