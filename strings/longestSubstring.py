class Solution(object):
    """
    395.给定一个字符串和数字K,找到给定字符串(由小写字符组成)中的最长子串 T,
    要求T中的每一字符出现次数都不少于k,输出 T的长度
    """
    import functools

    @functools.lru_cache()
    def longestSubstring(self, s, k):
        """
        滑动窗口的问题
        """
        if not s:
            return 0
        for c in set(s):
            if s.count(c)<k:
                # 要善于运用Python中的函数
                return max(self.longestSubstring(s1,k) for s1 in s.split(c))
        return len(s)


if __name__ == '__main__':
    s=Solution()
    strings="abababccccb"
    k=3
    print(s.longestSubstring(strings,k))