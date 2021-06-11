customers = {}
with open('input.txt', 'r') as f:
    words1 = (f.read().split('\n'))
    f.close()
    words = []
    for i in words1:
        words.append(i.split(" "))
    print(words)
    if words[-1][0] == '':
        words.pop()
    for i in words:
        # print(i)
        if i[0] not in customers:
            customers[i[0]] = {}

        if i[1] in customers[i[0]]:
            customers[i[0]][i[1]] += int(i[2])
        else:
            customers[i[0]][i[1]] = int(i[2])

        # print(customers)
    for i in list(sorted(customers.keys())):
        print(i + ":")
        for j in list(sorted(customers[i].keys())):
            print(j, customers[i][j])
