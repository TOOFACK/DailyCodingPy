old_pos = set()
new_pos = set()
ok_pos = set()

t, d, n = map(int, input().split())

for x in range(0 - t, t + 1):
    for y in range(- t, t + 1):
        # print(x,y)
        if abs(- x) + abs(- y) <= t:
            old_pos.add((x, y))
        if abs(+ x) + abs(+ y) <= t:
            old_pos.add((-x, -y))

_x, _y = map(int, input().split())
for x in range(_x - d, d + 1 + _x):
    for y in range(_y - d, d + 1 + _y):
        if (x, y) in old_pos and abs(_x-x) + abs(_y-y) <= d:
            ok_pos.add((x, y))

old_pos = set.copy(ok_pos)
ok_pos.clear()
new_pos.clear()
# print(old_pos)

for i in range(n-1):

    for (x, y) in old_pos:
        for j in range(-t, t+1):
            new_pos.add((x+j,y))
            new_pos.add((x, y+j))

        # for _x in range(x- t, x+t + 1):
        #     for _y in range(y- t, y+t + 1):
        #         if abs(_x - x) + abs(_y - y) <= t:
        #             new_pos.add((_x, _y))
        #         if abs(_x + x) + abs(_y + y) <= t:
        #             new_pos.add((-_x, -_y))

    _x, _y = map(int, input().split())
    # print("old = ", old_pos)
    # print("new_pos = ", new_pos)
    for x in range(_x - d, d + 1 + _x):
        for y in range(_y - d, d + 1 + _y):
            if (x, y) in new_pos and abs(_x-x) + abs(_y-y) <= d:
                ok_pos.add((x, y))
                # ok_pos.add((x_old, y_old))
    # print("ok_pos = ", ok_pos)

    old_pos = set.copy(ok_pos)
    ok_pos.clear()
    new_pos.clear()

print(len(old_pos))
for i in old_pos:
    print(str(i).replace(")", "").replace("(", "").replace(",", ""))
