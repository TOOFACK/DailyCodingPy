class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        #->
        minDown = -1
        minUp = 9
        minRight = 9
        minLeft = -1
        diag1 = [king[0] + 8, king[1] - 8]
        diag2 = [king[0] - 8, king[1] + 8]
        diag3 = [king[0] - 8, king[1] - 8]
        diag4 = [king[0]+8, king[1]+8]
        d1 = False
        d2 = False
        d3 = False
        d4 = False

        for coors in queens:
            if coors[0] == king[0]:
                if coors[1] > king[1]:
                    minRight = min(minRight, coors[1])
                else:
                    minLeft = max(minLeft, coors[1])
            elif coors[1] == king[1]:
                if coors[0] > king[0]:
                    minUp = min(minUp,coors[0])
                else:
                    minDown = max(minDown, coors[0])

            if abs(coors[0] - king[0]) == abs(coors[1] - king[1]):
                # print(coors)
                if king[0] < coors[0] and king[1] > coors[1]:
                    if coors[0] < diag1[0] and coors[1] > diag1[1]:
                        diag1 = coors
                        d1 = True
                elif king[0] > coors[0] and king[1] < coors[1]:
                    if coors[0] > diag2[0] and coors[1] < diag2[1]:
                        diag2 = coors
                        d2 = True
                elif king[0] > coors[0] and king[1] > coors[1]:
                    if coors[0] > diag3[0] and coors[1] > diag3[1]:
                        diag3 = coors
                        d3 = True
                elif king[0] < coors[0] and king[1]< coors[1]:
                    if coors[0] < diag4[0] and coors[1] < diag4[1]:
                        diag4 = coors
                        d4 = True
        ans = []
        if minDown != -1:
            ans.append([minDown, king[1]])
        if minUp != 9:
            ans.append([minUp, king[1]])
        if minRight != 9:
            ans.append([king[0],minRight])
        if minLeft != -1:
            ans.append([king[0],minLeft])
        if d1:
            ans.append(diag1)
        if d2:
            ans.append(diag2)
        if d3:
            ans.append(diag3)
        if d4:
            ans.append(diag4)

        # print(minUp, minDown,minLeft,minRight, diag1, diag2, diag3, diag4)
        return ans

s = Solution()
s.queensAttacktheKing(queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4])




