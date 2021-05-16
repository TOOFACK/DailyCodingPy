class Solution(object):
    def __init__(self):
        self.was = set()
        self.ans = ""

    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """

        self.ans = "9"*len(s)

        def dfs(s):
            print(s)
            if s not in self.was:
                self.was.add(s)
                if s < self.ans:
                    self.ans = s
                tmp = ""
                for i in range(len(s)):
                    if i % 2 == 1:
                        tmp += str((int(s[i]) + a)%10)
                    else:
                        tmp += s[i]
                dfs(tmp)
                tmp = s[len(s) - b:] + s[0:len(s) - b]
                dfs(tmp)




        dfs(s)
        print("ans = ", self.ans)
        return self.ans

s= Solution()
s.findLexSmallestString(s = "5525", a = 9, b = 2)