m = {
    '2': list('abc'),
    '3': list('def'),
    '4': list('ghi'),
    '5': list('jkl'),
    '6': list('mno'),
    '7': list('pqrs'),
    '8': list('tuv'),
    '9': list('wxyz'),
}


class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        ls1 = ['']
        for i in digits:
            ls1 = [x + y for x in ls1 for y in m[i]]
        return ls1

a='234'
s=Solution()
result=s.letterCombinations(a)

for i in result:
    print(i,end=' ')