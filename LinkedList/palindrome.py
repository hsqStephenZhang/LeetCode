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
    def isPalindrome1(self, head):
        if head is None or head.next is None : return True
        fast,slow=head,head
        while fast:
            slow=slow.next
            if fast.next:
                fast=fast.next.next
            else: fast=fast.next
        pre=None
        while slow.next:
            tmp=slow.next
            slow.next=pre
            pre=slow
            slow=tmp
        slow.next=pre
        while slow:
            if slow.val!=head.val:
                return False
            slow=slow.next
            head=head.next
        return True

    def isPalindrome2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        return a==a[::-1]

if __name__ == '__main__':
    l = [1,]
    a = initiate(l)
    s = Solution()
    print(s.isPalindrome1(a))
