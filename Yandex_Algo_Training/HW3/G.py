am_turtle = int(input())
may_ans = set((i, am_turtle - i-1) for i in range(am_turtle))
in_ans = set()
ans = 0
# print(may_ans)
for i in range(am_turtle):
    a, b = map(int, input().split())
    if (a, b) in may_ans and (a, b) not in in_ans:
        in_ans.add((a, b))
        ans += 1
print(ans)
