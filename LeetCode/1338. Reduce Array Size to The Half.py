class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = {}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        freq_sorted = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        min = len(arr)//2
        ans = []
        new_len = 0
        for val in list(freq_sorted.keys()):
            new_len = freq_sorted[val] + new_len

            if len(arr) - new_len <= min:
                ans.append(val)
                break
            else:
                ans.append(val)


        # print(ans)
        # print(freq)
        # print(freq_sorted)
        # print(freq_sorted.keys())
        return len(ans)

s = Solution()
s.minSetSize(arr = [1,2,3,4,5,6,7,8,9,10])