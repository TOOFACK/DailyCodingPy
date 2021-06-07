str1 = input()
str2 = input()
a1 = []
b = set()
ans = 0
for i in range(len(str1) - 1):
    a1.append(str1[i] + str1[i + 1])
for i in range(len(str2) - 1):
    b.add(str2[i] + str2[i + 1])
for i in a1:
    if i in b:
        ans += 1
print(ans)
