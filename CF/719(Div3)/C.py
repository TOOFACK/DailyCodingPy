t = int(input())


def in_matrix(row, col):
    if 0 <= row < n and 0 <= col < n:
        return True
    else:
        return False


for i in range(t):
    n = int(input())
    if n == 2:
        print(-1)
    elif n == 1:
        print(1)
    else:
        vals = [v for v in range(1, n * n + 1)]
        # print(vals)

        idxs = []
        matrix = []
        for col in range(n):
            matrix.append([0] * n)
        col = 0
        for row in range(n - 1, -1, -1):
            idxs.append((row, col))
            if row != 0:
                idxs.append((0, row))
        # row = 0
        # for col in range(1,n+1):
        #     idxs.append((row,col))
        # idxs = sorted(idxs)
        # print(idxs)
        for coor in idxs:
            row = coor[0]
            col = coor[1]
            vals_idx = 0
            while in_matrix(row, col):
                matrix[row][col] = vals.pop()

                # print("vals = ", vals)
                # print(row, col)
                row += 1
                col += 1
                # print(in_matrix(row,col))

        for row in matrix:
            for col in row:
                print(col, end=" ")
            print()
