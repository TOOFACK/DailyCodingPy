class Solution(object):

    def __init__(self):
        self.ans = 0

    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """

        start = {}
        end = {}
        abc = set()
        for idx, ch in enumerate(s[:-1]):
            abc.add(ch)
            start[idx] = len(abc)

        abc = set()
        for idx, ch in enumerate(s[:0:-1]):
            abc.add(ch)
            end[idx] = len(abc)

        print(start)
        print(end)

        for i in range(len(start)):
            if start[i] == end[len(end)-1-i]:
                self.ans += 1

        print(self.ans)
        return self.ans


s = Solution()
s.numSplits(s="aacaba")
