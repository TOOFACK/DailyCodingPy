# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        ans = []
        if n == 1:
            return [TreeNode(0)]
        for i in range(1,n,2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(n-1-i):
                    node = TreeNode(0)
                    node.left = left
                    node.right = right
                    ans.append(node)
        return ans