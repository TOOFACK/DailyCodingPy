_ = input()
a = list(map(int, input().split()))


def slow(seq):
    for start in range(len(seq)):
        i = start
        j = len(seq) - 1
        while i < len(seq) and j >= 0 and seq[i] == seq[j] and i <= j:
            i += 1
            j -= 1
        if i > j:
            print(start)
            # print(reversed(seq[0:start]))
            return reversed(seq[0:start])


ans = slow(a)
print(*ans)
