class Solution(object):

    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        perm = [_ for _ in range(n)]

        perm_to_change = list.copy(perm)
        arr = list.copy(perm)

        def change():
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm_to_change[i // 2]
                else:
                    arr[i] = perm_to_change[n // 2 + (i - 1) // 2]

        change()
        perm_to_change = list.copy(arr)
        # print(perm_to_change)
        ans = 1

        while perm_to_change != perm:
            change()
            perm_to_change = list.copy(arr)
            # print(perm_to_change)
            ans += 1

        print(ans)
        return ans


s = Solution()
s.reinitializePermutation(4)
