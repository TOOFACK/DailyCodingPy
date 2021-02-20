from collections import deque

lst = [1, 2, 3, 4, 5, 6]
s = 0
for i in lst:
    for j in lst:
        for k in lst:
            if i + j + k > 12:
                s += 1
print(s)

