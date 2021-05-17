class Solution(object):

    def __init__(self):
        self.stack = []

    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        self.stack = []

        push_idx = 0
        popped_idx =0
        le = 0

        while True:
            le += 1
            print("push idx = ", push_idx)
            print("pop idx = ", popped_idx)
            print("stack = ", self.stack)
            if push_idx < len(pushed):
                self.stack.append(pushed[push_idx])
                push_idx += 1

            while self.stack and  popped_idx < len(popped) and popped[popped_idx] == self.stack[-1]:
                self.stack.pop()
                popped_idx += 1

            if push_idx >= len(pushed) and popped_idx >= len(popped):
                break
            if push_idx >= len(pushed):
                break




        if self.stack:
            print("False")
            return False
        else:
            print("True")
            return True

s = Solution()
s.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1])