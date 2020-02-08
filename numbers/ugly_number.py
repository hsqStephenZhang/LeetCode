class Solution(object):
    """判断一个正整数的质因数是否只含有2,3,5"""

    def isUgly(self, num):
        if num<=0:return False
        while num%2==0:
            num=num//2
        while num % 3 == 0:
            num = num // 3
        while num % 5 == 0:
            num = num // 5
        if num == 1:
            return True
        else:
            return False
