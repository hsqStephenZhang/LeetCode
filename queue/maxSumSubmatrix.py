class Solution(object):
    """
    363.给定一个非空二维矩阵 matrix 和一个整数 k，找到这个矩阵内部不大于 k 的最大矩形和
    """

    def maxSumSubmatrix(self, matrix, k):
        """
        先求出前缀和矩阵
        如果行的数目大于列的数目，则将列的左右的位置固定，然后分别计算最大的不超过k的
        矩形面积,遍历所有的左右边界的可能，可以在O(n*n*m*logm)时间内求出结果，其中，
        若行数大于列数，则n为列数
        """