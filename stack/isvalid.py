import stack

class Solution(stack.Stack):
    def __init__(self):
        super(Solution, self).__init__()

    @staticmethod
    def match(s1,s2):
        if s1=='(' and s2==')':
            return True
        if s1=='[' and s2==']':
            return True
        if s1=='{' and s2=='}':
            return True
        return False
    
    def isValid(self,str):
        for i in range(len(str)):
            if self.items!=[] and self.match(self.gettop(),str[i]) :
                self.pop()
            else:
                self.push(str[i])
        if self.items==[]:
            return True
        else: return False

if __name__ == '__main__':
    s=Solution()
    result=s.isValid('({[})')
    print(result)