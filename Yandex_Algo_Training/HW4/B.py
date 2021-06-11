with open('input.txt', 'r') as f:
    sents = f.read().split()
    a = {}
    ans = []
    for i in sents:
        if i in a:
            ans.append(a[i])
            a[i] += 1
        else:
            ans.append(0)
            a[i] = 1
    for i in ans:
        print(i, end=" ")
# 0 0 0 0 0 0 1 0 0 1 0 0 1 0 2 2 0 0 0 0 1 2 3 3 1 1 4 0 1 0 1 2 4 1 5 0 0
# 0 0 0 0 0 0 1 0 0 1 0 0 1 0 2 2 0 0 0 0 1 2 3 3 1 1 4 0 1 0 1 2 4 1 5 0 0