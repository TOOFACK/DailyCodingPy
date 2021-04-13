# Definition for a binary tree node.
import ntpath


class Solution(object):
    def delNodes(self, root, to_delete):
        to_del = set(to_delete)
        res = []

        def helper(node, parent, to_del):
            if node:
                node_del = node.val in to_del
                if node_del:
                    node.left = helper(node.left, False, to_del)
                    node.right = helper(node.right, False, to_del)
                else:
                    node.left = helper(node.left, True, to_del)
                    node.right = helper(node.right, True, to_del)

                if not parent and not node_del:
                    res.append(node)

                if node_del:
                    return None
                else:
                    return node

            else:
                return None

        helper(root, True, to_del)
        return res


s = Solution()
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(3)
n5 = TreeNode(5)
n6 = TreeNode(4)
n7 = TreeNode(6)
n8 = TreeNode(7)

n1.left = n2
n1.right = n3

n2.left = n4

n4.left = n5
n4.right = n6

n3.left = n7
n3.right = n8
s.delNodes(n1, [3, 5])
