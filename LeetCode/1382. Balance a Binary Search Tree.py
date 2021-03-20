# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def balanceBST(self, root):
        arr = []

        def preoder(root):
            if root:
                preoder(root.left)
                arr.append(root.val)
                preoder(root.right)

        preoder(root)

        def bst(v):
            if v:
                mid = len(v) // 2
                new_root = TreeNode(v[mid])
                new_root.left = bst(v[:mid])
                new_root.right = bst(v[mid + 1:])
                return new_root
            else:
                return None
        bst(arr)