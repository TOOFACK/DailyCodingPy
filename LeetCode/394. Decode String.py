import collections


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        vals = collections.deque()
        seq = []
        curr_num = 0

        curr_str = ""
        for i in s:
            # print(i)
            if i.isdigit():
                curr_num = curr_num*10 + int(i)
            elif i == "[":
                seq.append(curr_str)
                vals.append(curr_num)
                curr_str = ""
                curr_num = 0

            elif i == "]":
                curr_str = seq.pop() + vals.pop() * curr_str
            else:
                curr_str += i
        print(curr_str)
        return curr_str


s = Solution()
s.decodeString("100[abc]")













