own = input().replace("-","").replace("(","").replace(")","")
first = input().replace("-","")
sec = input().replace("-","")
thir = input().replace("-","")


if own[0] == "8":
    own = own[1:]
elif own[0] == "+":
    own = own[2:]
if len(own) == 10:
    code = own[0:3]
    number = own[3:]
else:
    code = "495"
    number = own

if first[0] == "8":
    first = first[1:]
elif first[0] == "+":
    first = first[2:]

if sec[0] == "8":
    sec = sec[1:]
elif sec[0] == "+":
    sec = sec[2:]

if thir[0] == "8":
    thir = thir[1:]
elif thir[0] == "+":
    thir = thir[2:]


if len(first) == 10:
    if first[0:3] == code and first[3:] == number:
        print("YES")
    else:
        print("NO")
elif len(first) == 7:
    if "495" == code and first == number:
        print("YES")
    else:
        print("NO")
else:
    print("NO")

if len(sec) == 10:
    if sec[0:3] == code and sec[3:] == number:
        print("YES")
    else:
        print("NO")
elif len(sec) == 7:
    if "495" == code and sec == number:
        print("YES")
    else:
        print("NO")
else:
    print("NO")


if len(thir) == 10:
    if thir[0:3] == code and thir[3:] == number:
        print("YES")
    else:
        print("NO")
elif len(thir) == 7:
    if "495" == code and thir == number:
        print("YES")
    else:
        print("NO")
else:
    print("NO")