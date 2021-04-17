class Solution(object):
    def __init__(self):
        self.ans = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(str, open, close):

            if open + close == 2*n:
                # print(str)
                self.ans.append(str)
            if open < n:
                generate(str+"(", open+1, close)
            if open > close:
                generate(str+ ")", open, close+1)

        generate("", 0,0)
        return self.ans

s = Solution()
s.generateParenthesis(3)
