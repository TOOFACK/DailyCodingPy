import collections


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(T)
        stack = []

        for idx, temp in enumerate(T):
            while stack and T[stack[-1]] < temp:
                curr = stack.pop()
                ans[curr] = idx - curr
            stack.append(idx)
        return  ans







s = Solution()
s.dailyTemperatures(T=[73, 74, 75, 71, 69, 72, 76, 73])
