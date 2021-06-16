n = int(input())
path = []
for i in range(n):
    path.append(list(map(int, input().split())))
m = int(input())
traces = []
for i in range(m):
    traces.append(list(map(int, input().split())))
# print(traces)
ans = []

for (s,f) in (traces):
    curr_h = 0
    ans_curr_h = 0
    print(s,f)
    if s < f:
        s = s-1
        end = f
        f = s+1
    else:
        tmp = s
        f = s -1
        end = s
        f = tmp+1
    while f < end:
        print(s,f)
        print(path[s])
        print(path[f])
        if path[s][1] < path[f][1]:
            curr_h += path[f][1] - path[s][1]
            s +=1
            f +=1
        else:

            ans_curr_h += curr_h
            curr_h = 0
            s +=1
            f +=1
    ans.append(ans_curr_h)

print(ans)
