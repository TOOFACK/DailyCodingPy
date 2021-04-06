class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])

        prev_sum = [[0]*(n+1) for _ in range(m+1)]
        ans = [[0] * (n) for _ in range(m)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                prev_sum[i][j] = mat[i-1][j-1] + prev_sum[i-1][j] + prev_sum[i][j-1]- prev_sum[i-1][j-1]

        for i in range(1, m+1):
            for j in range(1, n+1):
                end_j = min(n, j+K)
                end_i = min(m, i+K)

                start_i = max(1, i-K)
                start_j = max(1, j-K)

                ans[i-1][j-1] = prev_sum[end_i][end_j] - prev_sum[start_i-1][end_j] - prev_sum[end_i][start_j-1]+prev_sum[start_i-1][start_j-1]

        return ans