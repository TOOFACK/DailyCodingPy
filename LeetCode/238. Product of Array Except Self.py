class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        p = 1
        for i in nums:
            ans.append(p)
            p *= i
        p = 1
        print(ans)
        for i in range(len(nums)-1,-1,-1):

            ans[i] *= p
            p *= nums[i]

        # print(ans)
        return ans
s = Solution()
s.productExceptSelf([1,2,3,4])