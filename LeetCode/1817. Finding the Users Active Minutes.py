class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        ans = [0] * k
        users = {}
        UAM = {}
        for i in range(k):
            UAM[i+1] = 0
        logs = sorted(logs, key=lambda x: x[0])
        for i in logs:
            if i[0] in users:
                tmp = users[i[0]]
                tmp.add(i[1])
                users[i[0]] = tmp
            else:
                users[i[0]] = {i[1]}
        # print(users)

        for i in list(users.keys()):
            if len(users[i]) in UAM:
                UAM[len(users[i])] += 1
        # print(UAM)

        return list(UAM.values())


s = Solution()
s.findingUsersActiveMinutes(logs = [[1,1],[2,2],[2,3]], k = 4)






