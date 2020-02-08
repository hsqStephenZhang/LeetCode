class Solution(object):
    def longestConsecutive(self, nums):
        """
        仿照第二种方法，但是存储的是从一个数开始的和从一个数结束的最长的子序列长度
        what?凭什么?为什么O(n*logn)的算法时间还要短?为什么还可以用set?
        """
        if len(nums) == 0:
            return len(nums)
        dic = dict()
        maxlength = 1
        for i in nums:
            if i not in dic.keys():
                if i - 1 not in dic.keys() and i + 1 not in dic.keys():
                    dic[i] = 1
                elif i - 1 in dic.keys() and i + 1 in dic.keys():
                    maxlength = max(maxlength,
                                    dic[i - 1] + dic[i + 1]+ 1)
                    dic[i - dic[i - 1]] = dic[i - 1] + dic[i + 1] + 1
                    dic[i + dic[i + 1]] = dic[i - 1] + dic[i + 1] + 1
                    dic[i]=1
                elif i - 1 in dic.keys() and i + 1 not in dic.keys():
                    maxlength = max(maxlength, dic[i - 1] + 1)
                    dic[i] = dic[i - 1] + 1
                    dic[i - dic[i - 1]]= dic[i - 1] + 1
                else:
                    maxlength = max(maxlength, dic[i + 1][0] + 1)
                    dic[i] = dic[i + 1] + 1
                    dic[i + dic[i + 1]] = dic[i + 1] + 1
        return maxlength

    def longestConsecutive2(self, nums):
        """
        这是一个寻找最长连续子序列的高于O(n)的算法，因为如果数据过于密集，查找dic的过程
        将接近于O(n)的复杂度，总的复杂度将上升到O(n^2)
        """
        if len(nums) == 0:
            return len(nums)
        dic = {}
        maxlength = 1
        for i in nums:
            if i not in dic.keys():
                dic[i] = 1
                low, high = i, i
                while low in dic.keys():
                    low -= 1
                while high in dic.keys():
                    high += 1
                maxlength = max(maxlength, high - low - 1)
        return maxlength


if __name__ == '__main__':
    s = Solution()
    lis = [1,8,2,3,5,6,7,4,9,11,15]
    print(s.longestConsecutive(lis))
