class Solution(object):
    """
    84.状图中最大的矩形
    给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1,
    求在该柱状图中，能够勾勒出来的矩形的最大面积。
    """

    def largestRectangleArea(self, heights):
        """
        维护一个单调栈来处理
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


if __name__ == '__main__':
    s = Solution()
    nums = [2, 1, 5, 7, 2, 2, 7, 8, 5, 6, 2, 3]
    nums2 = [2, 1, 5, 4, 2, 3]
    print(s.largestRectangleArea(nums2))
