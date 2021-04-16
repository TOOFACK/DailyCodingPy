import collections


class Solution(object):
    def __init__(self):
        self.ans = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def build(arr, utils):
            # print(arr)

            if len(arr) == len(nums):
                self.ans.append(list.copy(arr))
                return

            for i in nums:
                if i in utils:
                    utils.remove(i)
                    arr.append(i)
                    build(arr, utils)
                    arr.pop()
                    utils.add(i)

        utils = set(nums)
        arr = []
        for i in nums:
            utils.remove(i)
            arr.append(i)
            build(arr, utils)
            arr.pop()
            utils.add(i)
        print(self.ans)
        return self.ans


s = Solution()
s.permute(nums=[1, 2, 3])
