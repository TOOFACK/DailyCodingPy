# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def inorderTraversal(self, root):
        def dfs(root):
            if root:
                dfs(root.left)
                self.ans.append(root.val)
                dfs(root.right)
        dfs(root)
        return self.ans

