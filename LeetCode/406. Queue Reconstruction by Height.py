class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people_dict = {}
        height = []
        res = []

        for p in people:
            if p[0] in people_dict:
                people_dict[p[0]] += [(p[0], p[1])]
            else:
                people_dict[p[0]] = [(p[0], p[1])]
                height.append(p[0])
        list.sort(height)

        for h in height[::-1]:
            people_dict[h].sort(key=lambda x:x[1])
            for p in people_dict[h]:
                res.insert(p[1],(p[0],p[1]))

        print(res)
        return res

s = Solution()
s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])