# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.res = 0

    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root):
            if root:
                left = dfs(root.left)
                right = dfs(root.right)
                self.res += abs(left) + abs(right)
                return root.val + left + right - 1
            else:
                return 0

        dfs(root)
        return self.res
