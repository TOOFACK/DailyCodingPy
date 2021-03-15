class Solution:

    def checkArithmeticSubarrays(self, nums, l, r):
        ans = []
        for i in range(len(l)):
            tr_false = False
            temp_arr = nums[l[i]: r[i] + 1]

            list.sort(temp_arr)
            prev_sum = temp_arr[1] - temp_arr[0]
            for j in range(len(temp_arr) - 1):
                if prev_sum != temp_arr[j + 1] - temp_arr[j]:
                    tr_false = True
                    break
            if tr_false:
                ans.append("false")
            else:
                ans.append("true")
        print(ans)
        return ans


s = Solution()
s.checkArithmeticSubarrays([4, 6, 5, 9, 3, 7], [0, 0, 2], [2, 3, 5])
