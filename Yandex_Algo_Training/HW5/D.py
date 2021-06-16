_, r = map(int, input().split())
l = 0
last = 0
ans = 0
mas = list(map(int, input().split()))
for l in range(len(mas)):
    while last < len(mas) and mas[last] - mas[l] <= r:

        last += 1
    ans += len(mas) - last
print(ans)
