import collections
class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        ans = [0] * len(seq)
        A = []
        B = []
        idx = 0
        last_open = 'B'
        for idx, i in enumerate(seq):
            if i == "(":
                if len(A) > len(B):
                    B.append("(")
                else:
                    A.append("(")
                    ans[idx] = 1

            else:
                if len(A) > len(B):
                    A.pop()
                    ans[idx] = 1
                else:
                    B.pop()
        return ans


s = Solution()
s.maxDepthAfterSplit("()(())()")






