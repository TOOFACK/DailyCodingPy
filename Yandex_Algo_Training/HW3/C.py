n,m = map(int, input().split())
a = set()
b = set()
s = set()

i = 0
while i < n:
    a.add(int(input()))
    i += 1
i = 0
while i < m:
    b.add(int(input()))
    i += 1

for i in a:
    if i in b:
        s.add(i)
for i in b:
    if i in a:
        s.add(i)
for i in s:
    if i in b:
        b.remove(i)
    if i in a:
        a.remove(i)
print(len(s))
for i in sorted(list(s)):
    print(i, end=" ")
print()
print(len(a))
for i in sorted(list(a)):
    print(i, end=" ")
print()
print(len(b))
for i in sorted(list(b)):
    print(i, end= " ")