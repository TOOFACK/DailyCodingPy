# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.tr = True

    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs_canon(root):
            if root:
                if root.left and root.right:
                    if root.left.val > root.right.val:
                        tmp_node = root.left
                        root.left = root.right
                        root.right = tmp_node
                else:
                    if root.right:
                        root.left = root.right
                        root.right = None
                dfs_canon(root.left)
                dfs_canon(root.right)

        def dfs(root1, root2):
            if root1 and root2 and self.tr:
                if root1.val != root2.val:
                    self.tr = False
                else:
                    dfs(root1.left, root2.left)
                    if self.tr:
                        dfs(root1.right, root2.right)

            if root1 and not root2 or root2 and not root1:
                self.tr = False

        dfs_canon(root1)
        dfs_canon(root2)
        dfs(root1, root2)
        return self.tr








