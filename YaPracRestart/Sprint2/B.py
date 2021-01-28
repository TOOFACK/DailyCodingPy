def solution(node):
    print(node.value)
    while node.next_item is not None:
        node = node.next_item
        print(node.value)

#
# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item
#
#
# n4 = Node("4")
# n3 = Node("3", n4)
# n2 = Node("2",n3)
# n1 = Node("1",n2)
# solution1(n1)
