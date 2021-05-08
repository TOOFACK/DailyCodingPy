class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        d = {x[0]: x[1] for x in knowledge}

        keys = set()

        curr = ""
        ans = s

        for i in range(len(s)):
            if s[i] == "(":
                j = i + 1
                while s[j] != ")":
                    curr += s[j]
                    j += 1
                print("curr = ", curr)
                if curr in d:
                   ans= ans.replace("(" +curr+")", d[curr])
                else:
                    ans=ans.replace("(" + curr + ")", "?")
                i = j
                curr = ""
        ans = ans.replace("(", "")
        ans = ans.replace(")", "")
        print(ans)
        return ans
        # print(keys)
        # s = s.replace("(", ")")
        # arr = s.split(")")
        # print(arr)
        # print(d)
        # for i in range(len(arr)):
        #
        #     if arr[i] in keys:
        #
        #         if arr[i] in d:
        #
        #             arr[i] = d[arr[i]]
        #         else:
        #
        #             arr[i] = "?"
        #
        # ans = ""
        # for i in arr:
        #     print(i, end="")
        #     ans+=i
        # return ans


s = Solution()
s.evaluate(s="(name)is(age)yearsold", knowledge=[["name", "bob"], ["age", "two"]])
