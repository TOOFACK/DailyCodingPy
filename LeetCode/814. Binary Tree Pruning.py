# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def dfs(root):

            if root:
                root.left = dfs(root.left)
                root.right = dfs(root.right)
                if root.val == 0 and not root.left and not root.right:
                    return None
                else:
                    return root

        root.left = dfs(root.left)
        root.right = dfs(root.right)

        if root.val == 0 and not root.left and not root.right:
            return None
        else:
            return root


s = Solution()
n1 = TreeNode(1)
n2 = TreeNode(0)
n3 = TreeNode(0)
n1.right = n2
n2.left = n3
n2.right = TreeNode(1)
s.pruneTree(n1)
