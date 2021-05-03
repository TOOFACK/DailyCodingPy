class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1 = sorted(s1)
        s2 = sorted(s2)
        ans1 = True
        ans2 = True
        for c1, c2 in zip(s1, s2):
            if ord(c1) < ord(c2):
                ans1 = False

        for c1, c2 in zip(s2, s1):
            if ord(c1) < ord(c2):
                ans2 = False

        return ans1 or ans2


