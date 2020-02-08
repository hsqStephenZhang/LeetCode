class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack,hash=list(),dict()
        for i in nums2:
            while len(stack)!=0 and stack[-1]<i:
                hash[stack[-1]]=i
                stack.pop()
            stack.append(i)
        return [hash.get(i,-1) for i in nums1]

if __name__ == '__main__':
    nums1=[1,2,4]
    nums2=[1,2,5,3,4]
    s=Solution()
    print(s.nextGreaterElement(nums1,nums2))
