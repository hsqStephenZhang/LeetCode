class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        974.求出数组中能够被k整除的一段子数组的个数
        nice，LeetCode击败了100%,100%的用户
        参照前缀和数组的思路，只不过利用了同余的性质
        """
        concrugence_dict=dict.fromkeys(range(K),0)
        concrugence_dict[0]=1
        prefixsum=0
        result=0
        for elem in A:
            prefixsum+=elem
            concrugence_dict[prefixsum%K]+=1
        for i in range(K):
            if concrugence_dict[i]>1:
                # 直接根据C(n,2)的公式计算
                result+=concrugence_dict[i]*(concrugence_dict[i]-1)//2
        return result


if __name__ == '__main__':
    s=Solution()
    A = [4, 5, 0, -2, -3, 1]
    K=5
    print(s.subarraysDivByK(A,K))


