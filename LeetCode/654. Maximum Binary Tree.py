# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        _max = -1
        for i in nums:
            if i > _max:
                _max = i

        root = TreeNode(_max)
        idx = nums.index(_max)
        arr1 = nums[:idx]
        arr2 = nums[idx + 1:]
        root.left = self.constructor(arr1, root)
        root.right = self.constructor(arr2, root)
        return root

    def constructor(self, arr, root):

        if len(arr) > 1:
            _max = -1
            for i in arr:
                if i > _max:
                    _max = i
            idx = arr.index(_max)
            arr1 = arr[:idx]
            arr2 = arr[idx + 1:]
            n_root = TreeNode(_max)
            n_root.left = self.constructor(arr1, n_root)

            n_root.right = self.constructor(arr2, n_root)

            return n_root

        elif not arr:
            return None
        else:
            return TreeNode(arr[0])

    def dfs(self, roo):

        if roo:
            self.dfs(roo.left)

            self.dfs(roo.right)


s = Solution()
s.dfs(s.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]))
