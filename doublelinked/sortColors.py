class Solution:
    def sortColors(self, nums):
        length=len(nums)
        if length<=1:
            return nums
        left,middle,right=0,0,length-1
        while(middle<=right):
            if nums[middle]==2:
                nums[middle],nums[right]=nums[right],nums[middle]
                right-=1
            elif nums[middle]==0 :
                nums[left]=0
                if middle>left:
                    nums[middle]=1
                left+=1
                middle+=1
            else:
                middle+=1
        return nums

a=[1,2,2,1,0,0,0,1]
s=Solution()
result=s.sortColors(a)
print(result)










num=[2,0,2,1,1,0]
s=Solution()
