_, types = map(int, input().split())
trees = list(map(int, input().split()))
formed = 0
required = types
window = {}
ans = [1000000000, 0, 0]

r = l = 0
while r < len(trees):
    window[trees[r]] = window.get(trees[r], 0) + 1

    if window[trees[r]] == 1:
        formed +=1

    while l <= r and formed == required:
        if r - l + 1 < ans[0]:
            ans[0] = r-l+1
            ans[1] = l
            ans[2] = r
        window[trees[l]] -= 1
        if window[trees[l]] < 1:
            formed -= 1

        l +=1
    r +=1
print(ans[1] + 1,ans[2] + 1)



