a = input().split()
a = [int(i) for i in a]
ok = True
for idx in range(len(a)-1):
    if a[idx] >= a[idx+1]:
        ok = False
        break

if ok:
    print("YES")
else:
    print("NO")
