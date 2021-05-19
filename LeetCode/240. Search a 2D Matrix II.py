class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        found = False

        def bin_search(mas, target):
            l = 0
            r = len(mas) - 1

            while l <= r:
                mid = (l + r) // 2
                if mas[mid] < target:
                    l = mid + 1
                elif mas[mid] > target:
                    r = mid -1
                else:
                    return mid
            return -1

        for i in matrix:
            tmp = i
            ans = bin_search(tmp, target)
            if ans > -1 and tmp[ans] == target:
                found = True
                break
        return found
