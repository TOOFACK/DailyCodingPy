from asyncio import PriorityQueue


n, k = map(int, input().split())
a = list(map(int, input().split()))

last_ans = {i: 0 for i in a}
b = sorted(a)


def printKclosest(arr, n, x, k):
    # Make a max heap of difference with
    # first k elements.
    pq = PriorityQueue()
    for i in range(k):
        pq.put((-abs(arr[i] - x), i))

    # Now process remaining elements
    for i in range(k, n):
        diff = abs(arr[i] - x)
        p, pi = pq.get()
        curr = -p

        # If difference with current
        # element is more than root,
        # then put it back.
        if diff > curr:
            pq.put((-curr, pi))
            continue
        else:

            # Else remove root and insert
            pq.put((-diff, i))

    # Print contents of heap.
    curr = 0
    while (not pq.empty()):
        p, q = pq.get()
        curr += abs(val -arr[q])
    last_ans[val]=curr

for idx, val in enumerate(b):
    printKclosest(a,n,val,k)



for i in a:
    print(last_ans[i], end=" ")
