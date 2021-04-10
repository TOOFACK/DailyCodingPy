class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans = []
        maxes = set()

        for x in range(len(arr), 1, -1):
            i = arr.index(x)
            ans.extend([i+1, x])
            arr = arr[:i:-1] + arr[:i]
        return ans



s = Solution()
s.pancakeSort([3, 2, 4, 1])
