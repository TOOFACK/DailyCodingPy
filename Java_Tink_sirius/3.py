w = [int(i) for i in input().split(" ")]
l = w[0]
r = w[1]
x = w[2]
ans = [-1,-1,-1]

max_len = len(bin(x)[2:])
for k in range(1,max_len+10):

    first_val = bin(x)[2:]
    sec_val = bin(x)[2:]
    # print("f = ", first_val)
    # print("s = ", sec_val)
    # print("k = ", k)

    first_val = "0b" + first_val[:-k] + "0"*k
    sec_val = "0b" + sec_val[:-k] + "1"*k

    # print("f = ", first_val)
    # print("s = ", sec_val)

    if l <= int(first_val,2) <= r and l <= l <= int(sec_val, 2) <= r and k > ans[0]:
        ans[0] = k
        ans[1] = int(first_val, 2)
        ans[2] = int(sec_val, 2)
for i in ans:
    print(i, end=" ")

