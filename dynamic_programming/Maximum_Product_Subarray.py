class Solution(object):
    def maxProduct(self,nums):
        """
        给定一个整形数组，求乘积最大的连续子序列
        """
        length=len(nums)
        if length==1: return nums[0]
        max_index=0
        my_dict={}
        my_dict[0]=[nums[0],nums[0]]
        start=1
        flag=0
        while start<length:
            if nums[start]>0:
                if my_dict[start-1][0]<0:
                    my_dict[start]=[nums[start],nums[start]*my_dict[start-1][1]]
                elif my_dict[start-1][0]>0:
                    my_dict[start]=[nums[start]*my_dict[start-1][0],min(nums[start]*my_dict[start-1][1],nums[start])]
                else:
                    my_dict[start] = [nums[start], nums[start]]
            elif nums[start]<0:
                if my_dict[start - 1][1] < 0:
                    my_dict[start] = [nums[start] * my_dict[start - 1][1],min(nums[start],nums[start] * my_dict[start - 1][0])]
                elif my_dict[start - 1][1] > 0:
                    my_dict[start] = [nums[start],nums[start] * my_dict[start - 1][0]]
                else:
                    my_dict[start] = [nums[start], nums[start]]
            else:
                flag = 1
                if start==length-1:
                    break
                else:
                    start += 1
                    my_dict[start] = [nums[start], nums[start]]
            if my_dict[start][0]>my_dict[max_index][0]:
                max_index=start
            start+=1
        if flag==0:
            return my_dict[max_index][0]
        else:
            return max(my_dict[max_index][0],0)


if __name__ == '__main__':
    s=Solution()
    nums1=[2,3,-2,4,0,-2,-3,-2,-3]
    nums2=[2,3,-2,-10,9,0,4,5,6]
    nums3=[0,2]
    print(s.maxProduct(nums1))
    print(s.maxProduct(nums2))
    print(s.maxProduct(nums3))

