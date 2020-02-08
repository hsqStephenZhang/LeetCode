class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        if head is None or head.next is None or m == n:
            return head
        tmphead = ListNode(-1)
        tmpcur = ListNode(-1)
        tmphead.next = head
        startnode = tmphead
        for i in range(m - 1):
            startnode = startnode.next
        endnode = cur = startnode.next
        for i in range(n - m + 1):
            tmpcur.next, cur.next, cur = cur, tmpcur.next, cur.next
        startnode.next = tmpcur.next
        endnode.next = cur
        return tmphead.next

    def recurrence(self, head):
        if head is None or head.next is None:
            return head
        newhead = self.recurrence(head.next)
        head.next.next = head
        head.next = None

        return newhead


def initiate(lis,withhead=False):
    if withhead==True:
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


if __name__ == '__main__':
    a = [6, 5, 4, 3, 2, 1]
    reverse = initiate(a)
    s = Solution()
    result = s.recurrence(reverse)
    while (result is not None):
        print(result.val, end=' ')
        result = result.next
