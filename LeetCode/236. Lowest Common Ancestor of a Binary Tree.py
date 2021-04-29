# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def dfs(root):
            if root:
                l = dfs(root.left)
                r = dfs(root.right)

                if l is None or r is None:
                    return
                elif l and (root.val == p.val or root.val == q.val) or r and (root.val == p.val or root.val == q.val):
                    self.ans = root
                    return
                elif l == r == True:
                    self.ans = root
                    return
                elif root.val == p.val or root.val == q.val or l or r:
                    return True
                else:
                    return False
            else:
                return False

        dfs(root)
        return self.ans


n1 = TreeNode(3)
n2 = TreeNode(5)
n3 = TreeNode(2)
n4 = TreeNode(6)
n5 = TreeNode(1)
n6 = TreeNode(7)
n7 = TreeNode(4)
n8 = TreeNode(0)
n9 = TreeNode(8)

n1.left = n2
n1.right = n5

n2.left = n4
n2.right = n3

n3.left = n6
n3.right = n7

n5.left = n8
n5.right = n9

s = Solution()
s.lowestCommonAncestor(n1, n2, n3)
