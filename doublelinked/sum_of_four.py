class Solution:
    def fourSum(self, nums, target):
        length = len(nums)
        if not nums or length < 4:
            return []
        nums.sort()
        res = []
        for i in range(length - 3):
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[-3] + nums[-2] + nums[-1] < target:
                continue
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if nums[j] + nums[j + 1] + nums[j + 2] + nums[i] > target:
                    break
                if nums[i] + nums[j] + nums[-2] + nums[-1] < target:
                    continue
                if j - i > 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = length - 1
                while(left < right):
                    tmp = nums[i] + nums[j] + nums[left] + nums[right]
                    if (tmp == target):
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while (left < right and nums[left] == nums[left + 1]):
                            left = left + 1
                        while(left < right and nums[right] == nums[right - 1]):
                            right = right - 1
                        left = left + 1
                        right = right - 1
                    elif tmp < target:
                        left = left + 1
                    else:
                        right = right - 1
        return res


class Solution2:
    def fourSum(self, nums, target):
        n = len(nums)
        if(not nums or n < 4):
            return []
        nums.sort()
        res = []
        for i in range(n - 3):
            if(nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target):
                break
            if(nums[i] + nums[-1] + nums[-2] + nums[-3] < target):
                continue
            if(i > 0 and nums[i] == nums[i - 1]):
                continue
            for j in range(i + 1, n - 2):
                if(nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target):
                    break
                if(nums[i] + nums[j] + nums[-1] + nums[-2] < target):
                    continue
                if(j - i > 1 and nums[j] == nums[j - 1]):
                    continue
                L = j + 1
                R = n - 1
                while(L < R):
                    if(nums[i] + nums[j] + nums[L] + nums[R] == target):
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        while(L < R and nums[L] == nums[L + 1]):
                            L = L + 1
                        while(L < R and nums[R] == nums[R - 1]):
                            R = R - 1
                        L = L + 1
                        R = R - 1
                    elif(nums[i] + nums[j] + nums[L] + nums[R] > target):
                        R = R - 1
                    else:
                        L = L + 1
        return res


nums = [1, 0, -1, 0, -2, 2]
s = Solution()
print(s.fourSum(nums, target=0))
