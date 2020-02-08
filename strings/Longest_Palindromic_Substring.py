class Solution(object):
    """
    5.求一个字符串中的最长的回文子串
    """

    def judge(self, s, left, right):
        """
        当left=right时，就是奇数回文串
        当left+1=right时，就是偶数回文串
        """

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    def longestPalindrome(self, s):
        if s[::-1] == s:
            return s
        res = s[:1]
        for i in range(len(s)):
            palindrome_odd = self.judge(s, i, i)
            palindrome_even = self.judge(s, i, i + 1)
            res = max(palindrome_even, palindrome_odd, res, key=len)
        return res

    def longestPalindrome2(self, s):
        """
        DP 问题，可以找到递推关系式:
        每次只需要记录遍历到第n-1个字符的时候，以第n-1个字符结尾的最长的回文子串长度
        和在前n-1个字符的中间的最长的回文子串的长度
        """
        length = len(s)
        if length == 0:
            return ""
        if length == 1:
            return s
        if s[0] != s[1]:
            all = [0, 0]
            end = [0, 0]
            cur = 1
        else:
            all = [0, 1]
            end = [0, 1]
            cur = 2
        while cur < length:
            if end[0] - 1 >= 0:
                sub_start = end[0] - 1
                sub_end = cur
                while True:
                    while s[sub_start] != s[sub_end]:
                        sub_start += 1
                    if sub_start == sub_end:
                        end = [cur, cur]
                        break
                    else:
                        tmp_start, tmp_end = sub_start, sub_end
                        while tmp_start < tmp_end and s[tmp_start] == s[tmp_end]:
                            tmp_start += 1
                            tmp_end -= 1
                        if tmp_start >= tmp_end:
                            end = [sub_start, sub_end]
                            if end[1] - end[0] >= all[1] - all[0]:
                                all[0], all[1] = end[0], end[1]
                            break
                        else:
                            sub_start += 1
            else:  # 前面的从头到尾都是回文子串
                sub_start = 0
                sub_end = cur
                while True:
                    while s[sub_start] != s[sub_end]:
                        sub_start += 1
                    if sub_start == sub_end:
                        end = [cur, cur]
                        break
                    else:
                        tmp_start, tmp_end = sub_start, sub_end
                        while tmp_start < tmp_end and s[tmp_start] == s[tmp_end]:
                            tmp_start += 1
                            tmp_end -= 1
                        if tmp_start >= tmp_end:
                            end = [sub_start, sub_end]
                            if end[1] - end[0] >= all[1] - all[0]:
                                all[0], all[1] = end[0], end[1]
                            break
                        else:
                            sub_start += 1

            cur += 1
        return s[all[0]:all[1] + 1]


if __name__ == '__main__':
    s = Solution()
    strings = "efefefefefhh"
    strings2 = "bbb"
    print(s.longestPalindrome(strings))
    print(s.longestPalindrome2(strings))
