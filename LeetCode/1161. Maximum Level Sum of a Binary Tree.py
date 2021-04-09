import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.lvls = {}

    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, lvl):
            if root:
                dfs(root.left, lvl+1)
                dfs(root.right, lvl+1)
                if lvl in self.lvls:
                    self.lvls[lvl] += root.val
                else:
                    self.lvls[lvl] = root.val
        dfs(root, 1)
        max_lvl = self.lvls[1]
        lvl = 1
        for k in list(self.lvls.keys()):
            if self.lvls[k] > max_lvl:
                max_lvl = self.lvls[k]
                lvl = k

        print(lvl)
        return lvl



n1 = TreeNode(1)
n2 = TreeNode(7)
n3 = TreeNode(0)
n1.left = n2
n1.right = n3
n2.left = TreeNode(7)
n2.right = TreeNode(-8)

s = Solution()
s.maxLevelSum(n1)