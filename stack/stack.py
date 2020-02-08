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


