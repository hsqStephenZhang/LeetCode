class Solution(object):
    def decodeString(self,s):
        this_atr=''
        num=0
        mystack=[]
        for i in s:
            if i.isdigit():
                num=num*10+int(i)
            elif i.isalpha():
                this_atr+=i
            elif i=='[':
                mystack.append((this_atr,num))
                this_atr,num='',0
            else:
                last_atr,this_num=mystack.pop()
                this_atr=last_atr+this_num*this_atr
        return this_atr


if __name__ == '__main__':
    string = "3[a]2[bd3[c]]"
    s=Solution()
    result=s.decodeString(string)
    print(result)







