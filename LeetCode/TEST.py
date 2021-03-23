import collections
from collections import deque

lst = [1,2,3]
print(lst[0:1])
print(lst)
b = [17,13,11,2,3,5,7]
list.sort(b)
ans = collections.deque(b)
print(ans)
ans.rotate(-1)
print(ans)
ans.rotate(2)
print(ans)
ans.rotate(3)
print(ans)
ans.rotate(4)
print(ans)