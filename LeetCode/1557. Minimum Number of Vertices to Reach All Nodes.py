class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ans = set()
        for v1,v2 in edges:
            ans.add(v1)
        for v1,v2 in edges:
            if v2 in ans:
                ans.discard(v2)
        return ans