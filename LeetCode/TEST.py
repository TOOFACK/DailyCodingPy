a = [0,1,2,3,4,5,6,7,8,9]

n = 3
start = 0
end = 9
while start < end:
    mid = (start + end)//2
    print("mid =", mid)
    if a[mid] < n:
        start = mid + 1
    else:
        end = mid
    print("start = ", start)
    print("end = ", end)

print(a[mid])
print(a[start])
print(a[end])