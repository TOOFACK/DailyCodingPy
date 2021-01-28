def solution(node, elem):
    index = 0
    tr = False
    while node is not None:
        if node.value == elem:
            tr = True
            break
        index += 1
        node = node.next

    if tr:
        return index
    else:
        return -1
