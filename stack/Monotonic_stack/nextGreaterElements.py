class Solution(object):
    """
    496.下一个更大的元素2
    给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），
    输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，
    这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。
    如果不存在，则输出 -1。
    """

    def nextGreaterElements(self, nums):
        """
        对于循环数组来说，最好的处理方式就是对下标取余数，这道题可以通过double数组以及对下标取余数来实现目的
        """
        stack = []
        length = len(nums)
        res=[-1]*length
        for i in range(2 * len(nums)):
            while stack != [] and nums[stack[-1]] < nums[i % length]:
                res[stack.pop(-1)] = nums[i % length]
            stack.append(i % length)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [100, 1, 11, 1, 120, 111, 123, 1, -1, -100]
    print(s.nextGreaterElements(nums))
