class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        if not target:
            return 0
        i = 0
        curr = target[i]
        n = 1
        while i < len(target):
            if curr != target[i]:
                curr = target[i]
                n += 1
                i += 1
            else:
                i += 1
        if target[0] == "0":
            print(n-1)
            return n-1
        else:
            print(n)
            return n
