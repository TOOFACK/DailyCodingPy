# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1, a: int, b: int, list2):
        ida = idb = None
        n1 = list1
        idx = 0
        while n1:

            print(n1.val)

            if idx == a - 1:
                ida = n1
            if idx == b + 1:
                idb = n1
            n1 = n1.next
            idx += 1

        print("ida", ida.val)
        print("idb", idb.val)

        n2 = list2

        while n2.next is not None:
            n2 = n2.next

        # print("last.next", n2.next.val)
        ida.next = list2
        n2.next = idb
        # print("last.next", n2.next.val)

        return list1


node0 = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node0_b = ListNode(100)
node1_b = ListNode(101)
node2_b = ListNode(102)

node0_b.next = node1_b
node1_b.next = node2_b
s = Solution()
new_no1 = s.mergeInBetween(node0, 3, 4, node0_b)

print("ans")
while new_no1.next is not None:
    print(new_no1.val)
    new_no1 = new_no1.next
