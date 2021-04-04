class Solution(object):

    def __init__(self):
        self.ans = []

    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        right_idx = {c: i for i, c in enumerate(S)}
        print(right_idx)

        left, right = 0, 0

        for i, l in enumerate(S):

            right = max(right, right_idx[l])

            if i == right:
                self.ans.append((right - left) + 1)
                left = right + 1

        print(self.ans)
        return self.ans


s = Solution()
s.partitionLabels("ababcbacadefegdehijhklij")
