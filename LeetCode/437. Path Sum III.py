# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans = 0

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """

        # def helper(root, sum_p):
        #     if not root:
        #         return 0
        #     if root.val == sum_p:
        #         return 1 + helper(root.left, sum_p - root.val) + helper(root.right, sum_p - root.val)
        #     else:
        #         return helper(root.left, sum_p - root.val) + helper(root.right, sum_p - root.val)
        #
        # if not root:
        #     return 0
        # return self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum) + helper(root, targetSum)
        #
        #

        summary = {0: 1}

        def helper(root, r_sum, t):
            if not root:
                return 0
            r_sum += root.val

            if r_sum - t in summary:
                cnt = summary[r_sum - t]

            else:
                cnt = 0

            if r_sum in summary:
                summary[r_sum] = summary[r_sum] + 1
            else:
                summary[r_sum] = 1

            cnt += helper(root.left, r_sum, t) + helper(root.right, r_sum, t)
            summary[r_sum] = summary[r_sum] - 1
            return cnt

        return helper(root, 0, targetSum)
