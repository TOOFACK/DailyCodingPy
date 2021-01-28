def solution(node, idx):
    head = node
    tempNode = node
    if idx == 0:
        return node.next_item

    i = 0
    while i != idx:
        node = node.next_item
        i += 1
    node_to_delete = node

    if node_to_delete.next_item is None:
        i = 0
        while i != idx - 1:
            tempNode = tempNode.next_item
            i += 1
        tempNode.next_item = None
        return head
    else:
        i = 0
        while i != idx +1:
            if i == idx -1:
                new_prev = tempNode
            tempNode = tempNode.next_item
            i += 1
        new_next = tempNode
        new_prev.next_item = new_next
        node_to_delete.next_item = None
        return head

# def solution1(node):
#     print(node.value)
#     while node.next_item is not None:
#         node = node.next_item
#         print(node.value)
#
#
# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item
#
#
# n4 = Node("4")
# n3 = Node("3", n4)
# n2 = Node("2", n3)
# n1 = Node("1", n2)
#
#
# solution1(solution(n1, 0))
