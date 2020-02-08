class Solution(object):
    def singleNumber(self,nums):
        ones,twos,threes=0,0,0
        for i in range(len(nums)):
            twos|=nums[i]&ones
            ones^=nums[i]
            threes=twos&ones
            ones&=~threes
            twos&=~threes
        return ones

    def singleNumber_modified(self,nums):
        ones,twos=0,0
        for i in range(len(nums)):
            ones=ones^nums[i]&~twos
            """
            1+0+0 or 0+1+0
            """
            twos=twos^nums[i]&~ones
            """
            2+0+0 or 0+1+1
            """
        return ones

# s=Solution()
# a=[-2,-2,-3,-2]
# result=s.singleNumber(a)
# print(result)

a,b,c=3,4,5
print(a^b&c)
print(a^(b&c))
