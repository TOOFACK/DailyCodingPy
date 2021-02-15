class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        dict = {}
        ans = []
        for i in range(len(groupSizes)):
            # print(dict)
            if groupSizes[i] in dict:
                tmpLst = dict[groupSizes[i]]
                tmpLst.append(i)
                dict[groupSizes[i]] = tmpLst
                # print("tmpLst = ", tmpLst)
                if len(dict[groupSizes[i]]) == groupSizes[i]:
                    ans.append(dict[groupSizes[i]])
                    del dict[groupSizes[i]]
            else:
                lst = []
                lst.append(i)
                dict[groupSizes[i]] = lst

                if len(dict[groupSizes[i]]) == groupSizes[i]:
                    ans.append(dict[groupSizes[i]])
                    del dict[groupSizes[i]]
        print(ans)
        return ans



s = Solution()
lst = [2,1,3,3,3,2]


s.groupThePeople(lst)