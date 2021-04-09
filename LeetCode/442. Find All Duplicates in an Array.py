class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for v in nums:
            if nums[abs(v)-1] < 0:
                ans.append(abs(v))
            else:
                nums[abs(v)-1]*=-1

        # print(ans)
        return ans

s = Solution()
s.findDuplicates([4,3,2,7,8,2,3,1])