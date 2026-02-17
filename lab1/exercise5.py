n = int(input("array size: "))
arr = []

for i in range(n):
    arr.append(int(input()))
k = int(input("k: "))

method = int(input("method 1 2 or 3: "))

if n > 0:
    k = k % n

if method == 1:
    tmp = [0] * n
    for i in range(n):
        tmp[(i + k) % n] = arr[i]
    for i in range(n):
        arr[i] = tmp[i]

elif method == 2:
    for _ in range(k):
        last = arr[n-1]
        i = n - 1
        while i > 0:
            arr[i] = arr[i-1]
            i = i - 1
        arr[0] = last

elif method == 3:
    left = 0
    right = n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left = left + 1
        right = right - 1
    left = 0
    right = k - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left = left + 1
        right = right - 1
    left = k
    right = n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left = left + 1
        right = right - 1

print(arr)
