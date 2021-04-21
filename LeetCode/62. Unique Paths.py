class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = []
        for row in range(m):
            dp.append([0]*n)

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = 1
                elif j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]

        return dp[-1][-1]