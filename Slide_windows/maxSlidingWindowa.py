class Solution(object):
    """
    239.滑动窗口最大值
    给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
    你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
    返回滑动窗口中的最大值。
    请在线性时间内完成该问题
    """

    def maxSlidingWindow(self, nums, k):
        """
        使用一个单调栈来控制，因为每次滑动窗口移动了之后，要么是当前的元素，要么是单调栈
        中的元素，所以不需要担心res中的元素不是滑动窗口的最大值
        """
        if not nums:
            return []
        res, stack = [], []
        for i in range(len(nums)):
            while stack != [] and nums[stack[-1]] < nums[i]:
                stack.pop(-1)
            stack.append(i)
            if i - stack[0] >= k: # 已经超过了滑动窗口的左边范围了
                stack.pop(0)
            if i > k - 2: # 数组一开始的一段特殊处理
                res.append(nums[stack[0]])
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    print(s.maxSlidingWindow(nums, 3))
