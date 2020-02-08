class Solution(object):
    def __init__(self,graph):
        self.graph=graph
        self.length=len(graph)
        self.colors=[-1]*self.length
        self.starttime=[0]*self.length
        self.finishtime=[0]*self.length
        self.pre=[-1]*self.length
        self.time=0

    def DFS(self):
        for node in self.graph:
            if self.colors[node]==-1:
                self.DFS_visit(node)

    def DFS_visit(self,i):
        self.colors[i]=0
        self.time += 1
        self.starttime[i]=self.time
        for j in self.graph[i]:
            if self.colors[j]==-1:
                self.pre[j]=i
                self.DFS_visit(j)
        self.colors[i]=1
        self.time += 1
        self.finishtime=self.time+1

