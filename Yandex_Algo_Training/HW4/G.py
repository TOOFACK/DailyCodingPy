with open('input.txt', 'r') as f:
    syst = {}
    words1 = (f.read().split('\n'))
    f.close()
    opers = []
    for i in words1:
        opers.append(i.split(" "))
    # print(words)
    if opers[-1][0] == '':
        opers.pop()
    ans = []
    for i in opers:

        if i[0] == "DEPOSIT":
            if i[1] in syst:
                syst[i[1]] += int(i[2])
            else:
                syst[i[1]] = int(i[2])
        elif i[0] == "INCOME":
            for k in syst.keys():
                if syst[k] > 0:
                    syst[k] +=  int(syst[k] * (int(i[1]) / 100))
        elif i[0] == "BALANCE":
            if i[1] in syst:
                ans.append(syst[i[1]])
            else:
                ans.append("ERROR")
        elif i[0] == "WITHDRAW":
            if i[1] in syst:
                syst[i[1]] -= int(i[2])
            else:
                syst[i[1]] = -int(i[2])
        elif i[0] == "TRANSFER":
            if i[1] in syst:
                syst[i[1]] -= int(i[3])
            else:
                syst[i[1]] = -int(i[3])
            if i[2] in syst:
                syst[i[2]] += int(i[3])
            else:
                syst[i[2]] = int(i[3])
    for i in ans:
        print(i)
