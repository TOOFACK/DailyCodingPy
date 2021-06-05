_ = input()
a = input().split()
val = int(input())
dif = 100001
ans = 0
a = [int(i) for i in a]
for c in a:
    if abs(c - val) < dif:
        dif = abs(c - val)
        ans = c
print(ans)
