class Solution(object):
    def countDigitOne1(self,n):
        result=0
        a=b=1
        while n>0:
            result+=(n+8)//10*a+(n%10==1)*b
            b+=n%10*a
            a=a*10
            n=n//10
        return result

    def countDigitOne2(self, n):
        count=0
        factor=1
        while n//factor!=0:
            lower=n%factor
            cur=(n//factor)%10
            higher=n//(factor*10)
            if cur==0:
                count+=higher*factor
            elif cur==1:
                count+=higher*factor+lower+1
            else:
                count+=(higher+1)*factor
            factor*=10
        return count


a=12321
s=Solution()
# print(s.countDigitOne1(a))
print(s.countDigitOne2(a))