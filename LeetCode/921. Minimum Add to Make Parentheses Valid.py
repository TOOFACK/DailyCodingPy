import collections


class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = collections.deque()
        ans = len(S)

        for s in S:
            if s == "(":
                stack.append("(")
            elif stack:
                stack.pop()
                ans -=2

        return ans

