# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        st = head
        list_arr = []
        list_arr.append(st.val)
        while st.next:
            st = st.next
            list_arr.append(st.val)
        print(list_arr)

        k1 = k - 1
        k2 = len(list_arr) - k - 1

        tmp = list_arr[k1]
        list_arr[k1] = list_arr[k2]
        list_arr[k2] = tmp

        def helper(arr, index):
            if index == len(arr):
                return None
            node = ListNode(arr[index])
            node.next = helper(arr, index + 1)
            return node

        head = ListNode(list_arr[0])
        head.next = helper(list_arr, 1)

        return head


s = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
n8 = ListNode(8)
n9 = ListNode(9)
n10 = ListNode(10)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10
s.swapNodes(n1, 5)
