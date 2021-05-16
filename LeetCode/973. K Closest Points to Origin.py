import math


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def distance(points):
            return math.sqrt((0-points[0])**2 + (0 - points[1])**2)

        neighbours = []
        ans = []
        for i in points:
            neighbours.append((i,distance(i)))

        neighbours.sort(key=lambda x:x[1])
        # print(neighbours)
        for i in range(k):
            ans.append(neighbours[i][0])
        print(ans)
        return ans

s = Solution()
s.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2)