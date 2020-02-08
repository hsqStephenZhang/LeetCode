"""
找到一个排序数组中第一个大于等于给定元素的位置
"""
""" 
high=mid or high=mid-1
low=mid or low=mid+1
这四者需要针对要求好好地考虑
"""

import bisect


class Solution(object):
    def solution1(self, nums, val):
        low, high = -1, len(nums)  # 初始化的值可以是不在数组的下标范围内的
        while high > low:
            # 这里是一种写法，还有一种，假如函数里面的low=high的话，
            # 为了避免死循环，需要将判断条件改为high-low>1
            mid = low + (high - low) // 2
            if nums[mid] >= val:
                high = mid
            else:
                low = mid + 1  # mid这个值肯定是不满足的
        return high

    def solution2(self, nums, val):
        index = bisect.bisect_left(nums, val)
        return index


if __name__ == '__main__':
    s = Solution()
    nums = [4, 4, 6]
    print(s.solution1(nums, 4))
    print(s.solution2(nums, 4))
