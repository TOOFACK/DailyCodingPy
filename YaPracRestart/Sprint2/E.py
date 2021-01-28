def solution(node: DoubleConnectedNode):
    tempPrevN = node.next
    tempNextN = None
    while tempPrevN is not None:
        node.next = tempNextN
        node.prev = tempPrevN
        tempNextN = node
        node = node.prev
        tempPrevN = node.next
    node.next = tempNextN
    node.prev = tempPrevN
    return node


