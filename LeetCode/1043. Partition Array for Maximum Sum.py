class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # def find_max(arr, i, j):
        #     tmp  = []
        #     for idx in range(i-j,i):

        dp = [0] * (len(arr) + 1)
        for i in range(1, (len(arr) + 1)):
            for j in range(1, k + 1):
                print("i = ", i)
                print("j = ", j)
                if i >= j:
                    # max = find_max(arr, i,j)

                    if dp[i] < dp[i - j] + (max(arr[i - j:i])) * j:
                        dp[i] = dp[i - j] + (max(arr[i - j:i])) * j
                    # print("dp[i-j] = ", dp[i-j])
                    # print("max = ", (max(arr[i - j:i])) * j)
                    print(dp[i])
        # print(dp)
        return dp[-1]


s = Solution()
s.maxSumAfterPartitioning(arr=[1, 15, 7, 9, 2, 5, 10], k=3)
