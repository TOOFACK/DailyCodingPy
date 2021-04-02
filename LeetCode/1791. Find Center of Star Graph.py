import collections


class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        ed = {}

        for i in edges:

            if i[0] in ed:
                ed[i[0]] += 1

            else:
                ed[i[0]] = 1

            if i[1] in ed:
                ed[i[1]] += 1

            else:
                ed[i[1]] = 1

        new_dic = dict(sorted(ed.items(), key= lambda x:x[1]))
        return list(new_dic.keys())[-1]
        # return list(dict(sorted(ed.items(), key= lambda x:x[1])).keys())[-1]


s = Solution()
print(s.findCenter([[1,2],[2,3],[4,2]]))
