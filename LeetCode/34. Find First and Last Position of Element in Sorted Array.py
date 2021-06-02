class Solution(object):
    def __init__(self):
        self.first = self.second = 0

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def bin_search1(arr, target):
            print("arr = ", arr)
            idx1 = -1
            l = 0
            r = len(arr) - 1

            while l <= r:
                mid = (l + r) // 2
                if arr[mid] == target:
                    idx1 = mid
                    r = mid - 1
                elif arr[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            return idx1

        def bin_search2(arr, target):
            print("arr = ", arr)
            idx2 = -1
            l = 0
            r = len(arr) - 1

            while l <= r:
                mid = (l + r) // 2
                if arr[mid] == target:
                    idx2 = mid
                    l = mid + 1
                elif arr[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            return idx2

        return [bin_search1(nums, target), bin_search2(nums, target)]

s = Solution()

s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8)
