import collections


class Solution(object):

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """


        # window = collections.deque(s[0:len(p)])
        # need_char = len(p)
        # for i in p:
        #     if i in table:
        #         table[i] += 1
        #     else:
        #         table[i] = 1
        #
        # for i in window:
        #     if i in table:
        #         table[i] -= 1
        #         if table[i] >= 0:
        #             need_char -= 1
        #
        # if need_char == 0:
        #     ans.append(0)
        #
        # print("window = ", window)
        # print("table = ", table)
        # print("needChar = ", need_char)
        #
        # for idx in range(len(p), len(s)):
        #
        #     c_pop = window.popleft()
        #     if c_pop in table:
        #
        #         if table[c_pop] >= 0:
        #             need_char += 1
        #             table[c_pop] += 1
        #
        #     c_add = s[idx]
        #     window.append(c_add)
        #     if c_add in table:
        #         table[c_add] -= 1
        #         if table[c_add] >= 0:
        #             need_char -= 1
        #
        #     if need_char == 0:
        #         ans.append(idx - len(p) + 1)

        table = {}
        ans = []
        count = len(p)

        for i in p:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1

        l = r = 0

        while r < len(s):
            # print("r = ", r)
            # print("l = ", l)
            # print("s[r] = ", s[r])
            # print("s[l] = ", s[l])
            # print("count = ", count)
            # print("table = ", table)
            if s[r] in table:
                table[s[r]] -= 1
                if table[s[r]] >= 0:
                    count -= 1

            if r - l == len(p):
                if s[l] in table:
                    if table[s[l]] >= 0:
                        count += 1
                    table[s[l]] += 1
                l += 1
            r += 1


            if count == 0:
                ans.append(l)



        print(ans)
        return ans


s = Solution()
s.findAnagrams(s="cbaebabacd", p="abc")
