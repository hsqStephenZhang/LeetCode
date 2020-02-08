class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        if head is None or head.next is None:
            return head
        #插入头结点，之后返回头结点的指针域
        tmphead=ListNode(-1)
        tmphead.next=head
        cur =  head
        while  cur.next is not None:
            if cur.next.val>= cur.val:
                cur=cur.next
            else :
                insert = cur.next
                pre=tmphead
                while pre.next is not None and pre.next.val < insert.val:
                    pre = pre.next
                prenext=pre.next
                cur.next = insert.next
                pre.next=insert
                insert.next=prenext

        return tmphead.next


if __name__ == '__main__':
    a = [6, 4, 5, 3, 2,8 ,9 ,1,-1]
    head = ListNode(a[0])
    insert = head
    for i in a[1:]:
        elem = ListNode(i)
        insert.next = elem
        insert = elem

    insert = head
    s = Solution()
    result = s.insertionSortList(insert)
    while (result is not None):
        print(result.val)
        result = result.next
