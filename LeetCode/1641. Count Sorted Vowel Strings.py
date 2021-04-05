class Solution(object):


    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = []
        tmp = []
        for i in range(n):
            for j in range(5):
                tmp.append(0)
            dp.append(list.copy(tmp))
            tmp.clear()


        dp[0] = [5,4,3,2,1]
        print(dp)
        for i in range(1,n):
            for j in range(4,-1,-1):
                if j == 4:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j+1]
        # print(dp)
        print(dp[n-1][0])
s = Solution()
s.countVowelStrings(33)
