class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 1:
            fast = 0
            slow = 0

            while True:
                slow = nums[slow]
                fast = nums[nums[fast]]
                if slow == fast:
                    break
            slow = 0
            while True:
                fast = nums[fast]
                slow = nums[slow]

                if slow == fast:
                    print(slow)
                    return slow



s = Solution()
s.findDuplicate([3, 1, 3, 4, 2])
