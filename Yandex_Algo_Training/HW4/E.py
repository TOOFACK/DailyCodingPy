n = int(input())
blocks = []
a = set()
c = {}
for i in range(n):
    blocks.append(tuple(map(int, input().split())))
    a.add(blocks[i][0])
    if blocks[i][0] in c:
        if blocks[i][1] > c[blocks[i][0]]:
            c[blocks[i][0]] = blocks[i][1]
    else:
        c[blocks[i][0]] = blocks[i][1]



# print(c)
# print(blocks)
# print(a)
widths = sorted(list(a))
ans = 0
for i in widths:
    ans += c[i]
print(ans)

