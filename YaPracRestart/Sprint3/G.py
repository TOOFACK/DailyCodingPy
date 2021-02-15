temp = int(input())
lst = []
for i in input().split(" "):
    lst.append(int(i))
t = []
th = []
for i in lst:
    if i == 0:
        print(i, end=" ")
    if i == 1:
        t.append(1)
    if i == 2:
        th.append(2)
for i in t:
    print(i, end=" ")
for i in th:
    print(i, end=" ")

