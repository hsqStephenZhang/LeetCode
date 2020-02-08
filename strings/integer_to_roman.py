class Solution(object):
    """
    12.将一个整数转换为罗马字符，输入确保在 1 到 3999 的范围内。
    """

    def __init__(self):
        self.dic = dict()
        self.matches = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'}

    def intToRoman(self, num):
        self.breaknubmer(num)
        result = ""
        for base in [1000, 100, 10, 1]:
            if self.dic[base] != 0:
                if self.dic[base] == 4:
                    result += self.matches[base]
                    result += self.matches[base * 5]
                elif self.dic[base] == 9:
                    result += self.matches[base]
                    result += self.matches[base * 10]
                elif self.dic[base]==1 or self.dic[base]==5:
                    result+=self.matches[base*self.dic[base]]
                elif 2<=self.dic[base]<=4:
                    result+=self.matches[base]*self.dic[base]
                else:
                    result+=self.matches[base*5]
                    result+=self.matches[base]*(self.dic[base]-5)

        return result

    def breaknubmer(self, num):
        """
        将一个数字分解
        """
        pos = [1, 10, 100, 1000]
        for i in range(4):
            self.dic[pos[i]] = num % 10
            num = num // 10


if __name__ == '__main__':
    s = Solution()
    num = 4
    print(s.intToRoman(num))
