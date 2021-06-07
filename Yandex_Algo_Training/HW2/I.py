row, col, am_mins = map(int, input().split())
mins = []
for i in range(am_mins):
    mins.append(list(map(int, input().split())))
# print(mins)
pole = []
for i in range(row):
    pole.append([0] * col)
for coor in mins:
    pole[coor[0] - 1][coor[1] - 1] = "*"
# print(pole)


def in_pole(x, y):
    return  0 <= x <= row-1 and 0 <= y <= col-1


for r in range(row):
    for c in range(col):
        cur = 0
        if pole[r][c] != "*":
            if in_pole(r - 1, c - 1) and pole[r - 1][c - 1] == "*":
                cur += 1
            if in_pole(r - 1, c) and pole[r - 1][c] == "*":
                cur += 1
            if in_pole(r + 1, c) and pole[r + 1][c] == "*":
                cur += 1
            if in_pole(r, c - 1) and pole[r][c - 1] == "*":
                cur += 1
            if in_pole(r, c + 1) and pole[r][c + 1] == "*":
                cur += 1
            if in_pole(r - 1, c + 1) and pole[r - 1][c + 1] == "*":
                cur += 1
            if in_pole(r + 1, c + 1) and pole[r + 1][c + 1] == "*":
                cur += 1
            if in_pole(r + 1, c - 1) and pole[r + 1][c - 1] == "*":
                cur += 1
            pole[r][c] = cur
for i in pole:
    print(str(i).replace("[", "").replace(",", "").replace("]","").replace("'", ""), end="\n")
