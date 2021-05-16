s = "5525"
b = 2
tmp = s[len(s) - b:] + s[0:len(s) - b]
# print(s[0:])
print(tmp)