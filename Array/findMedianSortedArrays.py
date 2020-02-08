class Solution(object):
    """
    4.找到两个有序数组的中位数,要求时间复杂度为O(log(m+n))，可以假设nums1和nums2不同时为空
    """

    def findMedianSortedArrays(self, nums1, nums2):
        """
        这一题要使用二分查找的方法
        只需要向右排除到第(len1+len2)//2个元素即可
        考虑中位数的作用，也就是将数组分为两半，保证左边的所有的数小于右边的数,这样中位数在左边最大的数
        和右边最小的数之间产生
        """
        """
        两个数组的问题常常将一个数组的下标定下来再讨论
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)
        if len2==0:
            raise ValueError("Wrong input")
        imin, imax, halflen = 0, len1, (len1 + len2 + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = halflen - i
            if i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            elif i < len1 and nums1[i] < nums2[j - 1]:
                imin = i + 1
            else:
                if i == 0:
                    maxleft = nums2[j - 1]
                elif j == 0:
                    maxleft = nums1[i - 1]
                else:
                    maxleft = max(nums1[i - 1], nums2[j - 1])
                if (len1 + len2) % 2:
                    return maxleft
                if i == len1:
                    minright = nums2[j]
                elif j == len2:
                    minright = nums1[i]
                else:
                    minright = min(nums1[i], nums2[j])
                return (maxleft + minright) / 2


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 3,]
    nums2 = [2]
    print(s.findMedianSortedArrays(nums1, nums2))