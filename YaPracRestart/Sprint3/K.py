def merge(arr, left, mid, right):
    if right - left <= 1:
        return arr[left]
    L = arr[left:mid]
    R = arr[mid:right]

    l = 0
    r = 0
    k = 0
    ans = [] * len(arr)

    while l < len(L) and r < len(R):
        if L[l] <= R[r]:
            ans[k] = L[l]
            l += 1
        else:
            ans[k] = R[r]
            r += 1
        k += 1

    while l < len(L):
        ans[k] = L[l]
        l += 1
        k += 1

    while r < len(R):
        ans[k] = R[r]
        r += 1
        k += 1

    return ans


def merge_sort(arr, left: int, right: int):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge(arr, left, mid, right)

        merge_sort(arr, mid, right)

        merge(arr, left, mid, right)


arr = [12, 11, 13, 5, 6, 7]

print(arr)
merge_sort(arr,0, len(arr))
print(arr)
