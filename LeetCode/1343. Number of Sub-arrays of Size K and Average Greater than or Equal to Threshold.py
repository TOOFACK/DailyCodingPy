import collections


class Solution(object):
    def __init__(self):
        self.window = collections.deque()
        self.ans = []
        self.sumy = 0

    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        self.window = collections.deque()
        for i in range(k+1):
            self.window.append(arr[i])
        self.sumy = sum(self.window)

        if self.sumy /k >= threshold:
            self.ans.append(list(self.window))

        for i in range(k+1, len(arr)):
            self.sumy -= self.window.popleft()
            self.window.append(arr[i])
            self.sumy += self.window[-1]
            if self.sumy / k >= threshold:
                self.ans.append(list(self.window))

        return self.ans

