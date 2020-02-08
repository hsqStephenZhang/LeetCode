class Solution(object):
    def firstMissingPositive(self,nums):
        """
        给定一个数组，求出其第一个缺失的正整数
        时间复杂度为O(n)，空间复杂度为O(1)
        """
        """ 
        一种情况是1不在数组中，这样的话就可以直接返回1
        另一种情况是1在数组中，则需要找到从1开始的连续整数中第一个缺失的
        """
        if nums==[]: return 1
        length=len(nums)
        for i in range(length):
            while 0<nums[i]<=length and nums[i]!=nums[nums[i]-1]:
                self.swap(nums,i,nums[i]-1)
        for i in range(length):
            if i+1!=nums[i]:
                return i+1
        return length+1

    def swap(self,nums,index1,index2):
        nums[index1],nums[index2]=nums[index2],nums[index1]

if __name__ == '__main__':
    s=Solution()
    nums=[1,5,3,2,4]
    print(s.firstMissingPositive(nums))

