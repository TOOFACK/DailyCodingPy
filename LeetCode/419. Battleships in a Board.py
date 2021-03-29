class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        row = len(board)
        col = len(board[0])
        if len(board) == 0:
            return 0
        ans = 0

        for r in range(row):
            for c in range(col):
                if board[r][c] == "X" and (r == 0 or board[r-1][c] == ".") and (c == 0 or board[r][c-1] == "."):
                    ans +=1
        return ans