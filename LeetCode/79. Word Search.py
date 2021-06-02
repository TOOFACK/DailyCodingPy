class Solution(object):
    def __init__(self):
        self.path = []
        self.exisited = False
        self.in_path = []

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def in_matrix(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def search(idx, row, col):
            if len(self.path) == len(word):
                self.exisited = True
                return

            if not in_matrix(row, col) or self.in_path[row][col]:
                return

            elif board[row][col] == word[idx]:
                self.in_path[row][col] = True
                self.path.append(board[row][col])
                for i,j in ([1,0],[-1,0],[0,1],[0,-1]):
                    search(idx+1, row+i, col+j)
                    if self.exisited:
                        return
                self.path.pop()
                self.in_path[row][col] = False



        for row in range(len(board)):
            self.in_path.append([False] * len(board[0]))

        for row in range(len(board)):
            for col in range(len(board[0])):
                search(0, row, col)
                if self.exisited:
                    print(self.exisited)
                    return self.exisited
        print(self.exisited)
        return self.exisited

s = Solution()
s.exist(board = [["A","B","C","D"], ["D", "D", "D", "A"], ["C", "A", "C", "B"], ["A", "B", "C", "C"]], word = "ABCB")
