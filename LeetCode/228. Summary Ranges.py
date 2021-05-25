class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i = 0
        ans = []
        temp = [0, "!"]
        while i < len(nums):
            temp[1] = "!"
            temp[0] = (nums[i])
            j = i + 1
            while j < len(nums) and abs(nums[j] - nums[j-1]) == 1:
                temp[1] = nums[j]
                j += 1

            i = j
            if temp[1] != "!":
                ans.append(str(temp[0]) + "->" + str(temp[1]))
            else:
                ans.append(str(temp[0]))
        print(ans)
        return ans

s = Solution()
s.summaryRanges(nums = [0,2,3,4,6,8,9])