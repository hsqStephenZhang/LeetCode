class Solution(object):
    """
    162.寻找一个数列中的峰值元素，可以假定一定存在该元素,且相邻两个元素一定不相等
    """

    def findPeakElement(self, nums):
        """
        根据本题的特殊要求，只需要返回一处的索引即可
        因此，可以分为2种情况，一种是先上升再下降，另一种与之对应，对于先上升
        再下降的情况，可以分析任意一个元素处于的位置，一定要么是上升区间或者
        下降区间，若为下降区间，则峰值在其左边，若为上升区间，则峰值在其右边
        """

        def solution1(left, right, nums):
            if left == right:
                return left # 返回其中一处的索引
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return solution1(left, mid, nums)
            else:
                return solution1(mid + 1, right, nums)
        return solution1(0, len(nums) - 1, nums)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 1, ]
    print(s.findPeakElement(nums))
