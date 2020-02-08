class Solution(object):

    def lengthOfLongestSubstring(self, s):
        smax = 0
        length = len(s)
        if length <= 1:
            return length
        p = 0
        for end in range(1, length):
            start = p
            while start < end:
                if s[start] == s[end]:
                    p = start + 1
                    if smax < end - start:
                        smax = end - start
                    break
                start += 1
            if smax < end - p + 1:
                smax = end - p + 1
        return smax


s = Solution()
a = 'abcabcb'
print(s.lengthOfLongestSubstring(a))
