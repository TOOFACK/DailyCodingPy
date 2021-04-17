import collections


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans = [0]*len(T)
        stack = []
        for i, t in enumerate(T):
            print("i = ", i)
            print("t = ",t)
            while stack and T[stack[-1]] < t:
                print("stack = ", stack)
                cur = stack.pop()
                print("curr = ", cur)
                ans[cur] = i - cur
            stack.append(i)
        print(ans)
        return ans[::-1]


s = Solution()
s.dailyTemperatures(T=[73, 74, 75, 71, 69, 72, 76, 73])
