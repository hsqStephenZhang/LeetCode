class Solution(object):
    def __init__(self):
        self.bad_str = {}
        self.good_suffix_table = {}

    def generate_bad_str(self, pattern):
        for i in range(97, 123):
            self.bad_str[chr(i)] = -1
        for i, s in enumerate(pattern):
            self.bad_str[s] = i

    def generate_good_suffix(self,pattern):
        pass



    def BoyerMooreHorspool(self, pattern, text):
        self.generate_bad_str(pattern)
        m = len(pattern)
        n = len(text)
        k = m - 1
        while k < n :
            j = m - 1
            i = k
            while j >= 0 and text[i] == pattern[j]:
                j -= 1
                i -= 1
            if j == -1:
                return i + 1
            k = k + j -self.bad_str[text[i]]
        return -1



if __name__ == '__main__':
    text = "here-is-a-simple-example"
    pattern = "sim"
    s = Solution()
    result = s.BoyerMooreHorspool(pattern, text)
    print('Text:', text)
    print('Pattern:', pattern)
    if result > -1:
        print('Pattern \"' + pattern + '\" found at position', result)
