a = list(map(int, input().split()))
max_1 = 1
max_2 = 1
idx_m = -1
l_idx = -1
l_1 = -1
l_2 = -1
for idx, val in enumerate(a):
    if val >= max_1:
        max_2 = max_1
        max_1 = val
        idx_m = idx
    if max_2 <= val <= max_1 and idx != idx_m:
        max_2 = val

for idx, val in enumerate(a):
    if val <= l_1:
        l_2 = l_1
        l_1 = val
        l_idx = idx
    if l_2 >= val >= l_1 and l_idx != idx:
        l_2 = val
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