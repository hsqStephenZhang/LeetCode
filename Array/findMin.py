class Solution(object):
    """
    153.寻找旋转排序数组中的最小值
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    (例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2])。
    请找出其中最小的元素。你可以假设数组中不存在重复元素。
    """

    def findMin(self, nums):
        """
        没有重复元素的情况还是比较简单的
        """
        low, high = 0, len(nums) - 1
        if high < 0:
            return 0
        if nums[-1] > nums[0]:
            return nums[0]
        while low < high:
            mid = (low + high) // 2
            if low > 0 and nums[low] < nums[low - 1]:
                return nums[low]
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] < nums[low]:
                high = mid - 1
            else:
                low = mid + 1
        return nums[low]


if __name__ == '__main__':
    s = Solution()
    nums1 = [4, 5, 6, 7, -2,-1,0, 1, 2]
    nums2 = [5, 1, 2,]
    nums3 = [8, 9, 11, 12, 13, 15, 2, 3, 4]
    print(s.findMin(nums1))
    print(s.findMin(nums2))
    print(s.findMin(nums3))
