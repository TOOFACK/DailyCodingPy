t = int(input())
ans = []

for i in range(t):
    c = 0
    val = int(input())
    lent = len(str(val))
    osn = 0

    for i in range(lent):
        pro = 1
        osn += 10 ** i
        while pro <= 9:
            if osn * pro <= val:
                c += 1
            else:
                break
            pro += 1

    ans.append(c)
for i in ans:
    print(i)
