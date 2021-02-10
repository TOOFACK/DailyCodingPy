temp = int(input())
lst = []
for i in input().split(" "):
    lst.append(i)


def compare(a, b):
    if int(a + b) > int(b + a):
        return True
    else:
        return False


# print(lst)


def puzir(mas):
    for i in range(len(mas)):
        for j in range(len(mas) - 1):
            if not compare(mas[j], mas[j + 1]):
                tmp = mas[j]
                mas[j] = mas[j + 1]
                mas[j + 1] = tmp

#
puzir(lst)
# print(lst)
for i in lst:
    print(i, end="")
