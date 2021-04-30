from math import sqrt


class Solution(object):
    def __init__(self):
        self.memo = {}

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        # def dfs(n):
        #     if n in self.memo:
        #         return self.memo[n]
        #     cnt = n
        #     i = 1
        #     while i * i <= n:
        #         cnt = min(cnt, dfs(n - i * i) + 1)
        #         i += 1
        #     self.memo[n] = cnt
        #     return cnt
        #
        # ans = n
        # i = 1
        # while i * i <= n:
        #     ans = min(ans, dfs(n - i * i) + 1)
        #     i += 1
        # print(ans)
        # return ans
        #
        dp = [0] *(n+1)

        for i in range(0, n+1):
            dp[i] = i
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i-j*j] + 1)
                j += 1
        print(dp[n])
        return (dp[n])

s = Solution()
s.numSquares(
    43)
