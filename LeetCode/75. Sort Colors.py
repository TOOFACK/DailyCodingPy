class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        beg, mid, end = 0, 0, len(nums) - 1

        while mid <= end:
            if nums[mid] == 0:
                nums[mid], nums[beg] = nums[beg], nums[mid]
                beg += 1
                mid += 1

            elif nums[mid] == 2:
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1

            else:
                mid += 1
        return nums


s = Solution()
s.sortColors(nums=[2, 0, 2, 1, 1, 0, 1, 2, 2, 0, 0])
