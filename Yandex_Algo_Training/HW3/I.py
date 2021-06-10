am_pupils = int(input())
d = {}
for i in range(am_pupils):
    j = 0
    k = int(input())
    new_s = set()
    while j < k:
        lang = input()
        if lang in d:
            d[lang] += 1
        else:
            d[lang] = 1
        j += 1
all_know = []
one = []
for k in d.keys():
    one.append(k)
    if d[k] % am_pupils == 0:
        all_know.append(k)
print(len(all_know))
for i in all_know:
    print(i)
print(len(one))
for i in one:
    print(i)




