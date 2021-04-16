arr = [
  " /",
  "/ "
]
print(arr)
print(arr[0].split())
new_arr = []
for i in arr:
    print(i)
    tmp = i.split("")
    new_arr.append(list.copy(tmp))
    tmp.clear()
print(new_arr)