class Solution(object):
    def zigzagLevelOrder(self, root):
        if root is None: return []
        result = []
        prelevel = [root]
        curlevel = []
        tag = 0
        while prelevel != [] or curlevel != []:
            result.append([item.val for item in prelevel])
            while prelevel != []:
                cur = prelevel.pop()
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
            prelevel = curlevel
            curlevel = []
            tag = 1 ^ tag
        return result

