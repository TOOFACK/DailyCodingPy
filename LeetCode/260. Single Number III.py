class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = set()
        for i in nums:
            if i in a:
                a.remove(i)
            else:
                a.add(i)
        return list(a)