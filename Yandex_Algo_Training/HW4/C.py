import struct
with open('input.txt', 'r') as f:
    a = {}
    words = list(f.read().split())
    for i in words:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    all_words = []
# print(a)
    max = -1
    for i in a.keys():
        if a[i] > max:
            max = a[i]
    for i in a.keys():
        if a[i] == max:
            all_words.append(i)
# print(all_words)
    print(sorted(all_words)[0])

