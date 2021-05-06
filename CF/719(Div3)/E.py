for _ in range(int(input())):
    lent = int(input())
    curr = 1
    stroka = input()
    mas = []
    min_sr = lent
    sr_idx = 0
    for i in range(len(stroka)):
        if stroka[i] == "*":
            if abs(lent / 2 - i + 1) < min_sr:
                min_sr = abs(lent / 2 - i + 1)
                sr_idx = i + 1
            mas.append(curr)
            curr += 1
        else:
            curr += 1
    print(mas)
    print(sr_idx)
    l = r = sr_idx
    ans = 0
    for i in mas:
        if i != sr_idx:
            if i < sr_idx:
                ans += abs(l - i -1)
                l = sr_idx-1
            else:
                ans+=abs(r-i-1)
                r=sr_idx+1

    print(ans)
