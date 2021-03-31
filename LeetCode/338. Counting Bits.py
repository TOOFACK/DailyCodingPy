class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        pow = 1
        dp = [0] * (num+1)
        dp[0] = 0
        for i in range(1,num+1):
            if pow *2 == i:
                pow *= 2
            dp[i] = dp[i - pow] + 1
        return dp
