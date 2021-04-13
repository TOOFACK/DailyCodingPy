def helper(node, parent, to_del):
    if node:
        node_del = False
        if node.val in to_del:
            node_del = True
            node.left = helper(node.left, False, to_del)
            node.right = helper(node.right, False, to_del)

        else:
            node.left = helper(node.left, True, to_del)
            node.right = helper(node.right, True, to_del)

        if not parent and not node_del:
            ans.append(node)

        if node_del:
            return None
        else:
            return node
    else:
        return None