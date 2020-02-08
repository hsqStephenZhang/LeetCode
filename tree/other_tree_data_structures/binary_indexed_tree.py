class BIT(object):

    def __init__(self, nums):
        """
        树状数组的公式(lowbit代表最低的二进制为1的位置):
        C[i]=A[i-lowbit(i)+1]+A[i-lowbit(i)+2]+......A[i]
        lowbit(x)=x & (-x)
        其中i-lowbit(x)=i&(i-1)
        """
        self.length = len(nums)
        self.tree = [0] * (self.length + 1)
        sums = [0] * (self.length + 1)
        for i in range(self.length):
            sums[i + 1] = sums[i] + nums[i]
        for i in range(1, self.length + 1):
            self.tree[i] = sums[i] - sums[i & (i - 1)]

    def getsum(self, x):
        """
        求和的实质就是将一个区间按照length的bit位划分:
        length~length&(length-1),length2~length2&(length2-1)...
        其中，length2=length&(length-1)...
        """
        if x < 0 or x >= self.length:
            raise IndexError("out of boundry!")
        result = 0
        while x > 0:
            result += self.tree[x]
            x = x & (x - 1)
        return result

    def getrange(self, low, high):
        """
        前high个数的和减去前low个数的和
        """

        if low < 0 or high < 0 or low >= self.length or high >= self.length:
            raise IndexError("out of boundry!")
        if low > high:
            raise IndexError
        else:
            return self.getsum(high) - self.getsum(low)

    def update(self, i, val):
        """
        这里的i是序号，从1开始
        """
        while i <= self.length:
            self.tree[i] += val
            i += i & (-i)


class BIT2d(object):
    def __init__(self, data):
        self.table = []
        self.rows = len(data)
        self.cols = len(data[0])
        for i in range(self.rows):
            self.table.append(BIT(data[i]))


if __name__ == '__main__':
    lis = [1, 2, 3, 4, 5, 6, 7]
    mydata = [[1, 2, 3], [4, 5, 6, ], [7, 8, 9]]
    s = BIT(lis)
    print(s.getrange(0,3))
    # s = BIT2d(mydata)
    # for row in s.table:
    #     print(row.tree)
