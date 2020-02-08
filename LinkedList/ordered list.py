class Lnode(object):
    def __init__(self, elem=None, nextnode=None):
        self.elem = elem
        self.nextnode = nextnode


class Head(object):
    def __init__(self):
        self.head = None


def initializelist(head, lis):
    end = Lnode(lis)
    head.head = end
    for i in lis:
        curnode = Lnode(i)
        end.nextnode = curnode
        end = curnode
    return head


def printllist(head):
    node = head.head
    while node is not None:
        if node.elem is not None:
            print(node.elem)
        node = node.nextnode


def delelem(head, value):
    cur = head.head
    while (cur.nextnode!=None and cur.nextnode.elem != value):
        cur = cur.nextnode
    if cur.nextnode!=None:
        cur.nextnode = cur.nextnode.nextnode
    else:
        print('the value is not in the list')

if __name__ == '__main__':
    head = Head()
    head = initializelist(head, [1, 2, 3, 4,5])
    delelem(head, 1)
    printllist(head)
