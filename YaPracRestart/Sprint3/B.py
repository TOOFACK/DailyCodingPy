d = {2: "abc",
     3: "def",
     4: "ghi",
     5: "jkl",
     6: "mno",
     7: "pqrs",
     8: "tuv",
     9: "wxyz"}

c = input()


def gen_leeters(length, d, c, ans):
    if length == len(c):
        print(ans,end=" ")

        return

    for i in d[int(c[length])]:
        gen_leeters(length+1,d,c,ans+i)


gen_leeters(0, d, c, "")
