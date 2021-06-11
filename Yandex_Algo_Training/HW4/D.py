n = int(input())
keys_max_push = list(map(int, input().split()))
_ = input()
keys_pushed = list(map(int, input().split()))
for i in keys_pushed:
    keys_max_push[i-1] -= 1
for i in keys_max_push:
    if i < 0:
        print("YES")
    else:
        print("NO")