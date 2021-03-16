class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        tr = False
        for i in range(len(nums)):
            val1 = nums[i]
            for j in range(len(nums)):
                if i != j:
                    if val1+nums[j] == target:
                        ans.append(i)
                        ans.append(j)
                        tr = True
                        break
            if tr:
                return ans
