import collections


class Solution(object):
    def __init__(self):
        self.count = 0
        self.p = []

    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def dfs(path, parent_idx):

            if path == target and parent_idx + 1 == len(nums):
                # print("path!! = ", path)
                self.count += 1

            if parent_idx + 1 < len(nums):
                dfs(path + nums[parent_idx + 1], parent_idx + 1)

                dfs(path - nums[parent_idx + 1], parent_idx + 1)

        path = -nums[0]

        dfs(path, 0)
        path = nums[0]

        dfs(path, 0)
        print(self.count)


s = Solution()
s.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3)
