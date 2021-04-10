import collections
class Solution(object):
    def __init__(self):
        self.ans = set()

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        def comb(stroka, idx):
            # print("idx = ", idx)
            # print("str = ", stroka)
            if len(stroka) == len(S):
                self.ans.add(stroka)
            if idx < len(S):
                if S[idx].isdigit():
                    comb(stroka + S[idx], idx+1)
                else:
                    comb(stroka+S[idx].lower(), idx+1)
                    comb(stroka+S[idx].upper(), idx+1)
        comb("",0)
        # print(self.ans)
        return list(self.ans)

s = Solution()
s.letterCasePermutation("C")