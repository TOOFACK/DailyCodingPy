class Solution(object):
    def __init__(self):
        self.visited = []

    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """

        def inside(row, col):
            max_row = len(grid)
            max_col = len(grid[0])
            if 0 <= col < max_col and 0 <= row < max_row:
                return True
            else:
                return False

        def dfs(row, col, t):

            if not inside(row, col) or self.visited[row][col][t]:
                return

            self.visited[row][col][t] = True

            if t == 0:
                dfs(row - 1, col, 2)
            elif t == 1:
                dfs(row, col + 1, 3)
            elif t == 2:
                dfs(row + 1, col, 0)
            elif t == 3:
                dfs(row, col - 1, 1)

            if grid[row][col] != "/":
                dfs(row, col, t ^ 1)
            if grid[row][col] != "\\":
                dfs(row, col, t ^ 3)

        ans = 0


        tmp = []

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                tmp.append([False,False,False,False])
            self.visited.append(list.copy(tmp))
            tmp.clear()


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                for t in range(4):
                    if not self.visited[row][col][t]:
                        dfs(row, col, t)
                        ans += 1
        return ans
