class TreeNode(object):
    def __init__(self, left=None, right=None, val=None):
        self.left = left
        self.right = right
        self.val = val

class Tree(object):
    def __init__(self):
        self.index=0

    def create_tree(self,root,data):
        if len(data)-1==self.index or data[self.index]== "#":
            self.index+=1
            return None
        else:
            root=TreeNode(val=data[self.index])
            self.index+=1
            root.left=self.create_tree(root.left,data)
            root.right=self.create_tree(root.right,data)
        return root

    def in_order(self,tree):
        if tree is not None:
            self.in_order(tree.left)
            print(tree.val,end=' ')
            self.in_order(tree.right)
        else: return

root=TreeNode()
t=Tree()
string="AB#D##C##"
data=[i for i in "AB#D##C##"]
root=t.create_tree(root,data=data)
t.in_order(root)
