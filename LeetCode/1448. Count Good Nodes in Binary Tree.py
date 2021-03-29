# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    ans = 0

    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root, m):
            if root:
                if root.val >= m:
                    self.ans += 1
                dfs(root.left, max(m, root.val))
                dfs(root.right, max(m, root.val))

        dfs(root, root.val)

        return self.ans
