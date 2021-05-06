for _ in range(int(input())):
    d = {}
    a = int(input())
    ans = 0
    mas = [int(x) for x in input().split(" ")]
    for i in range(len(mas)):
        if mas[i] - i in d:
            ans += d[mas[i]-i]
            d[mas[i]-i]+=1
        else:
            d[mas[i] - i] = 1
    print(ans)