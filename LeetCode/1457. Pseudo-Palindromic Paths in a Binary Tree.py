# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    ans = 0

    def pseudoPalindromicPaths(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root, vals):
            if not root: return 0

            vals.remove(root.val) if root.val in vals else vals.add(root.val)
            res = 0
            if not root.right and not root.left:
                if len(vals) <= 1:  res = 1
            else:
                res = res + dfs(root.left, vals) + dfs(root.right, vals)
            vals.remove(root.val) if root.val in vals else vals.add(root.val)

            return res

        dfs(root, set())

        return dfs(root, set())
