class Solution(object):
    def __init__(self):
        self.ans = [[]]

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def helper(val, sub):

            self.ans.append([list.copy(sub)])
            for idx in range(nums.index(val) + 1, len(nums)):
                sub.append(nums[idx])
                helper(nums[idx], sub)
                sub.pop()

        tmp = []
        for val in nums:
            tmp.append(val)
            helper(val, tmp)
            tmp.pop()
        print(self.ans)


s = Solution()
s.subsets(nums=[1, 3])
