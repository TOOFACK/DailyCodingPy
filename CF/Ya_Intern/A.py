_ = input()
a = list(map(int, input().split()))
tr = True
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        tr = False
        break

if not tr:
    print(-1)
else:
    print(max(a) - min(a))

