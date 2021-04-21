# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        lvls = {}

        def dfs(l, root):
            if root:
                if l in lvls:
                    lvls[l].append(root)
                else:
                    lvls[l] = [root]
                dfs(l + 1, root.left)
                dfs(l + 1, root.right)

        dfs(1, root)
        ans = []
        for l in list(lvls.keys()):
            ans.append(lvls[l])

        q = collections.deque()
        q.append(root)
        ans2 = []

        def bfs(node):
            while q:
                tmp = []
                for node in q:
                    tmp.append(node.val)
                    print(node.val)
                ans2.append(list.copy(tmp))

                l = len(q)
                for i in range(l):
                    n = q.popleft()
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
        if not root:
            return []
        bfs(root)

