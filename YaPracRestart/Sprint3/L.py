n = int(input())
moneys = []
for i in input().split():
    moneys.append(int(i))
s = int(input())


def binery_search(money, n, s, left, right, lastGoodIndex=-1):
    if right <= left:
        if lastGoodIndex != -1:
            return lastGoodIndex
        return -1

    print(right,"r")
    print(left,"l")
    mid = (left + right) // 2
    print(mid, "mid")

    if money[mid] - n >= s:
        lastGoodIndex = mid
        return binery_search(money, n, s, left, mid, lastGoodIndex)
    elif money[mid] - n < s:
        return binery_search(money, n, s, mid + 1, right, lastGoodIndex)
    else:
        return binery_search(money, n, s, left, mid, lastGoodIndex)


day1 = binery_search(moneys, 0, s, 0, len(moneys))
day2 = binery_search(moneys, s, s, 0, len(moneys))
if day1 == -1:
    print(-1,end=" ")
else:
    print(day1+1,end=" ")
print(day2+1)