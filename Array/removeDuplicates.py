class Solution(object):
    """
    80.删除排序数组中的重复项，每个数字的重复次数不能超过2次
    """

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 0
        for elem in nums:
            if length < 2 or nums[length - 2] != elem:
                nums[length] = elem
                length += 1
        return length


if __name__ == '__main__':
    s = Solution()
    nums = sorted([1, 4, 5, 3, 5, 6, 7, 1, 3])
    length = s.removeDuplicates(nums)
    print(nums[:length])
