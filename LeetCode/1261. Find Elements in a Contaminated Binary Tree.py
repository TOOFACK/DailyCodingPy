# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):


    def __init__(self, root):

        """
        :type root: TreeNode
        """
        self.nodes = set()

        root.val = 0
        self.nodes.add(0)
        self.dfs_init(root)

    def dfs_init(self,root):
        if root:
            if root.left:
                root.left.val = 2 * root.val + 1
                self.nodes.add(2 * root.val + 1)
                self.dfs_init(root.left)
            if root.right:
                root.right.val = 2 * root.val + 2
                self.nodes.add(2 * root.val + 2)
                self.dfs_init(root.right)


    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        if target in self.nodes:
            return True
        else:
            return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
