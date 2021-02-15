# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        visited = {}
        return self.dfs(cloned, visited, target)

    def dfs(self, node, visited, target):
        if node is not None:
            if not node in visited:
                if len(visited) == target:
                    print("found!")
                    print(node.val)
                    return node
                print(node.val)
                visited.append(node)
                for i in [node.left, node.right]:
                    self.dfs(i, visited, target)


node = TreeNode(7)
node2 = TreeNode(4)
node.left = node2
node3 = TreeNode(3)
node.right = node3
node4 = TreeNode(6)
node3.left = node4
node5 = TreeNode(19)
node3.right = node5
s = Solution()
v = []
s.dfs(node, v, 3)

