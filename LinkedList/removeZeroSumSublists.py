class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def initiate(lis, withhead=False):
    if withhead:
        head = ListNode(None)
        insert = head
        for i in lis:
            elem = ListNode(i)
            insert.next = elem
            insert = elem
        return head
    else:
        head = ListNode(lis[0])
        insert = head
        for i in lis[1:]:
            elem = ListNode(i)
            insert.next = elem
            insert = elem
        return head

class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        大佬的解决思路：先遍历一遍求出前缀和，并构造对应的map，刚好有重复的前缀和时会
        保留最后的一个前缀和对应的结点，此时再遍历一遍，将前缀和与dict中保存的前缀和对应
        的结点比较即可
        """
        if head is None: return head
        newhead=ListNode(0)
        newhead.next=head
        p=newhead
        sum=0
        pres={}
        while p:
            sum+=p.val
            pres[sum]=p
            p=p.next
        p=newhead
        sum=0
        while p:
            sum+=p.val
            p.next=pres[sum].next
            p=p.next
        return newhead.next

    def removeZeroSumSublists2(self, head):
        """
        暴力法直接求是否存在i,j，他们之间的元素之和为0
        """
        if head is None:
            return head
        newhead = ListNode(None)
        newhead.next = head
        prehead = newhead
        while prehead.next:
            sum = 0
            cur = prehead.next
            while cur:
                sum += cur.val
                if sum == 0:
                    prehead.next = cur.next
                    if prehead.next is None:
                        return newhead.next
                cur = cur.next
            prehead = prehead.next
        return newhead.next



if __name__ == '__main__':
    l = [1,2,-2,-1,3]
    a = initiate(l)
    s = Solution()
    result = s.removeZeroSumSublists2(a)
    while (result is not None):
        print(result.val, end=" ")
        result = result.next
