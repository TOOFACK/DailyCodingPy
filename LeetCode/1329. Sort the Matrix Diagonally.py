import collections

class Solution:
    def diagonalSort(self, mat):
        # print(mat)
        diag = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if (i-j) in diag:
                    tmp = diag[(i-j)]
                    tmp.append(mat[i][j])
                    diag[(i-j)] = tmp
                else:
                    tmp = [mat[i][j]]
                    diag[(i-j)] = tmp

        # print(diag)
        for i in list(diag.keys()):
            diag[i] = collections.deque(sorted(diag[i]))
        # print(diag)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = diag[(i-j)].popleft()
                # print((i-j))
                # print(diag)


        return mat






s = Solution()
s.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]])

