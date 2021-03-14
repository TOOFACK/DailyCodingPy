# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def getAllElements(self, root1, root2):

        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        order1 = []
        order2 = []

        def dfs1(root):
            if root:
                dfs1(root.left)
                order1.append(root.val)
                dfs1(root.right)

        def dfs2(root):
            if root:
                dfs2(root.left)
                order2.append(root.val)
                dfs2(root.right)

        def merge(order1, order2):
            res = []
            it1 = 0
            it2 = 0

            while it1 < len(order1) and it2 < len(order2):
                if order1[it1] < order2[it2]:
                    res.append(order1[it1])
                    it1 += 1
                else:
                    res.append(order2[it2])
                    it2 += 1

            if it1 == len(order1):
                res.extend(order2[it2:])
            elif it2 == len(order2):
                res.extend(order1[it1:])

            return res

        dfs1(root1)
        dfs2(root2)


        return merge(order1, order2)


r1 = TreeNode(2)
r1.left = TreeNode(1)
r1.right = TreeNode(4)

r2 = TreeNode(1)
r2.left = TreeNode(0)
r2.right = TreeNode(3)

s = Solution()
s.getAllElements(r1, r2)
