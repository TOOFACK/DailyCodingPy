class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        ans = []
        for i in range(len(l)):
            tmp = nums[l[i]:r[i]+1]
            tmp = sorted(tmp)
            is_arifmetic = True
            for j in range(0,len(tmp)-1):
                if tmp[1] - tmp[0] != tmp[j+1]-tmp[j]:
                    is_arifmetic = False
                    break
            ans.append(is_arifmetic)
        print(ans)

s=Solution()
s.checkArithmeticSubarrays([-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10])