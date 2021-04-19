class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}

        for word in strs:
            k = tuple(sorted(word))
            if k in d:
                d[k].append(word)
            else:
                d[k] = [word]
        return d.values()
