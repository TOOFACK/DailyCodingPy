class Solution(object):
    def __init__(self):
        self.ans = set()
        self.alpha = {}

    def dfs(self, dict, stroka, leng):
        # print("dict = ", dict)
        # print("str = ", stroka)
        if len(stroka) == leng:
            self.ans.add(stroka)
        for i in list(dict.keys()):
            if dict[i] != 0:
                dict[i] -= 1
                self.dfs(dict, stroka + str(i), leng)
                dict[i] += 1
                self.ans.add(stroka)

    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        for i in tiles:
            if i in self.alpha:
                self.alpha[i] += 1
            else:
                self.alpha[i] = 1
        leng = len(tiles)
        # print("leng = ", leng)
        # print(self.alpha)

        for i in list(self.alpha.keys()):
            self.alpha[i] -= 1
            self.dfs(self.alpha, str(i), leng)
            self.alpha[i] += 1

        # print(self.ans)
        # print(len(self.ans))
        return len(self.ans)
s = Solution()
s.numTilePossibilities("A")