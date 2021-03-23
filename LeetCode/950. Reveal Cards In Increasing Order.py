import collections


class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        if len(deck) == 1:
            return deck

        list.sort(deck)
        deq = collections.deque(deck)

        ans = collections.deque()
        a = deq.pop()
        ans.append(a)
        b = deq.pop()
        ans.appendleft(b)

        i = 1
        while deq:
            ans.rotate(-i)
            ans.appendleft(deq.pop())
            i += 1
        return ans


s = Solution()
s.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7])
