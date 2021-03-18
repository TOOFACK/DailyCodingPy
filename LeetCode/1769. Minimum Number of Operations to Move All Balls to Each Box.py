class Solution:
    def minOperations(self, boxes: str):
        ans = [0]*len(boxes)
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if i != j and boxes[j] != '0':
                    ans[i]+=abs(i-j)
        return ans