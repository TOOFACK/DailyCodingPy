
lent = int(input())
pos = [int(char) for char in input().split(" ")]
# print(pos)
ans = []
a = [i for i in range(1, lent+1)]
for i in pos[::-1]:
    # print(a)

    index_to_del = len(a)-i-1
    # print("idx = ", index_to_del)
    ans.append(a[index_to_del])
    a[index_to_del] = 0
    a = [i for i in a if i != 0]
for i in ans[::-1]:
    print(i, end=" ")