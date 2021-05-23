from collections import defaultdict


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = defaultdict(int)
        pref = 0
        ans = 0
        d[pref] += 1

        for i in range(len(nums)):
            # sum(L,R) = sum(0,R) - sum(0,L-1)==k
            # sum(0,L-1) = sum(0,R) - k
            pref += nums[i]
            need = pref - k
            ans += d[need]
            d[pref] += 1

        print(d)
        print(ans)
        return ans
