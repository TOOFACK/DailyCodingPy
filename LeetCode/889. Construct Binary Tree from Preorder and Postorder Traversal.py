# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre_index = 0
        self.post_index = 0

    def constructFromPrePost(self, pre, post):
        root = TreeNode(pre[self.pre_index])
        self.pre_index += 1

        if root.val != post[self.post_index]:
            root.left = self.constructFromPrePost(pre, post)

        if root.val != post[self.post_index]:
            root.right = self.constructFromPrePost(pre, post)

        self.post_index += 1
        return root
