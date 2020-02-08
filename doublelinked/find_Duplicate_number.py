class Solution:
    def findDuplicate(self, nums):
        fast,slow=0,0
        while True:
            fast=nums[nums[fast]]
            slow=nums[slow]
            if fast==slow:
                break
        finder=0
        while True:
            finder = nums[finder]
            slow = nums[slow]
            if finder==slow:
                break
        return slow

"""
使用快慢指针，列表中的每个元素都可以看成一个链表的结点，结点值为其序号，
结点的指针域为其值
"""


a=[1,2,4,3,2]
s=Solution()
print(s.findDuplicate(a))