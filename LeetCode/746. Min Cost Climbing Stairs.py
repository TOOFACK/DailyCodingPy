class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * len(cost)
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]
        new_mas = cost[-3::-1]
        for i in range(len(new_mas)):
            dp[-3-i] = new_mas[i] + min(dp[-2-i], dp[-1-i])
        return min(dp[0],dp[1])

s = Solution()
s.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1])