class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        slow = head
        fast = head
        pre = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        left = head
        right = pre.next
        pre.next = None
        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

    def merge(self, left, right):
        tmp = head = ListNode(-1)
        while left and right:
            if left.val < right.val:
                tmp.next = left
                tmp = tmp.next
                left = left.next
            else:
                tmp.next = right
                tmp = tmp.next
                right = right.next
        tmp.next = left if left else right
        return head.next



if __name__ == '__main__':
    a = [4, 6, 7, 9, 8, 3, 2, 1]
    head = ListNode(a[0])
    tmp = head
    for i in a[1:]:
        elem = ListNode(i)
        tmp.next = elem
        tmp = elem

    tmp = head
    s = Solution()
    result = s.sortList(tmp)
    while (result is not None):
        print(result.val)
        result = result.next
