# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def kthSmallest(self, root, k):
        def dfs(root):
            if root:
                dfs(root.left)
                self.ans.append(root.val)
                dfs(root.right)
        dfs(root)
        print(self.ans)
        return self.ans[k-1]


