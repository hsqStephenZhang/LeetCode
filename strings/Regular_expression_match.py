class Solution(object):
    """
    10.正则表导师匹配问题
    给你一个字符串 s 和一个字符规律 p，实现一个支持 '.' 和 '*' 的正则表达式匹配
    '.' 匹配任意单个字符
    '*' 匹配零个或多个前面的那一个元素
    """
    """
    declaration:
    s 可能为空，且只包含从 a-z 的小写字母。
    p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
    """
    """
    尤其要注意的是 a.b*这种匹配字符,以及匹配次数的问题
    """

    def __init__(self, p):
        self.matches, self.flag = self.getmatches(p)

    def isMatch(self, s, p):
        """
        :type s: the str given by user
        :type p: pattern
        :rtype: bool: True or False
        """
        if p == "" and s != "":
            return False
        len1 = len(s)
        len2 = len(self.matches)
        cur, j = 0, 0
        pass

    def getmatches(self, p):
        matches = []
        flag = 0
        cur, i, length = 0, 0, len(p)
        while cur < length:
            while cur < length and p[cur] != '*':
                cur += 1
            if cur > length - 1:
                matches.append(p[i:cur + 1])
                flag = 1
            else:
                matches.append(p[i:cur])
            cur += 1
            i = cur
        return matches, flag

    def match(self, pattern, s, i, repeat=True):
        length = len(pattern)
        j = 0
        if repeat is False:
            while j < length and i + \
                    j < len(s) and (pattern[j] == s[i + j] or pattern[j] == "*"):
                j += 1
            if j == length:
                return True
            else:
                return False


if __name__ == '__main__':
    strings = "aab"
    pattern = "c*a*b*"
    s = Solution(pattern)
    print(s.isMatch(strings, pattern))
    print(s.getmatches(pattern))
