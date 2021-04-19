class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        ans = []
        curr = 0
        using = []

        def all_comb(curr_sum, using, idx):
            # print("using = ", using)
            # print("curr_sum = ", curr_sum)
            if curr_sum == target:
                ans.append(list.copy(using))
                return
            if curr_sum > target:
                return

            for i, val in enumerate(candidates):
                if i >= idx:
                    using.append(val)
                    all_comb(curr_sum + val, using, i)
                    using.pop()

        for i, val in enumerate(candidates):
            using.append(val)
            all_comb(curr + val, using, i)
            using.pop()
        print(ans)
        return ans


s = Solution()
s.combinationSum(candidates = [2,3,5], target = 8)
