# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        fast = head
        slow = head

        while True:

            if fast.next:
                fast = fast.next.next
            else:
                return None

            slow = slow.next

            if not slow or not fast:
                return None

            if slow == fast:
                break

        slow = head

        while True:

            if slow == fast:
                return slow

            slow = slow.next
            fast = fast.next




