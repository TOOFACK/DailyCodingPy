# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        def dfs(root):
            if not root:
                return
            else:
                dfs(root.right)
                dfs(root.left)
                root.right = self.prev
                root.left = None
                self.prev = root

        dfs(root)
        return root




one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)

one.left = two
one.right = five

two.left = three
two.right = four

five.right = TreeNode(6)

s = Solution()
s.flatten(one)
