# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(preorder[0])
        l = []
        r = []
        for i in preorder[1:]:
            if i > root.val:
                r = preorder[preorder.index(i):]
                break
            l.append(i)
        print(r)
        print(l)

        root.left =  self.bstFromPreorder_Util(l)
        root.right = self.bstFromPreorder_Util(r)
        return root

    def bstFromPreorder_Util(self, preorder):

        if preorder:
            node = TreeNode(preorder[0])

            l = []
            r = []
            for i in preorder[1:]:
                if i > node.val:
                    r = preorder[preorder.index(i):]
                    break
                l.append(i)
            node.left = self.bstFromPreorder_Util(l)

            node.right = self.bstFromPreorder_Util(r)
            return node

        else:
            return None








s = Solution()
s.bstFromPreorder([8,5,1,7,10,12])

