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
    def reverseKGroup(self, head, k):
        length = 0
        node = head
        while node:
            length += 1
            if length >= k:
                break
            node = node.next
        if length < k:
            return head
        pre = None
        cur = head
        for i in range(k):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        head.next = self.reverseKGroup(cur, k)

        return pre


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6]
    a = initiate(l)
    s = Solution()
    result = s.reverseKGroup(a, k=2)
    while (result is not None):
        print(result.val, end=" ")
        result = result.next
