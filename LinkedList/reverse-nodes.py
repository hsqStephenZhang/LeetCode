class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        tmphead = ListNode(-1)
        while head:
            tmphead.next, head.next, head = head, tmphead.next, head.next
        return tmphead.next


if __name__ == '__main__':
    a = [6, 4, 5, 3, 2, 1]
    head = ListNode(a[0])
    insert = head
    for i in a[1:]:
        elem = ListNode(i)
        insert.next = elem
        insert = elem

    insert = head
    s = Solution()
    result = s.reverseList(insert)
    while (result is not None):
        print(result.val)
        result = result.next
