class Solution(object):

    def longestValidParentheses(self, s):
        """
        本题有一个需要注意的地方，就是'(',')'其实是一样的，所以需要分别正序和逆序求一遍最长括号长度
        """
        return max(self.longest_from_left(s),self.longest_from_right(s))

    def longest_from_left(self, s):
        length = len(s)
        if length <= 1:
            return 0
        cur = 0
        while cur < length - 1 and (s[cur] != '(' or s[cur + 1] != ')'):
            cur += 1
        if cur >= length - 1:
            return 0
        max_left,max_right=0,0
        maxes=[]
        while cur < length:
            while cur < length - 1 and (s[cur] != '(' or s[cur + 1] != ')'): # 先找到第一处可以扩展的地方
                cur += 1
            if cur >= length - 1:
                return max_right - max_left + 1
            else:
                left = cur
                right = cur + 1
                while left - 1 >= 0 and right + \
                        1 < length and s[left-1] == '(' and s[right+1] == ')':
                    left -= 1
                    right += 1
                if max_left==0 and max_right==0:
                    max_left,max_right=left,right
                maxes.append([left,right]) # 由该处扩展到最大范围，并添加到maxes列表中
                while True:
                    if len(maxes)>1 and maxes[-2][1]==maxes[-1][0]-1:
                        maxes[-2][1]=maxes[-1][1]
                        maxes.pop(-1)
                        while maxes[-1][0] - 1 >= 0 and maxes[-1][1] + \
                                1 < length and s[maxes[-1][0]-1] == '(' and s[maxes[-1][1]+1] == ')':
                            maxes[-1][0] -= 1
                            maxes[-1][1] += 1
                    else:
                        if  maxes[-1][1] - maxes[-1][0] >= max_right - max_left:
                            max_left, max_right = maxes[-1][0], maxes[-1][1]
                        break
                cur = right + 1
        return max_right - max_left + 1

    def longest_from_right(self, s):
        s=s[::-1]
        length = len(s)
        if length <= 1:
            return 0
        cur = 0
        while cur < length - 1 and (s[cur] != ')' or s[cur + 1] != '('):
            cur += 1
        if cur >= length - 1:
            return 0
        max_left,max_right=0,0
        maxes=[]
        while cur < length:
            while cur < length - 1 and (s[cur] != ')' or s[cur + 1] != '('): # 先找到第一处可以扩展的地方
                cur += 1
            if cur >= length - 1:
                return max_right - max_left + 1
            else:
                left = cur
                right = cur + 1
                while left - 1 >= 0 and right + \
                        1 < length and s[left-1] == ')' and s[right+1] == '(':
                    left -= 1
                    right += 1
                if max_left==0 and max_right==0:
                    max_left,max_right=left,right
                maxes.append([left,right]) # 由该处扩展到最大范围，并添加到maxes列表中
                while True:
                    if len(maxes)>1 and maxes[-2][1]==maxes[-1][0]-1:
                        maxes[-2][1]=maxes[-1][1]
                        maxes.pop(-1)
                        while maxes[-1][0] - 1 >= 0 and maxes[-1][1] + \
                                1 < length and s[maxes[-1][0]-1] == ')' and s[maxes[-1][1]+1] == '(':
                            maxes[-1][0] -= 1
                            maxes[-1][1] += 1
                    else:
                        if  maxes[-1][1] - maxes[-1][0] >= max_right - max_left:
                            max_left, max_right = maxes[-1][0], maxes[-1][1]
                        break
                cur = right + 1
        return max_right - max_left + 1


if __name__ == '__main__':
    s = Solution()
    strings = "(((()"
    # print(len(strings))
    print(s.longest_from_left(strings))
    print(s.longestValidParentheses(strings))
