a = list(map(int, input().split()))
am = 0
for idx in range(len(a)):
    if idx - 1 >=0 and idx + 1< len(a):
        if a[idx] > a[idx-1] and a[idx] > a[idx+1]:
            am += 1
print(am)
