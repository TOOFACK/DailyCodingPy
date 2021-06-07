n = int(input())
a = set()
for i in range(n):
    x, _ = map(int,input().split())
    a.add(x)
print(len(a))