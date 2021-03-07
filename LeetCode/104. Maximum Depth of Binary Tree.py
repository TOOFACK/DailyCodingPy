class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    lenM = 1

    def maxDepth(self, root):

        def dfs(root, currLen):

            if root:

                if currLen > self.lenM:
                    self.lenM = currLen

                dfs(root.left, currLen + 1)

                dfs(root.right, currLen + 1)

        if root:
            dfs(root, 1)
        else:
            return 0

        return self.lenM


root = TreeNode(3)
root.left = TreeNode(9)
n20 = TreeNode(20)
root.right = n20
n20.left = TreeNode(15)
n20.right = TreeNode(7)
s = Solution()
s.maxDepth(root)
