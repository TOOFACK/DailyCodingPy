a = int(input())
b = int(input())
c = int(input())
if c < 0:
    print("NO SOLUTION")
elif a == 0:
    print("MANY SOLUTIONS")
else:
    x = (c**2-b)/a
    if x.is_integer():
        print(int(x))
    else:
        print("NO SOLUTION")
