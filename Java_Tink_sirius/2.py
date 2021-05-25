s = input()
t = input()

set_s = set(s)
ans = 0

for i in t:
    if i in set_s:
        ans += 1

print(ans + 1)
