class Solution1:
    def isPalindrome(self, s: str):
        n = len(s)
        left, right = 0, n - 1
        while(left < right):
            while(s[left].isdigit() == False and s[left].isalpha() == False and left < right):
                left += 1
            while(s[right].isdigit() == False and s[right].isalpha() == False and left < right):
                right -= 1
            if left == right:
                return True
            if s[left].isdigit():
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            else:
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
        if left == right or left - right == 1:
            return True
        else:
            return False

class Solution2:
    def isPalindrome(self, s: str):
        str_list = s.upper()
        myword = [word for word in str_list if 'A'<=word<='Z' or '0'<=word<='9']
        myword_str=''.join(myword)
        print(myword_str,type(myword_str))
        reverseone=myword_str[::-1]
        print(reverseone,type(reverseone))
        return myword_str==reverseone

a = "A man, a plan, a canal: Panama"
b = ".,"
s = Solution2()
result = s.isPalindrome(a)
print(result)

