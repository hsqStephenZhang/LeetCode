class TreeNode(object):
    def __init__(self,left=None,right=None,val=None,Ltag=None,Rtag=None):
        self.left=left
        self.right=right
        self.Ltag=Ltag
        self.Rtag=Rtag
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
            root.Ltag=root.Rtag=0
            root.left=self.createtree(root.left,value=root.val,tag='left of ')
            root.right=self.createtree(root.right,value=root.val,tag='right of ')
        return root

    def inthreading(self,root,pre):
        if root is None: return
        self.inthreading(root.left,pre)
        if root.left is None:
            root.Ltag=1
            root.left=pre
        if pre.right is None:
            pre.Rtag=1
            pre.Rtag=root
        pre=root
        self.inthreading(root.right,pre)


s=Solution()
root=TreeNode()
pre=TreeNode()
root=s.createtree(root)
s.inthreading(root,pre)