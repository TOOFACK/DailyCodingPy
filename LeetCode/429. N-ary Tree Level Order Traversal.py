"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections


class Solution(object):
    def __init__(self):
        self.ans = []

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        q = collections.deque()
        q.append(root)
        while q:
            tmp = []
            for i in range(len(q)):
                r = q.popleft()
                if r.children:
                    for ch in r.children:
                        q.append(ch)

                tmp.append(r.val)
            self.ans.append(tmp.copy())
        return self.ans
