import networkx as nx
import matplotlib.pyplot as plt


class TreeNode(object):
    def __init__(self, left=None, right=None, val=None):
        self.left = left
        self.right = right
        self.val = val

class Tree(object):
    def __init__(self):
        self.root=None
        self.depth=None

    def createtree(self, tree, value=None, tag=None):
        if tag is not None:
            val = input(tag + value + " :")
        else:
            val = input('root:')
        if val == '#':
            tree = None
        else:
            tree = TreeNode(val=val)
            tree.left = self.createtree(
                tree.left, value=tree.val, tag='left of ')
            tree.right = self.createtree(
                tree.right, value=tree.val, tag='right of ')
        return tree

    def maxDepth(self, tree):
        if tree is None:
            return 0
        return max(self.maxDepth(tree.left), self.maxDepth(tree.right)) + 1

    def in_order(self,root):
        if root is not None:
            self.in_order(root.left)
            print(root.val)
            self.in_order(root.right)
        else:
            return

    def create(self,root:TreeNode,G:nx.DiGraph,pos,x=0,y=0,layer=1,bias=0):
        if root is not None:
            pos[root.val]=(x,y)
            if root.left:
                G.add_node(root.val)
                G.add_edge(root.val,root.left.val)
                l_x, l_y = x -bias, y - 1
                layer += 1
                self.create(root.left,G,pos,x=l_x,y=l_y,layer=layer,bias=bias//2)
            if root.right:
                G.add_edge(root.val,root.right.val)
                r_x, r_y = x +bias, y - 1
                layer += 1
                self.create(root.right,G,pos,x=r_x,y=r_y,layer=layer,bias=bias//2)
            return G,pos
        else:
            return

    def draw(self, root):
        graph = nx.DiGraph()
        graph, pos = self.create(root,graph,pos=dict(),bias=2**self.maxDepth(root))
        fig, ax = plt.subplots(figsize=(12, 8))
        nx.draw(
            graph,
            ax=ax,
            pos=pos,
            with_labels=True,
            edge_color='b',
            node_color='r',
            node_size=1000)
        plt.show()


if __name__ == '__main__':
    a = Tree()
    root = TreeNode()
    a.root = a.createtree(root)
    a.depth=a.maxDepth(root)
    a.draw(a.root)


