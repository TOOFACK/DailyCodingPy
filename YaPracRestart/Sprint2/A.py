n = int(input())
m = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))

list = []
for i in range(m):
    for j in range(n):
        list.append(matrix[j][i])
    print(' '.join(map(str, list)))
    list.clear()