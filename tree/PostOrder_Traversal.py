class TreeNode(object):
    def __init__(self, left=None, right=None, val=None):
        self.left = left
        self.right = right
        self.val = val


class Solution(object):
    """
    定义一颗二叉树，求其最大路径和
    注意，这里的路径和是指路径上所有的结点的值加起来之和
    """

    def __init__(self):
        self.index = 0

    def postorderTraversal(self, root):
        """
        用迭代的方法后序遍历二叉树
        """
        if root is None: return []
        nodes = []
        output = []
        tags = {}
        nodes.append(root)
        while nodes != []:
            cur = nodes[-1]
            if cur in tags.keys():
                output.append(nodes.pop(-1).val)
            else:
                tags[cur] = 1
                if cur.right and cur.left:
                    nodes.append(cur.right)
                    nodes.append(cur.left)
                    if cur.left.left is None and cur.left.right is None:
                        output.append(nodes.pop(-1).val)
                elif cur.left is not None and cur.right is None:
                    nodes.append(cur.left)
                elif cur.right is not None and cur.left is None:
                    nodes.append(cur.right)
                else:
                    output.append(nodes.pop(-1).val)
        return output

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


if __name__ == '__main__':
    s = Solution()
    root = TreeNode()
    data = [5, '#', -2, 1, '#', '#', -1, '#', 4, '#', '#', ]
    data2 = [1, -2, 3, '#', '#', 4, '#', -5, '#',
             '#', 6, -1, '#', '#', 7, -5, '#', '#', '#']
    data3 = [8, 9, '#', '#', -6, 5, '#', '#', 9, '#', '#', ]
    root = s.create_tree(root, data=data2)
    print(s.postorderTraversal(root))
