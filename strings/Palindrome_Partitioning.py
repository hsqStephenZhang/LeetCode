class Solution(object):
    """
    131.将一个给定的字符串分割，使得每一个子串都是回文串
    """
    """ 
    这个是别人的解答，确实十分精妙
    """
    def partition(self, s):
        a=[[s[0]]]
        for i in range(1,len(s)):
            for j in a[:len(a)]:
                if len(j)>1 and s[i]==j[-2]:
                    a.append(j[:-2]+[j[-2]+j[-1]+j[-2]])
                if s[i]==j[-1]:
                    a.append(j[:-1]+[j[-1]*2])
                j.append(s[i])
        return a


if __name__ == '__main__':
    s = Solution()
    strings = "aab"
    print(s.partition(strings))
