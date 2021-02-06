n = int(input())


def gen_branch(n, l, r, ans):
    if l + r == 2 * n:
        print(ans)
        return

    if l < n:
        gen_branch(n, l + 1, r, ans + '(')

    if l > r:
        gen_branch(n, l, r + 1, ans + ')')


gen_branch(n, 0, 0, "")
