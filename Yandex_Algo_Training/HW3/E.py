form  = set(input().split())
chi = input()
ans = 0
for i in chi:
    if i not in form:
        ans += 1
        form.add(i)
print(ans)
