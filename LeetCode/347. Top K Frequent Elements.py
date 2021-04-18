class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        ans = []

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for key in sorted(freq, key=freq.get, reverse=True):
            ans.append(key)
            # print(key)
            k -= 1
            if k == 0:
                break
            # print(k)
        # print(ans)
        return ans

s = Solution()
s.topKFrequent(nums = [1,1,1,2,2,3], k = 2)
