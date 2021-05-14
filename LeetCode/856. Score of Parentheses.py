class Solution(object):
    def __init__(self):

        self.stack = [0]


    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        for i in s:
            if i == "(":
                self.stack.append(0)
            else:
                l = self.stack.pop()
                self.stack[-1] += 2*l or 1



        return self.stack.pop()
