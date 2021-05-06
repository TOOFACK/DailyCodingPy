from collections import Counter

t = int(input())
ans = []
for i in range(t):
    was = set()
    temp = int(input())
    word = input()
    tr = True

    for ch in word:
        if ch not in was:
            was.add(ch)
            last_added = ch
        elif ch in was and ch == last_added:
            continue
        else:
            tr = False

    if tr:
        ans.append("YES")
    else:
        ans.append("NO")

for i in ans:
    print(i)
