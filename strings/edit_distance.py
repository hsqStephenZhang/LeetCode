import numpy as np
# 将包导入LeetCode中会慢很多

class Solution(object):
    """
    72.编辑将一个单词转换为另一个单词所需要的最少的最少操作数
    有效的操作是:
    1.插入一个字符
    2.删除一个字符
    3.添加一个字符
    """

    def minDistance(self, word1, word2):
        """
        动态规划的算法,这里先采用状态转移表格的方法
        Tips: Leetcode导入numpy包太慢了，所以还是使用内置的list比较快
        """
        len1 = len(word1)
        len2 = len(word2)
        if len1==0: return len2
        if len2==0: return len1
        states = [[0]*len2 for i in range(len1)]
        for j in range(len2):
            if word1[0] == word2[j]:
                states[0][j] = j
            elif j != 0:
                states[0][ j] = states[0][j - 1] + 1
            else:
                states[0][ 0] = 1
        for i in range(len1):
            if word1[i] == word2[0]:
                states[i][ 0] = i
            elif i != 0:
                states[i][ 0] = states[i - 1][ 0] + 1
            else:
                states[0][ 0] = 1
        for i in range(1, len1):
            for j in range(1, len2):
                if word1[i] == word2[j]:
                    states[i][ j] = min(states[i - 1][ j - 1],
                                       states[i - 1][ j] + 1, states[i][ j - 1] + 1)
                else:
                    states[i][ j] = min(
                        states[i - 1][ j - 1] + 1, states[i - 1][ j] + 1, states[i][ j - 1] + 1)
        return states[len1-1][len2-1]


if __name__ == '__main__':
    s = Solution()
    word1 = "horse"
    word2 = "ros"
    print(s.minDistance(word1, word2))
