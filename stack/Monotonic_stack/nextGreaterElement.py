class Solution(object):
    """
    496.下一个更大的元素1
    给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
    找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
    nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比
    x 大的元素。如果不存在，对应位置输出-1。
    """

    def nextGreaterElement(self, nums1, nums2):
        """
        维护一个单调递减的栈，一旦当前元素比栈顶的元素要大，说明栈顶元素的下一个
        更大的元素就是当前元素，只此一个
        """
        dic,lis=dict(),list()
        stack=[]
        for elem in nums2:
            while stack!=[] and stack[-1]<elem:
                dic[stack.pop(-1)]=elem
            stack.append(elem)
        return [dic.get(elem,-1) for elem in nums1]

if __name__ == '__main__':
    nums1=[5,4,3,2]
    nums2=[5,4,3,2,1]
    s=Solution()
    print(s.nextGreaterElement(nums1,nums2))