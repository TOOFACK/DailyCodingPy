d = {2: "abc",
     3: "def",
     4: "ghi",
     5: "jkl",
     6: "mno",
     7: "pqrs",
     8: "tuv",
     9: "wxyz"}

c = input()


def gen_leeters(index, length, d, c, ans):
    if length == len(c):
        print(ans)
        if index <= len(d[int(c[length - 1])]):
            ans = ans[:-1]
            gen_leeters(index + 1, length, d, c, ans + d[int(c[length - 1])][index + 1])
        else:
            return

    if length < len(c):
        # print(countF, "cF", countS, "cS")
        # for i in d[b]:
        #     print(d[a][countF], i)
        gen_leeters(index, length + 1, d, c, ans + d[int(c[length])][index])


gen_leeters(0, 0, d, c, "")
