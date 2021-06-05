t_room, t_con = map(int, input().split())
work = input()
if work == "fan":
    print(t_room)
elif work == "heat":
    if t_room < t_con:
        print(t_con)
    else:
        print(t_room)
elif work == "freeze":
    if t_room > t_con:
        print(t_con)
    else:
        print(t_room)
else:
    print(t_con)