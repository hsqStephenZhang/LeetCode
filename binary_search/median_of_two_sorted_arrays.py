class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        找到两个有序数组的中位数,要求时间复杂度为O(log(m+n))
        """
        length1 = len(nums1)
        length2 = len(nums2)
        if length1 > length2:
            return self.findMedianSortedArrays(nums2, nums1)
        imin, imax = 0, length1
        while imin <= imax:
            i = (imin + imax) // 2
            j = (length1 + length2 + 1) // 2 - i
            if (i < imax and nums2[j - 1] > nums1[i]):
                imin = i + 1
            elif (i > imin and nums2[j] < nums1[i - 1]):
                imax = i - 1
            else:
                maxleft, minright = 0, 0
                if i == 0:
                    maxleft = nums2[j - 1]
                elif j == 0:
                    maxleft = nums1[i - 1]
                else:
                    maxleft = max(nums1[i - 1], nums2[j - 1])
                if (length2 + length1) % 2:
                    return maxleft
                if i == length1:
                    minright = nums2[j]
                elif j == length2:
                    minright = nums1[i]
                else:
                    minright = min(nums1[i], nums2[j])
                return (maxleft + minright) / 2
        return 0

    def solution2(self, nums1, nums2):
        """
        最简单粗暴的方法就是将两个数组合并，空间和时间复杂度都是O(n+m)
        """
        pass


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    merged = sorted(nums1 + nums2)
    length = len(merged)
    if length % 2:
        print(merged[length // 2])
    else:
        print((merged[length // 2 - 1] + merged[length // 2]) / 2)
    print(s.findMedianSortedArrays(nums1, nums2))
