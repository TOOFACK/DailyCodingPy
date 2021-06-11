_, _ = input().split()
p = input()
s = input()
count = len(p)
ans = 0
table = {}

for i in p:
    if i in table:
        table[i] += 1
    else:
        table[i] = 1
l = r = 0

while r < len(s):
    print("r = ", r)
    print("l = ", l)
    print("s[r] = ", s[r])
    print("s[l] = ", s[l])
    print("count = ", count)
    print("table = ", table)
    if s[r] in table:
        table[s[r]] -= 1
        if table[s[r]] >= 0:
            count -= 1
        else:
            count += 1

    if r - l == len(p):
        if s[l] in table:

            table[s[l]] += 1
            if table[s[l]] > 0:
                count += 1
            else:
                count -= 1

        l += 1
    r += 1

    if count == 0:
        ans += 1

print(ans)
