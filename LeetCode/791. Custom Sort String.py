class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        appearance = {}
        tmp = set(S)
        ans = ""

        for ch in T:
            if ch in tmp:
                if ch in appearance:
                    appearance[ch] += 1
                else:
                    appearance[ch] = 1
            else:
                ans += ch

        for ch in S:
            if ch in appearance:
                ans += appearance[ch] * ch

        print(ans)
        return ans


s = Solution()
s.customSortString(S="kqep", T="pekeq")
