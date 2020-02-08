class TreeNode(object):
    def __init__(self,left=None,right=None,val=None):
        self.left=left
        self.right=right
        self.val=val


class  Solutions(object):
    def createtree(self,tree,value=None,tag=None):
        if tag is not None:
            val=input(tag+value+" :")
        else:
            val=input('root:')
        if val=='#':
            tree=None
        else:
            tree=TreeNode(val=val)
            tree.left=self.createtree(tree.left,value=tree.val,tag='left of ')
            tree.right=self.createtree(tree.right,value=tree.val,tag='right of ')
        return tree

    def inorderTraversal1(self, root: TreeNode):
        stack=[]
        stack.append(root)
        while (stack!=[]):
            while(stack[-1]):
                stack.append(stack[-1].left)
            stack.pop()
            if stack!=[]:
                p=stack.pop()
                if p.val:
                    print(p.val)
                stack.append(p.right)

    def inorderTraversal2(self, root: TreeNode):
        stack=[]
        p=root
        while p or stack!=[]:
            # 只有p不为空的时候入栈
            if p:
                stack.append(p)
                p=p.left
            else:
                p=stack.pop()
                # if p.val:
                print(p.val)
                # else:
                print('len: ',len(stack))
                p=p.right


if __name__ == '__main__':
    root=TreeNode()
    s=Solutions()
    s.createtree(root)
    s.inorderTraversal1(root)

