class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    visited = []
    dist = {}
    sum = 0

    def sumEvenGrandparent(self, root):

        self.dfs(root)
        print(self.sum)
        return sum

    def dfs(self, node):
        if node not in self.visited and node:
            self.visited.append(node)
            if node.val % 2 == 0:
                if node.left:
                    self.dist[node.left] = node
                if node.right:
                    self.dist[node.right] = node
            if node in self.dist:
                if node.left:
                    self.sum += node.left.val
                if node.right:
                    self.sum += node.right.val

            self.dfs(node.left)
            self.dfs(node.right)


node1 = TreeNode(6)
node2 = TreeNode(7)
node3 = TreeNode(8)
node4 = TreeNode(2)
node5 = TreeNode(7)
node6 = TreeNode(1)
node7 = TreeNode(3)
node8 = TreeNode(9)
node9 = TreeNode(1)
node10 = TreeNode(4)
node11 = TreeNode(5)
node12 = TreeNode(3)
node13 = TreeNode(5)
node14 = TreeNode(8)
node15 = TreeNode(6)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

node4.left = node8

node5.left = node9
node5.right = node10

node7.right = node11

node10.left = node12
node10.right = node13

node12.left = node14

node13.right = node15

s = Solution()
s.sumEvenGrandparent(node1)
