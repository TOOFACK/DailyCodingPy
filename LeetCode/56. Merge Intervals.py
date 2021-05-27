class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals = sorted(intervals, key=lambda x : x[0])
        ans = []

        idx = 0

        while idx < len(intervals):
            start = intervals[idx]
            j = idx + 1

            while j < len(intervals):

                if start[1] < intervals[j][0]:
                    break
                elif start[1] >= intervals[j][1]:
                    start= [start[0], start[1]]

                elif start[1] <= intervals[j][1]:
                    start = [start[0], intervals[j][1]]



                j += 1
            ans.append(start)
            idx = j


        print(ans)
        return ans

s = Solution()
s.merge(intervals =

[[1,3],[2,6],[8,10],[15,18]])