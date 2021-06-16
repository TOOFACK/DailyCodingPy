_ = input()
mikes = list(map(int, input().split()))
_ = input()
pants = list(map(int, input().split()))

point_m = point_p = 0
ans_p = ans_m = 0
dif = 10000000000000
while point_m < len(mikes) and point_p < len(pants):

    if abs(mikes[point_m] - pants[point_p]) < dif:
        dif = abs(mikes[point_m] - pants[point_p])
        ans_p = pants[point_p]
        ans_m = mikes[point_m]

    if mikes[point_m] > pants[point_p]:
        point_p += 1
    else:
        point_m += 1


# while point_m < len(mikes):
#     if abs(pants[point_p] - pants[point_p]) < dif:
#         dif = abs(mikes[point_m] - pants[point_p])
#         ans_p = pants[point_p]
#         ans_m = mikes[point_m]
#     point_m += 1
#
# while point_p < len(pants):
#     if abs(pants[point_p] - pants[point_p]) < dif:
#         dif = abs(mikes[point_m] - pants[point_p])
#         ans_p = pants[point_p]
#         ans_m = mikes[point_m]
#     point_p += 1

print(ans_m, ans_p)
