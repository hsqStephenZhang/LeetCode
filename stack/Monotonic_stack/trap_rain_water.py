class Solution(object):
    """
    42.给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
    """

    def trap(self, height):
        """
        单调栈问题
        """
        stack = []
        sum_of_rain = 0
        length = len(height)
        for i in range(length):
            while stack != [] and height[stack[-1]] < height[i]:
                cur = stack.pop(-1)
                if stack:
                    sum_of_rain += (i - stack[-1]-1) * \
                        (min(height[stack[-1]], height[i]) - height[cur])
            stack.append(i)
        return sum_of_rain


if __name__ == '__main__':
    s = Solution()
    height = [0, 2, 0, 2, 1, 0, 1, 3, 2, 6, 5, 0, 1, 2, 1]
    print(s.trap(height))
