def bin_search(mas, target):
    l = 0
    r = len(mas) - 1

    while l <= r:
        mid = (l + r) // 2
        if mas[mid] < target:
            l = mid + 1
        elif mas[mid] > target:
            r = mid - 1
        else:
            return mid
    return -1
