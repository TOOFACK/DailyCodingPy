# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def removeLeafNodes(self, root, target):

        def dfs_util(root):
            if root:
                if root.left:
                    root.left = dfs_util(root.left)
                if root.right:
                    root.right = dfs_util(root.right)
                if root.left is None and root.right is None and root.val == target:
                    return None
                else:
                    return root

        root.left = dfs_util(root.left)
        root.right = dfs_util(root.right)
        if root.left is None and root.right is None and root.val == target:
            return None
        else:
            return root

