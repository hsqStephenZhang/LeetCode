from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class TreeNode(object):
    def __init__(self, left=None, right=None, val=None):
        self.left = left
        self.right = right
        self.val = val


class Tree(object):
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

    def pre_order(self, tree):
        if tree is not None:
            print(tree.val)
            self.pre_order(tree.left)
            self.pre_order(tree.right)
        else:
            return

    def in_order(self, tree):
        if tree is not None:
            self.in_order(tree.left)
            print(tree.val)
            self.in_order(tree.right)
        else:
            return

    def post_order(self, tree):
        if tree is not None:
            self.post_order(tree.left)
            self.post_order(tree.right)
            if tree.val:
                print(tree.val)

    def BFS(self, tree):
        myqueue = deque()
        myqueue.append(tree)
        while len(myqueue) != 0:
            t = myqueue.popleft()
            if t.left.val is not None:
                myqueue.append(t.left)
            if t.left.val is not None:
                myqueue.append(t.right)
            print(t.val)

    def maxDepth1(self, tree):
        if tree is None:
            return 0
        return max(self.maxDepth1(tree.left), self.maxDepth1(tree.right)) + 1

    def maxDepth2(self, root):
        queue = []
        depth = []
        curr_depth = -1
        if root:
            queue.append(root)
            depth.append(0)
        while queue:
            curr_root = queue.pop()
            curr_depth = depth.pop()
            if curr_root.left:
                queue.insert(0, curr_root.left)
                depth.insert(0, curr_depth + 1)
            if curr_root.right:
                queue.insert(0, curr_root.right)
                depth.insert(0, curr_depth + 1)
        return curr_depth

    def maxDepth3(self, tree):
        myqueue = deque()
        depth = deque()
        maxdepth = 0
        if tree:
            myqueue.append(tree)
            depth.append(0)
        while myqueue:
            t = myqueue.popleft()
            maxdepth = depth.popleft()
            if t.left:
                myqueue.append(t.left)
                depth.append(maxdepth + 1)
            if t.left:
                myqueue.append(t.right)
                depth.append(maxdepth + 1)
        return maxdepth

    def get_sibling(self, tree, e):
        if tree and tree.left is not None and tree.left.val == e:
            return tree.right
        elif tree and tree.right is not None and tree.right.val == e:
            return tree.left
        else:
            if tree:
                p = self.get_sibling(tree.left, e)
                if p:
                    return p
                p = self.get_sibling(tree.right, e)
                if p:
                    return p
        return None

    def find_node(self, tree, e):
        if tree is None:
            return None
        if tree.val == e:
            return tree
        else:
            t1 = self.find_node(tree.left, e)
            if t1 is not None:
                return t1
            t1 = self.find_node(tree.right, e)
            if t1:
                return t1
        return None

    def inorderTraversal(self, root):
        stack = []
        cur = root
        result = []
        while stack or cur:
            while cur:
                stack.append(cur.left)
                cur = cur.left
            if stack:
                cur = stack.pop()
                if result:
                    result.append(cur.val)
                    cur = cur.right
        return result

    def create_graph(
            self,
            G: nx.DiGraph,
            node: TreeNode,
            pos=None,
            x=0,
            y=0,
            layer=1):
        if pos is None:
            pos = {}
        pos[node.val] = (x, y)
        if node.left:
            G.add_edge(node.val, node.left.val)
            l_x, l_y = x - 1 / 2**layer, y - 1
            layer += 1
            self.create_graph(
                G,
                node.left,
                pos=None,
                x=l_x,
                y=l_y,
                layer=layer)
        if node.right:
            G.add_edge(node.val, node.right.val)
            r_x, r_y = x - 1 / 2 ** layer, y - 1
            layer += 1
            self.create_graph(
                G,
                node.right,
                pos=None,
                x=r_x,
                y=r_y,
                layer=layer)

        return G, pos

    def draw(self, root):
        graph = nx.DiGraph()
        graph, pos = self.create_graph(graph, root)
        fig, ax = plt.subplots(figsize=(8, 10))
        nx.draw_networkx(graph, pos, ax=ax, node_size=300)
        plt.show()


if __name__ == '__main__':
    a = Tree()
    root = TreeNode()
    root = a.createtree(root)
    a.draw(root)
    # e='1'
    # find = [a.find_node(root, e) for e in "345"]
    # for item in find:
    #     if item:
    #         print(item.val)
    #     else:
    #         print("Not found")
    # result=a.get_sibling(root,e)
    # if result and result.val:
    #     print(result.val)
    # else:
    #     print("not found")
