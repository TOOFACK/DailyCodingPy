from copy import deepcopy


class Solution(object):
    def __init__(self):

        self.maxi = -1
        self.visited = []

    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def in_matrix(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col, max):
            # print("row =", row)
            # print("col = ", col)
            # print("len grid = ", len(grid))
            # print(in_matrix(row, col))
            if in_matrix(row, col) and not self.visited[row][col] and grid[row][col] != 0:
                self.visited[row][col] = True

                for r, c in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                    if in_matrix(r, c):

                        dfs(r, c, max + grid[r][c])
                        if max > self.maxi:
                            self.maxi = max
                self.visited[row][col] = False

        self.visited = []
        for i in range(len(grid)):
            self.visited.append([False] * len(grid[0]))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # print(self.visited)
                # print()
                if grid[row][col] != 0:

                    dfs(row, col, grid[row][col])
        print(self.maxi)
        return self.maxi


s = Solution()
s.getMaximumGold(
    grid=[[1, 0, 7, 0, 0, 0], [2, 0, 6, 0, 1, 0], [3, 5, 6, 7, 4, 2], [4, 3, 1, 0, 2, 0], [3, 0, 5, 0, 20, 0]])
