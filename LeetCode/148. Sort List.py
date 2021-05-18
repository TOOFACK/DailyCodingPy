# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def printList(head):
            while head:
                print(head.val)
                head = head.next

        def sort(head, lent):
            if lent > 1:

                m = lent // 2
                l = head
                point = head
                i = 1
                # print("m = ", m)

                while i < m:
                    i += 1
                    point = point.next
                # print("point after sub = , ",point.val)
                r = point.next
                point.next = None
                # print('l')
                # printList(l)
                # print("r")
                # printList(r)
                # print()
                l = sort(l, lent // 2)
                r = sort(r, lent - lent // 2)
                # print("after sort")
                # print('l')
                # printList(l)
                # print()
                # print("r")
                # printList(r)

                new_h = None

                while l and r:
                    if l.val < r.val:
                        if not new_h:
                            head = l
                            new_h = l
                            l = l.next
                        else:
                            new_h.next = l
                            l = l.next
                            new_h = new_h.next
                    else:
                        if not new_h:
                            head = r
                            new_h = r
                            r = r.next
                        else:
                            new_h.next = r
                            r = r.next
                            new_h = new_h.next

                while l:
                    new_h.next = l
                    l = l.next
                    new_h = new_h.next

                while r:
                    new_h.next = r
                    r = r.next
                    new_h = new_h.next

            return head



        i = 1
        tmp = head
        while tmp.next:
            i +=1
            tmp = tmp.next
        return sort(head,i)







s = Solution()
n1 = ListNode(3)
n2 = ListNode(2)
n3  = ListNode(1)
n4 = ListNode(-1)
n5 = ListNode(5)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
n1 = s.sortList(n1)
print("sorted")
while n1:
    print(n1.val)
    n1 = n1.next
