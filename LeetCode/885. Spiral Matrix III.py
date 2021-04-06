class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        i = r0
        j = c0

        left, right = c0, c0
        bottom, top = r0, r0

        res = [[i, j]]

        while top >= 0 or bottom < R or left >= 0 or right < C:
            j += 1
            right += 1
            bottom += 1
            left -= 1
            top -= 1

            while i < bottom:
                if 0 <= i < R and 0 <= j < C:
                    res.append([i, j])
                i += 1

            while j > left:
                if 0 <= i < R and 0 <= j < C:
                    res.append([i, j])
                j -= 1

            while i > top:
                if 0 <= i < R and 0 <= j < C:
                    res.append([i, j])
                i -= 1

            while j < right:
                if 0 <= i < R and 0 <= j < C:
                    res.append([i, j])
                j += 1

            if 0 <= i < R and 0 <= j < C:
                res.append([i, j])

        return res
