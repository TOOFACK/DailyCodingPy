class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        col = len(matrix[0])
        row = len(matrix)

        if len(matrix) == 0:
            return 0

        res = 0

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 1:
                    if c == 0 or r == 0:
                        res += 1
                    else:
                        val = min(matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1]) + 1
                        matrix[r][c] = val
                        res += val
        return res
