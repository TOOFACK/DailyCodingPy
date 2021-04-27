import collections


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        tasks = sorted(tasks)
        print(tasks)
        deq = collections.deque(tasks)
        ans = 0
        while deq:
            cur_task = deq.popleft()
            print(deq)
            print("cur_task = ", cur_task)
            ans += 1
            cooldown = n
            while cooldown and deq:
                if deq[-1] != cur_task:
                    print(deq)
                    print(deq[-1], "different task from", cur_task)
                    ans += 1
                    cooldown -= 1
                    cur_task = deq.pop()
                elif deq[0] != cur_task:
                    ans += 1
                    cooldown -= 1
                    cur_task = deq.popleft()
                    print(deq[-1], "equals", cur_task)

        print(ans)
        return ans

s = Solution()
s.leastInterval(["A","B","C","D","E","A","B","C","D","E"], 4)