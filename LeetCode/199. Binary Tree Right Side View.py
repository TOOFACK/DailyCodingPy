# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        q = collections.deque()
        ans = []
        q.append(root)

        def bfs(root):
            while q:
                l = 0
                for n in q:
                    if l == len(q) - 1:
                        ans.append(n)
                    l += 1
                for i in range(len(q)):
                    n = q.popleft()
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
        print(ans)
        return ans
