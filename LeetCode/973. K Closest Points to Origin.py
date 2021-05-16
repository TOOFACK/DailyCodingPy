import heapq
import math


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        def distance(points):
            return math.sqrt((0 - points[0]) ** 2 + (0 - points[1]) ** 2)

        neighbours = []

        for i in points:
            heapq.heappush(neighbours, (distance(i), i))


        # print(neighbours)
        # ans  = (heapq.nsmallest(k,neighbours))
        print([point[1] for point in heapq.nsmallest(k , neighbours)])
        # return ans


s = Solution()
s.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2)
