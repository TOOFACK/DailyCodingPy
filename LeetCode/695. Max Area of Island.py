class Solution(object):
    def __init__(self):
        self.visited = []
        self.ans = 0
        self.curr_area = 0

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        for i in range(len(grid)):
            self.visited.append([False] * len(grid[0]))

        def in_matrix(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                return True
            else:
                return False

        def dfs(row, col):
            if in_matrix(row, col) and not self.visited[row][col] and grid[row][col]:
                self.visited[row][col] = True
                self.curr_area += 1

                for x, y in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                    if in_matrix(x, y) and not self.visited[x][y] and grid[x][y] != 0:
                        print("from row = ", row, " ", col, " go to ", x, " ", y)
                        dfs(x, y)

                if self.curr_area > self.ans:
                    self.ans = self.curr_area

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0 and not self.visited[row][col]:
                    self.curr_area = 0
                    dfs(row, col)

        return self.ans
