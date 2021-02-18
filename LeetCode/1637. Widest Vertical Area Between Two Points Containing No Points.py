class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        lst = []
        for i in points:
            lst.append(i[0])
        lst.sort()
        # print(lst)
        max = -1
        for i in range(len(lst) - 1):
            # print(lst[i + 1])
            # print(lst[i])
            if max < lst[i + 1] - lst[i]:
                max = lst[i + 1] - lst[i]
        return max


s = Solution()
points = [[8,7],[9,9],[7,4],[9,7]]
print(s.maxWidthOfVerticalArea(points))
