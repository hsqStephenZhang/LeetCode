class Solution(object):
    """
    336.回文对
    给定一组唯一的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。
    """

    def palindromePairs(self, words):
        """
        对于一组可以拼成回文对的单词，可以将位于后面的单词看成是一个回文子串加上一个后缀
        只要后缀匹配了即可
        """
        res=[]
        reversed_words={}
        palinkdromed=[] #单独处理，因为这个对空字符处理很关键
        for i,word in enumerate(words):
            reversed_words[word[::-1]]=i
            if word==word[::-1]:
                palinkdromed.append(i)
        for i,word in enumerate(words):
            if word:
                for k in range(len(word)):
                    left,right=word[:k],word[k:]
                    if left==left[::-1] and right in reversed_words and reversed_words[right]!=i:
                        res.append([reversed_words[right],i])
                    if right==right[::-1] and left in reversed_words and reversed_words[left]!=i:
                        res.append([i,reversed_words[left]])
            else:
                for index in palinkdromed:
                    if index!=i:
                        res.append([index,i])
        return res

if __name__ == '__main__':
    s = Solution()
    mywords = ["abcd", "dcba", "lls", "s", "sssll"]
    mywords2 = ["a","b","c","ab","ac","aa"]
    print(s.palindromePairs(mywords2))