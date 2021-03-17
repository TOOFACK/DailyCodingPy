class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        matrix = []
        for i in range(len(rowSum)):
            matrix.append([0] * len(colSum))

        print(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                min_val = min(rowSum[i], colSum[j])

                matrix[i][j] = min_val
                rowSum[i] -= min_val
                colSum[j] -= min_val
                # print("str = ", i)
                # print("col = ", j)
                # print("minVal = ", min_val)
                # print("matrix", matrix)
                # print("rowSum = ", rowSum)
                # print("colSum = ", colSum)
        return matrix


s = Solution()
s.restoreMatrix([14,9], [6,9,8])
