class Solution(object):
    def __init__(self):
        self.visited = []

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def inside(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            if not inside(row, col) or self.visited[row][col] or grid[row][col] == "0":
                return
            self.visited[row][col] = True

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        islands = 0
        tmp = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                tmp.append(False)
            self.visited.append(list.copy(tmp))
            tmp.clear()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if not self.visited[row][col] and grid[row][col] != "0":
                    dfs(row, col)
                    islands += 1

        return islands

