import collections
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans = []
        for w in words:
            if len(set(pattern)) == len(set(w)) == len(set(zip(pattern,w))):
                ans.append(w)

        return ans
