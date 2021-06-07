from bisect import bisect_left

arr = [1,4,100,101]
x = 100
left = bisect_left(arr, x)-1
print(left)