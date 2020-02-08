class Solution(object):
    def isBipartite(self, graph):
        """
        染色法，通过DFS遍历将当前结点的邻接节点染成与当前结点不同的颜，如果染色
        冲突，说明该图不是二分图
        """
        colors=[-1]*len(graph)
        for i in range(len(graph)):
            if colors[i]==-1:
                stack=[]
                stack.append(i)
                colors[i]=0
                while stack!=[]:
                    cur=stack.pop()
                    for j in graph[cur]:
                        if colors[j]==-1:
                            stack.append(j)
                            colors[j]=1-colors[cur]
                        elif colors[j]==colors[cur]:
                            return False
        return True

if __name__ == '__main__':
    s=Solution()
    graph1=[[1,3],[0,2],[1,3],[0,2]]
    graph2 = [[1, 2,3], [0, 2], [0,1, 3], [0, 2]]
    graph3=[[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
    print(s.isBipartite(graph1))
    print(s.isBipartite(graph2))
    print(s.isBipartite(graph3))
