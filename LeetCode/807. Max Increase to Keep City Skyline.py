class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        max_row = [0]*(len(grid))
        max_col = [0]*(len(grid[0]))

        prev_sum = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                prev_sum += grid[row][col]
                if grid[row][col] > max_row[row]:
                    max_row[row] = grid[row][col]

        for col in range(len(grid[0])):
            for row in range(len(grid)):

                if grid[row][col] > max_col[col]:
                    max_col[col] = grid[row][col]

        ans = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] < min(max_row[row],max_col[col]):
                    grid[row][col] = min(max_row[row],max_col[col])

                ans += grid[row][col]


        # print(max_col)
        # print(max_row)
        # print(grid)
        # print(ans-prev_sum)
        return prev_sum-ans

s = Solution()
s.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])


