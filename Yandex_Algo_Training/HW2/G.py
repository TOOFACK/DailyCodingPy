a = list(map(int, input().split()))
mini = min(a)


id = [0]*(max(a) - (mini) + 1)
# print(id)
for i in a:
    id[i - mini] += 1
# print(id)
k = 0
for j in range(max(a), mini-1 , -1):
    for i in range(0 , id[j - mini]):
        a[k] = j
        k += 1
# print(a)

l_1, l_2 = a[0],a[1]
max_1, max_2 = a[-1],a[-2]
if l_1*l_2 > max_1*max_2:
    if l_1 <= l_2:
        print(l_1, l_2)
    else:
        print(l_2,l_1)
else:
    if max_1 < max_2:
        print(max_1,  max_2)
    else:
        print(max_2, max_1)

