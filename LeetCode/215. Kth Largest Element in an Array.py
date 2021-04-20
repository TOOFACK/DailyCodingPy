class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot = nums[len(nums)//2]
        left = [x for x in nums if x > pivot]
        right = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]

        if k <= len(left):
            return self.findKthLargest(left, k)
        elif k > len(left) + len(mid):
            return self.findKthLargest(right, k - len(left) - len(mid))
        else:
            return mid[0]