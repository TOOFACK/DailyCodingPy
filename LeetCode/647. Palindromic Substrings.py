class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = []
        tmp = [0] * len(s)
        for i in s:
            dp.append(list.copy(tmp))

        ans = 0

        for i in range(len(s)):
            start_j = i
            start_i = 0
            while start_j < len(s) and start_i < len(s):
                print(start_i, start_j)

                if start_j == start_i:
                    ans += 1
                    dp[start_i][start_j] = 1
                elif s[start_j] == s[start_i] and start_j - start_i == 1:
                    ans += 1
                    dp[start_i][start_j] = 1
                elif s[start_j] == s[start_i] and dp[start_i + 1][start_j - 1] == 1:
                    dp[start_i][start_j] = 1
                    ans += 1
                start_j += 1
                start_i += 1
        return ans


s = Solution()
s.countSubstrings("aabaaca")
