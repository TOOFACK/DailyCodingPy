# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    val = 0

    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.reverse_inOder(root)
        return root

    def reverse_inOder(self, node):
        if not node:

            return
        else:
            self.reverse_inOder(node.right)

            node.val = self.val + node.val
            self.val = node.val

            self.reverse_inOder(node.left)


n1 = TreeNode(4)
n2 = TreeNode(1)
n3 = TreeNode(6)
n4 = TreeNode(0)
n5 = TreeNode(2)
n6 = TreeNode(5)
n7 = TreeNode(7)
n8 = TreeNode(3)
n9 = TreeNode(8)

n1.left = n2
n1.right = n3

n2.left = n4
n2.right = n5

n3.left = n6
n3.right = n7

n5.right = n8

n7.right = n9

s = Solution()
s.reverse_inOder(n1)
