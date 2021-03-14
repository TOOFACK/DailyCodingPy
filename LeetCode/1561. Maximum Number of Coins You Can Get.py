class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        idx = int(len(piles)/3)

        return sum(piles[idx::2])






s = Solution()
print(s.maxCoins([2, 4, 1, 2, 7, 8]))
print(s.maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]))
