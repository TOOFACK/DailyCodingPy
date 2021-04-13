# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.DCA = 0
        self.lca = None

    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(root, depth):
            self.DCA = max(depth, self.DCA)
            if not root:
                return depth
            left = dfs(root.left, depth+1)
            right = dfs(root.right, depth+1)

            if left == right == self.DCA:
                self.lca = root

            return max(left, right)

        dfs(root, 0)
        return self.lca