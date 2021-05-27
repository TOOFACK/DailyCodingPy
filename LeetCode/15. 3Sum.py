class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ans = []
        # print("nums = ", nums)

        for idx in range(len(nums)- 2):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue

            # print("a = ", nums[idx])
            l = idx + 1
            r = len(nums) - 1

            # print("nums[l] = ", nums[l])
            # print("nums[r] = ", nums[r])
            # print("l = ", l)
            # print("r = ", r)

            while l < r:

                # print("nums[l] = ", nums[l])
                # print("nums[r] = ", nums[r])
                # print("l = ", l)
                # print("r = ", r)

                if nums[idx] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[idx] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    ans.append([nums[idx], nums[l], nums[r]])
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                    l += 1

        print(ans)
        return ans


s = Solution()
s.threeSum(
[-1,0,1,2,-1,-4,-2,-3,3,0,4]
     )
