n = int(input())
a = {}
b = {}

for i in range(n):
    w1, w2 = input().split()
    a[w1] = w2
    b[w2] = w1
word = input()
if word in a:
    print(a[word])
else:
    print(b[word])
