class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_curr = min(height[0], height[-1]) * (len(height) - 1)
        shortest_side_idx = 0 if height[0] < height[-1] else 1

        start = 0
        end = len(height) - 1
        while start != end:
            if shortest_side_idx == 0:
                start += 1
            else:
                end -= 1
            if height[start] < height[end]:
                shortest_side_idx = 0
            else:
                shortest_side_idx = 1
            if min(height[start], height[end]) * (end - start) > max_curr:
                max_curr = min(height[start], height[end]) * (end - start)

        return max_curr
