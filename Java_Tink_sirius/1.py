n = int(input())
m = int(input())

zamena = 0
ost = 0
for i in range(n):
    zamena += (m // 9)
    ost += (m % 9)
print(zamena)
print(ost * 6)