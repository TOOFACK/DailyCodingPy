class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = []
        for row in range(len(grid)):
            dp.append([0]*len(grid[0]))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1]+grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1]+ grid[i][j])
        return dp[-1][-1]
