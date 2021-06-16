from collections import defaultdict

_, target = map(int, input().split())
mas = list(map(int, input().split()))
d = defaultdict(int)
pref = 0
ans = 0
d[pref] += 1

for i in range(len(mas)):
    # sum(L,R) = sum(0,R) - sum(0,L-1)==k
    # sum(0,L-1) = sum(0,R) - k
    pref += mas[i]
    need = pref - target
    ans += d[need]
    d[pref] += 1

# print(d)
print(ans)
