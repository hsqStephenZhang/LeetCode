class Solution(object):
    def climbStairs(self,n):
        """
        每次可以爬一级或者两级台阶，爬到n级有多少种方案
        """
        if n<=2: return n
        i1,i2=1,2
        start=3
        while start<=n:
            i1,i2=i2,i1+i2
            start+=1
        return i2

if __name__ == '__main__':
    s=Solution()
    print(s.climbStairs(4))
