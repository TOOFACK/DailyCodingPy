import collections
d = {}
d[1] = collections.deque([])
print(d)
if d[1]:
    d[1].popleft()
print(d)