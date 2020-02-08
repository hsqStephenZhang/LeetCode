class Stack(object):
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items)==0

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            rtn=self.items[-1]
            self.items.pop()
            return rtn

    def size(self):
        return len(self.items)

    def gettop(self):
        if self.isEmpty():
            return False
        else:
            return self.items[-1]

class Solution(Stack):
    match=['+','-','*','/']

    def docal(self,calc):
        n2=int(self.pop())
        n1=int(self.pop())
        if calc=='+':
            self.items.append(str(n1+n2))
        if calc=='-':
            self.items.append(str(n1-n2))
        if calc=='*':
            self.items.append(str(n1*n2))
        if calc=='/':
            self.items.append(str(int(n1/n2)))

    def evalRPN(self, tokens):
        for item in tokens:
            if item not in self.match:
                self.push(item)
            # elif item==re.mat:
            else:
                self.docal(item)
        return int(self.items[0])

if __name__ == '__main__':
    s=Solution()
    tokens=["4","13","5","/","+"]
    print(s.evalRPN(tokens))