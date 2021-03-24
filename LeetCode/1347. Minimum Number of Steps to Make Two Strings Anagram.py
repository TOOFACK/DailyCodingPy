import collections


class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        c1 = collections.Counter(s)
        c2 = collections.Counter(t)
        ans = 0

        for char in c1:
            if char in c2 and c2[char] < c1[char]:
                ans += c1[char] - c2[char]
            elif char not in c2:
                ans += c1[char]

        return ans
