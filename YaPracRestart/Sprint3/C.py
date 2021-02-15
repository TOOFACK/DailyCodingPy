s = input()
t = input()
pos = 0
found = False

for i in t:
    if s[pos] == i:
        pos+=1
    if pos == len(s):
        found = True
        break
if found:
    print(True)
else:
    print(False)    