import math
from collections import deque


class Solution(object):
    def __init__(self):
        self.memo = []

    def numSquares(self, n):
        """
        第一种方法,需要搜索所有的结点，只是用了一个数组(当做hash表)来保存对i求该值的最小值，该数组初始化
        为1,2,3,4...(因为至少可以表示为i个1^2相加)
        """
        for i in range(n + 1):
            self.memo.append(i)

        for i in range(2, n + 1):
            for j in range(1, int(math.sqrt(i)) + 1):
                self.memo[i] = min(self.memo[i], 1 + self.memo[i - j**2])
        return self.memo[n]

    def solution2(self, n):
        """
        使用广度优先遍历的方法，通过队列来控制遍历的次序，因为是逐层遍历，所以一旦遍历结束，返回的就是最优解
        牺牲空间换取时间
        """
        count=1
        queue=[n]
        while queue:
            nextlevel=[]
            for cur in queue:
                for i in range(int(math.sqrt(cur)),0,-1):
                    if cur-i**2==0:
                        return count
                    else:
                        nextlevel.append(cur-i**2)
            queue=nextlevel
            count+=1
        return count-1



if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(3530))
    print(s.solution2(3530))
    print(s.solution2(12))
    print(s.solution2(9))
