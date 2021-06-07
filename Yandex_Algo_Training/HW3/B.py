a = set(map(int, input().split()))
b = set(map(int, input().split()))
ans = set()

for i in a:
    if i in b:
        ans.add(i)
for i in b:
    if i in a:
        ans.add(i)
ans = list(ans)
print(str(sorted(ans)).replace("[","").replace("]","").replace(",",""))