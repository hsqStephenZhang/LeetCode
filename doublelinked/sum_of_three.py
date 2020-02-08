class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        length = len(nums)
        if not nums or length < 3:
            return []
        for k in range(length):
            if nums[k]>0:
                return res
            if k>0 and nums[k]==nums[k-1]:
                continue
            left = k + 1
            right = length - 1
            while(left < right):
                tmp = nums[k] + nums[left] + nums[right]
                if (tmp == 0):
                    res.append([nums[k], nums[left], nums[right]])
                    while (left<right and nums[left] == nums[left + 1]):
                        left = left + 1
                    while(left<right and nums[right] == nums[right - 1]):
                        right = right - 1
                    left = left + 1
                    right = right - 1
                elif tmp < 0:
                    left = left + 1
                else:
                    right = right - 1
        return res


a = [-2, -1, 0, 1, 2, 3]
s = Solution()
result = s.threeSum(a)
for item in result:
    print(item, end='\n')
