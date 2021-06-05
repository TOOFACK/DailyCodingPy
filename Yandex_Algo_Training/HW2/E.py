_ = input()
a = list(map(int,input().split()))
maxi = max(a)
idx_m = a.index(maxi)
did = -1

for i in range(idx_m+1, len(a)):
    if a[i] % 10 == 5 and i+1 < len(a) and a[i+1] < a[i] and did < a[i]:
        did = a[i]

if did == -1:
    print(0)
else:
    a = sorted(a, reverse= True)
    place = a.index(did)
    print(place+1)
