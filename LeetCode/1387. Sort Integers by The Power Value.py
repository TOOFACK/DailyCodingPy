class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """

        vals = [_ for _ in range(lo, hi + 1)]
        # print(vals)
        steps_to_1 = {2:1}

        def count(val):
            if val not in steps_to_1:
                if val % 2 == 0:
                    steps_to_1[val] = 1 + count(val//2)
                else:
                    steps_to_1[val] = 1 + count(1 + val*3)
            return steps_to_1[val]

        for i in vals:
            count(i)
        ans = {}
        for i in vals:
            ans[i] = steps_to_1[i]
        print([k for k, v in sorted(ans.items(), key=lambda x : x[1])][k-1])
        return [k for k, v in sorted(ans.items(), key=lambda x : x[1])][k-1]









s = Solution()
s.getKth(12, 15, 2)
