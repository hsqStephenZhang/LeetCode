class TreeNode(object):
    def __init__(self,left=None,right=None,val=None):
        self.left=left
        self.right=right
        self.val=val

class Solution(object):
    def createtree(self,root,value=None,tag=None):
        if tag is not None:
            val=input(tag+value+" :")
        else:
            val=input('root:')
        if val=='#':
            root=None
        else:
            root=TreeNode(val=val)
            root.left=self.createtree(root.left,value=root.val,tag='left of ')
            root.right=self.createtree(root.right,value=root.val,tag='right of ')
        return root

    def in_order(self,tree):
        if tree is not None:
            self.in_order(tree.left)
            print(tree.val)
            self.in_order(tree.right)
        else: return

    def isSymmetric(self, root):
        if not root or (not root.right and not root.left):
            return True
        stack = []
        left=[]
        right=[]
        p = root
        while p or stack != []:
            # 只有p不为空的时候入栈
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                left.append(p.val)
                p = p.right
        p=root
        while p or stack != []:
            # 只有p不为空的时候入栈
            if p:
                stack.append(p)
                p = p.right
            else:
                p = stack.pop()
                right.append(p.val)
                p = p.left
        return left==right

    def zigzagLevelOrder(self,root):
        if root is None: return []
        result=[]
        prelevel=[root]
        curlevel=[]
        tag=0
        while prelevel!=[] or curlevel!=[]:
            result.append([item.val for item in prelevel])
            while prelevel!=[]:
                cur=prelevel.pop()
                if tag:
                    if cur.left:
                        curlevel.append(cur.left)
                    if cur.right:
                        curlevel.append(cur.right)
                else:
                    if cur.right:
                        curlevel.append(cur.right)
                    if cur.left:
                        curlevel.append(cur.left)
            prelevel=curlevel
            curlevel=[]
            tag=1^tag
        return result

s=Solution()
root=TreeNode()
root=s.createtree(root=root)

print(s.zigzagLevelOrder(root))