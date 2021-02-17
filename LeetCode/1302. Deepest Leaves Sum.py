# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    sum = 0
    max_depth = 0

    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root, 1)
        self.dfs_sum(root, 1)

        return self.sum

    def dfs(self, node, depth):
        # print("curr_depth", depth)
        if node:
            if depth > self.max_depth:
                self.max_depth = depth
            self.dfs(node.left, depth + 1)
            self.dfs(node.right, depth + 1)

    def dfs_sum(self, node, depth):
        # print("curr_depth", depth)
        # print("val", node.val)
        if node:
            if depth == self.max_depth:
                self.sum += node.val
            self.dfs_sum(node.left, depth + 1)
            self.dfs_sum(node.right, depth + 1)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node4.left = node7

node6.left = node8

s = Solution()
s.deepestLeavesSum(node1)