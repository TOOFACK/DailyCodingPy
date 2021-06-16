n = int(input())
watts = list(map(int, input().split()))
m = int(input())
models = []
for i in range(m):
    models.append(list(map(int, input().split())))
# print(models)
mapa = {}
for i in models:
    if i[0] in models and mapa[i[0]] > i[1]:
        mapa[i[0]] = i[1]
    else:
        mapa[i[0]] = i[1]
# print(mapa)
ans = 0
for watt in watts:
    price = 10000000000000000
    for k in mapa.keys():
        if k >= watt and price > mapa[k]:
            price = mapa[k]
    ans += price
print(ans)
