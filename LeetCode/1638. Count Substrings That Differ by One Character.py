class Solution(object):
    def countSubstrings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        start_i = 0
        i = 0
        start_j = 0
        ans = 0
        dif = 0
        i_end = False

        while True:
            if start_j == len(t):
                start_j = 0
                start_i += 1
                i = start_i
            if i == len(s):
                break

            # print("start_i = ", i)
            # print("start_j = ", start_j)

            for j in range(start_j, len(t)):
                # print("i = ", i)
                # print("j = ", j)
                # print("s_i = ", s[i])
                # print("t_j = ", t[j])

                if s[i] != t[j]:

                    dif += 1
                    # print("dif = ", dif)
                    if dif > 1:
                        break
                    else:
                        ans += 1
                        # print("ans = ", ans)
                elif dif != 0:
                    ans += 1
                    # print("ans = ", ans)
                i += 1
                if i == len(s):
                    break

            start_j += 1
            i = start_i
            dif = 0

        # print(ans)
        return ans


s = Solution()
s.countSubstrings("abe", "bbc")
