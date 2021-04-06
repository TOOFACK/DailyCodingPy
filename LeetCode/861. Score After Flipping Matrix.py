class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for row in range(len(A)):
            if A[row][0] == 0:
                for col in range(len(A[0])):
                    A[row][col] = 1 - A[row][col]

        M = len(A[0])
        two = 1
        ans = 0

        for col in range(M-1,-1,-1):
            summ = sum(A[row][col] for row in range(len(A)))
            ans += two*max(summ, len(A) - summ)
            two *= 2
        return ans


