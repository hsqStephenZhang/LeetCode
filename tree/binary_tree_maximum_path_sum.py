import sys
import functools



class TreeNode(object):
    def __init__(self, left=None, right=None, val=None):
        self.left = left
        self.right = right
        self.val = val


class Solution(object):
    """
    124.二叉树中的最大路径和
    定义一颗二叉树，求其最大路径和(结点的值可能是负数)
    注意，这里的路径和是指路径上所有的结点的值加起来之和
    """

    def __init__(self):
        self.res = -sys.maxsize
        self.my_dict = {}
        self.flags = {}
        self._max = -sys.maxsize
        self.index = 0


    def create_tree(self, root, data):
        if len(data) - 1 == self.index or data[self.index] == "#":
            self.index += 1
            return None
        else:
            root = TreeNode(val=data[self.index])
            self.index += 1
            root.left = self.create_tree(root.left, data)
            root.right = self.create_tree(root.right, data)
        return root

    def in_order(self, tree):
        if tree is not None:
            self.in_order(tree.left)
            print(tree.val, end=' ')
            self.in_order(tree.right)
        else:
            return

    def maxPathSum(self,root):
        """
        这一题的关键在于能不能和父结点相连，假如当前结点，左子树，右子树的值都大于零，那么是无法返回三者之和的
        只能选择其中的一颗子树
        """
        self.getmax(root)
        return self.res

    def getmax(self,root,):
        if root is None:
            return 0
        left=max(0,self.getmax(root.left))
        right=max(0,self.getmax(root.right))
        self.res=max(self.res,left+right+root.val)
        return max(left,right)+root.val





if __name__ == '__main__':
    s = Solution()
    root = TreeNode()
    data = [5, '#', -2, 1, '#', '#', -1, '#', 4, '#', '#', ]
    data2 = [1, -2, 3, '#', '#', 4, '#', -5, '#',
             '#', 6, -1, '#', '#', 7, -5, '#', '#', '#']
    data3 = [8, 9, '#', '#', -6, 5, '#', '#', 9, '#', '#', ]
    root = s.create_tree(root, data=data2)
    # s.in_order(root)
    # print("\n", end="")
    # print(s.maxPathSum(root))
    print(s.in_order(root))
