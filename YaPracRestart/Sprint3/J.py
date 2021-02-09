temp = int(input())
mas = []
for i in input().split(" "):
    mas.append(int(i))
swap = False
tr = 1
for i in range(len(mas)):

    for j in range(len(mas)-1):
        if mas[j] > mas[j+1]:
            swap = True

            tmp = mas[j]
            mas[j] = mas[j+1]
            mas[j+1] = tmp
    if swap:
        tr = 0
        for k in mas:
            print(k,end=" ")
        print()
        swap = False
if tr:
    for k in mas:
        print(k, end=" ")
    print()