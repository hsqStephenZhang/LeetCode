class Solution(object):
    """返回第n个丑数，丑数的质因子由primes给出"""

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :rtype: int
        """
        base = [1]
        indexs = [0] * len(primes)
        count = 1
        while count < n:
            base.append(min(base[indexs[i]] * primes[i]
                            for i in range(len(primes))))
            for i in range(len(primes)):
                if base[-1] == base[indexs[i]] * primes[i]:
                    indexs[i] += 1
            count += 1
        return base[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.nthSuperUglyNumber(12, [2, 7, 13, 19]))
