# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        tr = False

        while True:

            slow = slow.next

            if fast.next:
                fast = fast.next.next
            else:
                return False

            if not(slow and fast):
                return False

            if slow == fast:
                return True

