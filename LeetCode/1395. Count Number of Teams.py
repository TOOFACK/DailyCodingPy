class Solution:
    def numTeams(self, rating):
        ans = 0
        for j in range(len(rating)):
            rightS = 0
            rightG = 0
            leftS = 0
            leftG = 0
            i = 0
            while i < j:
                if rating[i] < rating[j]:
                    rightS += 1
                elif rating[i] > rating[j]:
                    rightG += 1
                i+=1
            k = j + 1
            while k < len(rating):
                if rating[k] < rating[j]:
                    leftS += 1
                elif rating[k] > rating[j]:
                    leftG += 1
                k+=1
            ans += leftS * rightG + leftG * rightS
        print(ans)
        return ans





