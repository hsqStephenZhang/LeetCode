class Solution(object):
    """
    85.给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积
    """

    def maximalRectangle(self, matrix):
        """
        当遍历到某一行时，可以将每一列上面的所有的1的数目看成是一个数字
        这样就转换成了第84的height数组
        """
        if matrix==[] or matrix==[[]]: return 0
        length = len(matrix)
        dp = [0] * len(matrix[0])
        maximal = 0
        for i in range(length):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[j] = dp[j] + 1
                else:
                    dp[j] = 0
            maximal = max(maximal, self.largestRectangleArea(dp))
        return maximal

    def largestRectangleArea(self, heights):
        """
        LeetCode第84题的求出最大的矩形面积
        """
        res = 0
        length = len(heights)
        if length == 0:
            return 0
        stack = [-1]
        heights.append(-1)
        for i in range(length):
            while stack != [] and heights[i] < heights[stack[-1]]:
                pre_bigger = stack.pop(-1)
                res = max(res, (i - stack[-1] - 1) * heights[pre_bigger])
            stack.append(i)
        res = max(res, length * heights[stack[0]])
        for index in range(1, len(stack)):
            res = max(
                res, (length - stack[index - 1] - 1) * heights[stack[index]])
        return res
