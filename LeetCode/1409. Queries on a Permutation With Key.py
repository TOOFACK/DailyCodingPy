class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        ans = []
        P = []
        for i in range(m):
            P.append(i + 1)

        for i in queries:

            for j in range(len(P)):
                if P[j] == i:
                    tmp = P[j]
                    P.remove(P[j])
                    P.insert(0, tmp)

                    ans.append(j)

                    break

        return ans


s = Solution()
print(s.processQueries([4, 1, 2, 2], 4))
