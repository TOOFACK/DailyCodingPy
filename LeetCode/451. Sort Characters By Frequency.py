class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        ans = ""
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
        # print(d)
        for i in d.keys():
            print(i*d[i], end="")
            ans += i*d[i]
        return ans

s = Solution()
s.frequencySort("Aabb")