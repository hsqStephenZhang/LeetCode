import sys

class Solution(object):
    def minWindow(self, s, t):
        """
        76.最小字符串的覆盖问题
        该算法通过了，但是仍然有很大的优化空间
        这里的思路就是维护一个窗格，使得该窗格总是覆盖着target字符串的，然后通过窗格左右的
        平移来调整，最麻烦的是边界条件的判断
        """
        length1 = len(s)
        length2 = len(t)
        min_left, min_right = 0, sys.maxsize
        match = dict()
        target = dict()
        left, right = 0, 0
        for char in t:
            if char in target:
                target[char] += 1
            else:
                target[char] = 1
        match[s[0]] = 1
        if s[0] in target.keys():
            length2 -= 1
        while right  < length1-1 and length2:
            if s[right + 1] in match:
                match[s[right + 1]] += 1
                if s[right + 1] in target.keys() and match[s[right + 1]] <= target[s[right + 1]]:
                    length2 -= 1
            elif s[right + 1] in target:
                match[s[right + 1]] = 1
                if match[s[right + 1]] <= target[s[right + 1]]:
                    length2 -= 1
            right += 1
        if right==length1-1 and length2!=0: return ""
        # 假设刚好完成了匹配，也就是match[s[right]] += 1之后刚好覆盖，则s[right]是
        # 刚好覆盖的一个元素
        while right < length1:
            while left <= right:
                if s[left] in target.keys():
                    if match[s[left]] > target[s[left]]:
                        match[s[left]] -= 1
                        left += 1
                    else:
                        if right - left < min_right - min_left:
                            min_left, min_right = left, right
                        break
                else:
                    left += 1

            right += 1
            if right >= length1:
                break
            while s[right] not in target.keys() and right < length1 - 1:
                right += 1
            if right != length1:
                if s[right] in target.keys():
                    match[s[right]] += 1
        return s[min_left:min_right+1]


if __name__ == '__main__':
    s = Solution()
    strings1 = "ADOBAAFCB"
    strings2 = "ABC"
    strings11 = "aab"
    strings22 = "b"
    print(s.minWindow(strings1, strings2))
    print(s.minWindow(strings11, strings22))
