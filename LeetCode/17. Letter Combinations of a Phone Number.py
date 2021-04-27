class Solution(object):
    def __init__(self):
        self.ans = []

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        alpha = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def dfs(path, idx):
            print("path =", path)

            print("idx = ", idx)

            if len(path) == len(digits):
                self.ans.append(path)
                return

            for c in alpha[digits[idx]]:
                dfs(path + c, idx + 1)

        if not digits:
            return []
        if len(digits) == 1:
            return [c for c in alpha[digits[0]]]

        for c in alpha[digits[0]]:
            dfs(c, 1)
        return self.ans


s = Solution()
s.letterCombinations("234")
