# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans = 0
        self.depth = 0

    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(root, depth):
            self.depth = max(self.depth, depth)
            if not root:
                return depth
            l = dfs(root.left, depth+1)
            r = dfs(root.right, depth +1)

            if l == r == self.depth:
                self.ans = root
            return max(l, r)

        dfs(root,0)
        return self.ans
