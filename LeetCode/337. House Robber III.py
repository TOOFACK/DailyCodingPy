# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.sub_sum = [0] * 100000
        self.added = [False] * 100000
        self.max = [0] * 100000

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def decision(node):
            if not node:
                return [0, 0]

            [leftRob, leftNotRob] = decision(node.left)

            [rightRob, rightNotRob] = decision(node.right)

            robD = node.val + leftNotRob + rightNotRob
            notRob = max(leftRob + rightRob, leftNotRob + rightRob, leftRob + rightNotRob, leftNotRob + rightNotRob)

            return [robD, notRob]

        return max(decision(root))