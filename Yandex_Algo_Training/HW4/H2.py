table = {}
ans = 0
_, _ = input().split()
p = input()
s = input()
count = len(p)

for i in p:
    if i in table:
        table[i] += 1
    else:
        table[i] = 1

l = r = 0

while r < len(s):

    if s[r] in table:
        table[s[r]] -= 1
        if table[s[r]] >= 0:
            count -= 1

    if r - l == len(p):
        if s[l] in table:
            if table[s[l]] >= 0:
                count += 1
            table[s[l]] += 1

        l += 1
    r += 1

    if count == 0:
        ans += 1

print(ans)
