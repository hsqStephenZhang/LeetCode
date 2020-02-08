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
    def addTwoNumbers1(self, l1:ListNode,l2:ListNode):
        if l1==None : return l2
        if l2==None : return l1
        p,q=l1,l2
        length1,length2=0,0
        while p:
            length1+=1
            p=p.next
        while q:
            length2+=1
            q=q.next
        stack=[0]
        count=0
        while count<length1-length2:
            stack.append(l1.val)
            l1=l1.next
            count+=1
        while count<length2-length1:
            stack.append(l2.val)
            l2=l2.next
            count+=1
        while l1:
            stack.append(l1.val+l2.val)
            l1=l1.next
            l2=l2.next
        head=ListNode(-1)
        carry=0
        while len(stack)>1:
            number=stack.pop()
            insert=ListNode((number+carry)%10)
            insert.next=head.next
            head.next=insert
            carry=(number+carry)//10
        if carry==1:
            head.val=1
            return head
        else: return head.next
    #正常写法，使用了栈来逐位相加

    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def calNum(head):
            """
            :param head: ListNode
            :return: int
            """
            res = 0
            while head is not None:
                res = res * 10 + head.val
                head = head.next
            return res

        num1 = calNum(l1)
        num2 = calNum(l2)
        num = str(num2 + num1)
        root = ListNode(int(num[0]))
        head = root
        for i in num[1:]:
            head.next = ListNode(int(i))
            head = head.next
        return root

if __name__ == '__main__':
    c = [0]
    d = [1,2,3,4,5]
    l1=initiate(c)
    l2=initiate(d)
    s=Solution()
    result=s.addTwoNumbers2(l1,l2)
    while result:
        print(result.val)
        result=result.next
