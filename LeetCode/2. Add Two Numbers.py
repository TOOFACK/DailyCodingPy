# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode((l1.val + l2.val) % 10)

        def go(n1, n2, ost):
            if n1:
                if n2:
                    sumR = n1.val + n2.val + ost
                    node = ListNode(sumR % 10)

                    if n1.next:
                        if n2.next:
                            node.next = go(n1.next, n2.next, sumR // 10)
                            return node
                        else:
                            node.next = go(n1.next, None, sumR // 10)
                            return node
                    else:
                        if sumR > 9:
                            node.next = ListNode(sumR // 10)
                            return node
                        else:
                            return node
                else:
                    sumR = n1.val + ost
                    node = ListNode(sumR % 10)

                    if n1.next:
                        node.next = go(n1.next, None, sumR // 10)
                        return node
                    else:

                        if sumR > 9:
                            node.next = ListNode(sumR//10)
                            return node
                        else:
                            return node
            else:
                if ost >0:
                    node = ListNode(ost)
                    return node

        len1 = 1
        n1 = l1
        while n1.next:
            n1 = n1.next
            len1 += 1

        len2 = 1
        n2 = l2
        while n2.next:
            n2 = n2.next
            len2 += 1
        if len1 > len2:
            ans.next = go(l1.next, l2.next, (l1.val + l2.val) // 10)
        else:
            ans.next = go(l2.next, l1.next, (l2.val + l1.val) // 10)
        return ans
