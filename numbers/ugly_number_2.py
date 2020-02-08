class Solution(object):
    """返回第n个丑数，第一个丑数是1"""

    def nthUglyNumber(self, n):
        base = [1]
        index_of_two, index_of_three, index_of_five = 0, 0, 0
        count = 1
        while count < n:
            base.append(min(base[index_of_two] * 2,
                            base[index_of_three] * 3,
                            base[index_of_five] * 5))
            if base[-1] == base[index_of_two] * 2:
                index_of_two += 1
            if base[-1] == base[index_of_three] * 3:
                index_of_three += 1
            if base[-1] == base[index_of_five] * 5:
                index_of_five += 1
            count += 1
        return base[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(14))
