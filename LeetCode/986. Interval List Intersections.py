class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        j = 0
        ans = []
        if len(firstList) == 0 or len(secondList) == 0:
            return []

        while True:
            print(i)
            print(j)
            if i < len(firstList):
                tur1 = firstList[i]
            else:
                tur1 = firstList[len(firstList) - 1]

            if j < len(secondList):
                tur2 = secondList[j]
            else:
                tur2 = secondList[len(secondList) - 1]

            print(tur1)
            print(tur2)

            intersection_start = max(tur1[0], tur2[0])
            intersection_end = min(tur1[1], tur2[1])

            print(intersection_start,intersection_end)

            if intersection_start <= intersection_end:
                ans.append([intersection_start, intersection_end])
                if tur1[1] < tur2[1]:
                    i += 1
                else:
                    j += 1
            elif tur1[1] < tur2[1]:
                i += 1
            else:
                j += 1
            if i >= len(firstList) or j >= len(secondList):
                break
        print(ans)
        return ans


s = Solution()
s.intervalIntersection(firstList = [[1,7]], secondList = [[3,10]])
